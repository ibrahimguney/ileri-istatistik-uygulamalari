import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import stats

PERMUTATIONS = 19999
SEED = 202606
SOURCE_HASH = "51dcab9aeaa121123dd28a00156d4dfa398c38eecad69bd5699ae4cea03e5ee9"


def summarize(data):
    first = data["G1"].to_numpy(dtype=float)
    final = data["G3"].to_numpy(dtype=float)
    pearson = stats.pearsonr(first, final)
    spearman = stats.spearmanr(first, final)
    rank_first = stats.rankdata(first, method="average")
    rank_final = stats.rankdata(final, method="average")
    np.testing.assert_allclose(pearson.statistic, np.corrcoef(first, final)[0, 1])
    np.testing.assert_allclose(spearman.statistic, np.corrcoef(rank_first, rank_final)[0, 1])
    np.testing.assert_allclose(rank_first, data["G1"].rank(method="average"))
    centered_first = first - first.mean()
    centered_final = final - final.mean()
    sum_xx = centered_first @ centered_first
    sum_yy = centered_final @ centered_final
    sum_xy = centered_first @ centered_final
    np.testing.assert_allclose(pearson.statistic, sum_xy / np.sqrt(sum_xx * sum_yy))
    statistic_t = pearson.statistic * np.sqrt((len(data) - 2) / (1 - pearson.statistic ** 2))
    np.testing.assert_allclose(pearson.pvalue, 2 * stats.t.sf(abs(statistic_t), len(data) - 2),
                               rtol=1e-10, atol=0)
    fisher = np.arctanh(pearson.statistic)
    fisher_bounds = np.tanh(fisher + np.array([-1, 1]) * stats.norm.ppf(0.975) / np.sqrt(len(data) - 3))
    interval = pearson.confidence_interval(confidence_level=0.95)
    np.testing.assert_allclose(fisher_bounds, [interval.low, interval.high])
    design = np.column_stack([np.ones(len(data)), first])
    coefficients = np.linalg.lstsq(design, final, rcond=None)[0]
    residuals = final - design @ coefficients
    regression_r2 = 1 - np.sum(residuals ** 2) / sum_yy
    np.testing.assert_allclose(pearson.statistic ** 2, regression_r2)
    np.testing.assert_allclose(stats.pearsonr(5 * first, final).statistic, pearson.statistic)
    np.testing.assert_allclose(stats.spearmanr(5 * first, final).statistic, spearman.statistic)
    return {
        "n": len(data), "pearson_r": float(pearson.statistic),
        "pearson_t": float(statistic_t), "pearson_p_classical": float(pearson.pvalue),
        "pearson_fisher_ci": fisher_bounds.tolist(),
        "spearman_r": float(spearman.statistic),
        "spearman_p_asymptotic": float(spearman.pvalue),
        "Sxx": float(sum_xx), "Syy": float(sum_yy), "Sxy": float(sum_xy),
        "x_mean": float(first.mean()), "y_mean": float(final.mean()),
        "x_sd": float(np.std(first, ddof=1)), "y_sd": float(np.std(final, ddof=1)),
        "pearson_r_squared": float(pearson.statistic ** 2),
        "regression_intercept": float(coefficients[0]), "regression_slope": float(coefficients[1])
    }


def permutation_check(data):
    rank_first = stats.rankdata(data["G1"], method="average")
    rank_final = stats.rankdata(data["G3"], method="average")
    centered_first = rank_first - rank_first.mean()
    centered_final = rank_final - rank_final.mean()
    denominator = np.linalg.norm(centered_first) * np.linalg.norm(centered_final)
    observed = centered_first @ centered_final / denominator
    generator = np.random.default_rng(SEED)
    extreme = 0
    for repetition in range(PERMUTATIONS):
        permutation = generator.permutation(len(data))
        statistic = centered_first @ centered_final[permutation] / denominator
        if repetition < 5:
            np.testing.assert_allclose(statistic,
                                       stats.spearmanr(data["G1"], data["G3"].to_numpy()[permutation]).statistic)
        extreme += int(abs(statistic) >= abs(observed) - 1e-14)
    return {"B": PERMUTATIONS, "seed": SEED, "extreme": extreme,
            "p_absolute_two_sided": (extreme + 1) / (PERMUTATIONS + 1),
            "minimum_reportable_p": 1 / (PERMUTATIONS + 1)}


def main():
    directory = Path(__file__).resolve().parent
    source_path = directory / "veri.csv"
    original_bytes = source_path.read_bytes()
    normalized_bytes = original_bytes.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    assert hashlib.sha256(normalized_bytes).hexdigest() == SOURCE_HASH
    source = pd.read_csv(source_path)
    assert list(source.columns) == ["kaynak_satir", "school", "G1", "G3"]
    assert len(source) == 80 and source.notna().all().all()
    np.testing.assert_array_equal(source["kaynak_satir"], np.arange(1, 81))
    assert source["school"].eq("GP").all()
    assert source[["G1", "G3"]].apply(lambda column: column.between(0, 20).all()).all()
    data = source.iloc[:60].copy()
    transfer = source.iloc[60:80].copy()
    complete = summarize(data)
    without_first = summarize(data.iloc[1:])
    independent = summarize(transfer)
    np.testing.assert_allclose([complete["Sxx"], complete["Syy"], complete["Sxy"]],
                               [385.4, 234.18333333333334, 224.3])
    sensitivity = []
    for index in data.index:
        remaining = data.drop(index=index)
        sensitivity.append({"cikarilan_kaynak_satir": int(data.loc[index, "kaynak_satir"]),
                            "n": len(remaining),
                            "pearson_r": float(stats.pearsonr(remaining.G1, remaining.G3).statistic),
                            "spearman_r": float(stats.spearmanr(remaining.G1, remaining.G3).statistic)})
    ranked = data.assign(sira_G1=stats.rankdata(data.G1, method="average"),
                         sira_G3=stats.rankdata(data.G3, method="average"))
    results = {
        "source_doi": "10.24432/C5TG7T",
        "local_projection_sha256": hashlib.sha256(original_bytes).hexdigest(),
        "normalized_LF_sha256": SOURCE_HASH,
        "selection": "Local veri.csv: rows 1-60 main, rows 61-80 exercise",
        "main": complete, "without_source_row_1": without_first, "transfer": independent,
        "spearman_permutation": permutation_check(data),
        "versions": {"numpy": np.__version__, "scipy": scipy.__version__, "pandas": pd.__version__}
    }
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    (output / "ozet.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    ranked.to_csv(output / "siralar.csv", index=False)
    pd.DataFrame(sensitivity).to_csv(output / "duyarlilik.csv", index=False)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.6), constrained_layout=True)
    for axis, first_column, final_column in zip(axes, ["G1", "sira_G1"], ["G3", "sira_G3"]):
        grouped = ranked.groupby([first_column, final_column]).size().reset_index(name="adet")
        axis.scatter(grouped[first_column], grouped[final_column], s=18 * grouped.adet,
                     color="#781e2d", alpha=0.75)
        first_point = ranked.iloc[0]
        axis.scatter([first_point[first_column]], [first_point[final_column]],
                     facecolors="none", edgecolors="#3c3c41", s=90, linewidths=1.2)
        axis.annotate("Satır 1", (first_point[first_column], first_point[final_column]),
                      xytext=(6, 7), textcoords="offset points", fontsize=8)
        axis.spines[["top", "right"]].set_visible(False)
    axes[0].set(xlabel="Birinci dönem notu (G1)", ylabel="Yıl sonu notu (G3)",
                title=f"(a) Pearson r = {complete['pearson_r']:.3f}", xlim=(-1, 20), ylim=(0, 20))
    axes[1].set(xlabel="G1 ortalama sırası", ylabel="G3 ortalama sırası",
                title=f"(b) Spearman rs = {complete['spearman_r']:.3f}", xlim=(-2, 63), ylim=(-2, 63))
    figures = directory / "grafikler"
    figures.mkdir(exist_ok=True)
    destination = figures / "b06-uci-korelasyon.pdf"
    figure.savefig(destination, metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source_path.read_bytes() == original_bytes
    print(json.dumps(results, indent=2))
    print("Doğrulama başarılı: Pearson, bağlı sıralar, duyarlılık, permütasyon ve aynı kayıtlarda OLS özdeşliği.")


if __name__ == "__main__":
    main()