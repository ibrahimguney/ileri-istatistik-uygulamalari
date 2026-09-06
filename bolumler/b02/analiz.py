import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

SOURCE_HASH = "51dcab9aeaa121123dd28a00156d4dfa398c38eecad69bd5699ae4cea03e5ee9"


def quantile7(values, probability):
    ordered = np.sort(np.asarray(values, dtype=float))
    position = (len(ordered) - 1) * probability
    lower = int(np.floor(position))
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return float((1 - fraction) * ordered[lower] + fraction * ordered[upper])


def describe(values):
    values = np.asarray(values, dtype=float)
    assert len(values) > 1 and np.isfinite(values).all()
    mean = float(values.sum() / len(values))
    squared_sum = float(np.sum((values - mean) ** 2))
    variance = squared_sum / (len(values) - 1)
    quartiles = [quantile7(values, probability) for probability in [.25, .5, .75]]
    np.testing.assert_allclose(quartiles, np.quantile(values, [.25, .5, .75], method="linear"))
    np.testing.assert_allclose([mean, variance], [values.mean(), values.var(ddof=1)])
    interquartile = quartiles[2] - quartiles[0]
    fences = [quartiles[0] - 1.5 * interquartile, quartiles[2] + 1.5 * interquartile]
    inside = values[(values >= fences[0]) & (values <= fences[1])]
    return {"n": len(values), "sum": float(values.sum()), "mean": mean, "median": quartiles[1],
            "modes": pd.Series(values).mode().tolist(), "SS": squared_sum, "sample_variance": variance,
            "sample_sd": float(np.sqrt(variance)), "finite_frame_variance": squared_sum / len(values),
            "min": float(values.min()), "max": float(values.max()), "range": float(np.ptp(values)),
            "Q1": quartiles[0], "Q3": quartiles[2], "IQR": interquartile,
            "MAD_raw": float(np.median(abs(values - quartiles[1]))), "fences": fences,
            "whiskers": [float(inside.min()), float(inside.max())]}


def pair_summary(first, last):
    first = np.asarray(first, dtype=float)
    last = np.asarray(last, dtype=float)
    cross_sum = float(np.sum((first - first.mean()) * (last - last.mean())))
    covariance = cross_sum / (len(first) - 1)
    correlation = covariance / (first.std(ddof=1) * last.std(ddof=1))
    np.testing.assert_allclose(covariance, np.cov(first, last, ddof=1)[0, 1])
    np.testing.assert_allclose(correlation, np.corrcoef(first, last)[0, 1])
    differences = last - first
    np.testing.assert_allclose(differences.var(ddof=1), first.var(ddof=1) + last.var(ddof=1) - 2 * covariance)
    return {"n": len(first), "cross_sum": cross_sum, "sample_covariance": covariance,
            "correlation": float(correlation), "difference": describe(differences),
            "positive": int(sum(differences > 0)), "zero": int(sum(differences == 0)), "negative": int(sum(differences < 0))}


def main():
    directory = Path(__file__).parent
    source = directory / "veri.csv"
    original = source.read_bytes()
    assert hashlib.sha256(original.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n").hexdigest() == SOURCE_HASH
    data = pd.read_csv(source)
    assert list(data.columns) == ["kaynak_satir", "school", "G1", "G3"]
    assert len(data) == 80 and not data.isna().any().any() and data.school.eq("GP").all()
    np.testing.assert_array_equal(data.kaynak_satir, np.arange(1, 81))
    assert data[["G1", "G3"]].ge(0).all().all() and data[["G1", "G3"]].le(20).all().all()
    data["fark_G3_G1"] = data.G3 - data.G1
    data.to_csv(directory / "notlar.csv", index=False)
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    summaries = {name: describe(data[name]) for name in ["G1", "G3", "fark_G3_G1"]}
    pd.DataFrame(summaries).T.to_csv(output / "betimsel_ozet.csv")
    frequency = pd.DataFrame({name: data[name].value_counts().reindex(range(21), fill_value=0)
                              for name in ["G1", "G3"]})
    assert (frequency.sum() == 80).all()
    for name in ["G1", "G3"]:
        np.testing.assert_allclose(np.average(frequency.index, weights=frequency[name]), summaries[name]["mean"])
    frequency.index.name = "puan"
    frequency.to_csv(output / "frekanslar.csv")
    flags = []
    quartile_methods = []
    for name in ["G1", "G3"]:
        values = data[name].to_numpy()
        ordered = np.sort(values)
        hinges = [float(np.median(ordered[:40])), float(np.median(ordered[40:]))]
        for method, quartiles in [("type7", [summaries[name]["Q1"], summaries[name]["Q3"]]), ("halves_n80", hinges)]:
            spread = quartiles[1] - quartiles[0]
            lower, upper = quartiles[0] - 1.5 * spread, quartiles[1] + 1.5 * spread
            marked = data.loc[(values < lower) | (values > upper), ["kaynak_satir", name]]
            quartile_methods.append({"variable": name, "method": method, "Q1": quartiles[0], "Q3": quartiles[1],
                                     "lower_fence": lower, "upper_fence": upper, "flagged_rows": marked.kaynak_satir.tolist()})
            flags.extend({"variable": name, "method": method, "source_row": int(row.kaynak_satir),
                          "value": int(row[name])} for _, row in marked.iterrows())
    pd.DataFrame(flags).to_csv(output / "isaretli_kayitlar.csv", index=False)
    pd.DataFrame(quartile_methods).to_csv(output / "ceyrek_yontemleri.csv", index=False)
    pairs = pair_summary(data.G1, data.G3)
    sensitivity = data.loc[data.kaynak_satir.ne(1)].copy()
    sensitivity.to_csv(output / "duyarlilik_satir1_haric.csv", index=False)
    sensitivity_summaries = {name: describe(sensitivity[name]) for name in ["G1", "G3"]}
    sensitivity_pair = pair_summary(sensitivity.G1, sensitivity.G3)
    first_mean, last_mean = float(data.G3.iloc[:60].mean()), float(data.G3.iloc[60:].mean())
    weighted = (60 * first_mean + 20 * last_mean) / 80
    np.testing.assert_allclose(weighted, data.G3.mean())
    transformed = {"five_times_G3": describe(5 * data.G3), "G3_plus_10": describe(data.G3 + 10)}
    np.testing.assert_allclose(transformed["five_times_G3"]["sample_sd"], 5 * summaries["G3"]["sample_sd"])
    np.testing.assert_allclose(transformed["G3_plus_10"]["sample_sd"], summaries["G3"]["sample_sd"])
    np.testing.assert_allclose(np.corrcoef(5 * data.G1, 5 * data.G3)[0, 1], pairs["correlation"])
    cv_demo = {"original_arithmetic_percent": 100 * data.G3.std() / data.G3.mean(),
               "shifted_arithmetic_percent": 100 * (data.G3 + 10).std() / (data.G3 + 10).mean(),
               "meaningful_relative_ability_claim": False}
    toy = {"easy1": describe([4, 6, 8, 10, 12]), "middle1": describe([10, 12, 14, 14, 20]),
           "middle2": describe([5, 7, 8, 9, 40]), "advanced1": describe([2, 4, 4, 6, 9]),
           "advanced3": pair_summary([1, 2, 3, 4], [2, 4, 5, 9]),
           "skew_example": describe([100, 100, 300, 500, 2000]),
           "same_mean_a": describe([8, 10, 12]), "same_mean_b": describe([0, 10, 20])}
    growth = float(np.exp(np.mean(np.log([1.1, .9]))) - 1)
    np.testing.assert_allclose((1 + growth) ** 2, .99)
    results = {"source_normalized_sha256": SOURCE_HASH, "source_raw_sha256": hashlib.sha256(original).hexdigest(),
               "remote_cells_verified": False, "n": 80, "quantile_method": "NumPy linear / R type 7; boxes explicitly use same quartiles",
               "summaries": summaries, "quartile_methods": quartile_methods, "pairs": pairs,
               "sensitivity": {"excluded_row_only_in_sensitivity": 1, "summaries": sensitivity_summaries, "pairs": sensitivity_pair},
               "subsets": {"first60_G3_mean": first_mean, "last20_G3_mean": last_mean,
                           "weighted_mean": weighted, "unweighted_mean_of_two_means": (first_mean + last_mean) / 2},
               "transformations": transformed, "CV_counterexample": cv_demo,
               "iid_SE_formula_not_a_validity_claim": float(data.G3.std() / np.sqrt(80)),
               "synthetic_examples": toy, "synthetic_growth_per_period": growth,
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "matplotlib": matplotlib.__version__}}
    (output / "ozet.json").write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 3, figsize=(7.2, 3.0), constrained_layout=True)
    boxes = []
    for position, (name, color) in enumerate([("G1", "#55555c"), ("G3", "#781e2d")]):
        counts, _, _ = axes[position].hist(data[name], bins=np.arange(-.5, 21.5, 1), color=color, edgecolor="white")
        np.testing.assert_array_equal(counts, frequency[name])
        axes[position].set(title=name, xlabel="Not (0–20)", ylabel="Kayıt sayısı" if position == 0 else "",
                           xlim=(-.5, 20.5), ylim=(0, 22), xticks=[0, 10, 20], yticks=[0, 5, 10, 15, 20])
        summary = summaries[name]
        lower, upper = summary["fences"]
        boxes.append({"label": name, "med": summary["median"], "q1": summary["Q1"], "q3": summary["Q3"],
                      "whislo": summary["whiskers"][0], "whishi": summary["whiskers"][1],
                      "fliers": data.loc[(data[name] < lower) | (data[name] > upper), name].tolist()})
    axes[2].bxp(boxes, showfliers=True, flierprops={"marker": "o", "markersize": 4})
    axes[2].set(title="Tip 7 kutular", ylabel="Not (0–20)", ylim=(-.5, 20.5), yticks=[0, 5, 10, 15, 20])
    figures = directory / "grafikler"
    figures.mkdir(exist_ok=True)
    figure.savefig(figures / "b02-gercek-betimsel.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source.read_bytes() == original
    print(json.dumps(results, indent=2, ensure_ascii=False))
    print("B02 kontrolleri geçti: iki varyans böleni, çeyrekler, frekanslar, kovaryans, fark varyansı ve dönüşümler.")


if __name__ == "__main__":
    main()