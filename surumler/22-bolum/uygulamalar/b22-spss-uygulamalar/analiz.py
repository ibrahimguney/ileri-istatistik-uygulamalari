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

HASHES = {
    "sleep.csv": "adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e",
    "ToothGrowth.csv": "654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3",
}


def validate_sleep(frame):
    if list(frame.columns) != ["kaynak_satir", "extra", "group", "ID"]:
        raise ValueError("Uyku sütunları beklenen sırada değil.")
    if frame.isna().any().any() or not all(pd.api.types.is_numeric_dtype(frame[name]) for name in frame):
        raise ValueError("Eksik veya sayısal olmayan uyku kaydı.")
    if not np.isfinite(frame.to_numpy()).all():
        raise ValueError("Sonlu olmayan değer.")
    if len(frame) != 20 or set(frame.kaynak_satir) != set(range(1, 21)):
        raise ValueError("Kaynak sırası/sayısı uyuşmuyor.")
    if frame.duplicated(["ID", "group"]).any():
        raise ValueError("Yinelenen kişi-koşul anahtarı.")
    expected = {(person, condition) for person in range(1, 11) for condition in [1, 2]}
    if set(zip(frame.ID, frame.group)) != expected:
        raise ValueError("Eksik veya yanlış kişi-koşul eşlemesi.")


def pair_sleep(frame):
    validate_sleep(frame)
    wide = frame.pivot(index="ID", columns="group", values="extra").sort_index()
    wide.columns = ["kosul1", "kosul2"]
    wide = wide.reset_index()
    wide["fark"] = wide.kosul2 - wide.kosul1
    return wide


def one_sample(values):
    values = np.asarray(values, dtype=float)
    count = len(values)
    mean = float(np.mean(values))
    deviation = float(np.std(values, ddof=1))
    error = deviation / np.sqrt(count)
    statistic = mean / error
    probability = 2 * stats.t.sf(abs(statistic), count - 1)
    interval = mean + np.array([-1, 1]) * stats.t.ppf(.975, count - 1) * error
    direct = stats.ttest_1samp(values, 0)
    np.testing.assert_allclose([statistic, probability], [direct.statistic, direct.pvalue])
    np.testing.assert_allclose(interval, direct.confidence_interval())
    return {"n": count, "mean": mean, "sd": deviation, "se": float(error), "t": float(statistic),
            "df": count - 1, "p_two": float(probability), "ci95": interval.tolist(),
            "dz": mean / deviation}


def independent(first, second, equal_variance):
    first, second = np.asarray(first), np.asarray(second)
    counts = np.array([len(first), len(second)])
    variances = np.array([first.var(ddof=1), second.var(ddof=1)])
    difference = float(first.mean() - second.mean())
    pooled = np.sum((counts - 1) * variances) / (counts.sum() - 2)
    if equal_variance:
        error = np.sqrt(pooled * np.sum(1 / counts))
        degrees = float(counts.sum() - 2)
    else:
        components = variances / counts
        error = np.sqrt(components.sum())
        degrees = components.sum() ** 2 / np.sum(components ** 2 / (counts - 1))
    statistic = difference / error
    probability = 2 * stats.t.sf(abs(statistic), degrees)
    interval = difference + np.array([-1, 1]) * stats.t.ppf(.975, degrees) * error
    direct = stats.ttest_ind(first, second, equal_var=equal_variance)
    np.testing.assert_allclose([statistic, degrees, probability], [direct.statistic, direct.df, direct.pvalue])
    np.testing.assert_allclose(interval, direct.confidence_interval())
    return {"difference": difference, "se": float(error), "t": float(statistic), "df": float(degrees),
            "p_two": float(probability), "ci95": interval.tolist(), "d_pooled": float(difference / np.sqrt(pooled))}


def main():
    directory = Path(__file__).resolve().parent
    root = directory.parent.parent
    source = root / "uygulamalar/b06-parametrik-testler/kaynak"
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    originals = {name: (source / name).read_bytes() for name in HASHES}
    for name, original in originals.items():
        normalized = original.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
        if hashlib.sha256(normalized).hexdigest() != HASHES[name]:
            raise ValueError(f"Kaynak hash'i değişmiş: {name}")
    sleep = pd.read_csv(source / "sleep.csv")
    wide = pair_sleep(sleep)
    pd.testing.assert_frame_equal(wide, pair_sleep(sleep.sample(frac=1, random_state=20260906)))
    malformed = []
    duplicate = sleep.copy()
    duplicate.loc[1, ["ID", "group"]] = duplicate.loc[0, ["ID", "group"]]
    malformed.append(duplicate)
    missing = sleep.copy()
    missing.loc[0, "extra"] = np.nan
    malformed.append(missing)
    malformed.append(sleep.iloc[:-1].copy())
    wrong = sleep.copy()
    wrong.loc[0, "group"] = 3
    malformed.append(wrong)
    for frame in malformed:
        try:
            pair_sleep(frame)
        except ValueError:
            pass
        else:
            raise AssertionError("Hatalı kontrol kopyası reddedilmedi.")
    wide.to_csv(directory / "uyku_esli.csv", index=False, float_format="%.10g")
    teeth = pd.read_csv(source / "ToothGrowth.csv")
    assert list(teeth.columns) == ["kaynak_satir", "len", "supp", "dose"]
    assert not teeth.isna().any().any() and len(teeth) == 60
    assert set(teeth.kaynak_satir) == set(range(1, 61))
    assert set(teeth.supp) == {"OJ", "VC"} and set(teeth.dose) == {.5, 1., 2.}
    assert np.isfinite(teeth[["len", "dose"]]).all().all() and (teeth.len > 0).all()
    assert (teeth.groupby(["supp", "dose"]).size() == 10).all()
    numeric = teeth.copy()
    numeric["supp"] = numeric.supp.map({"OJ": 1, "VC": 2})
    numeric.to_csv(directory / "dis_veri.csv", index=False, float_format="%.10g")
    paired = one_sample(wide.fark)
    direct = stats.ttest_rel(wide.kosul2, wide.kosul1)
    np.testing.assert_allclose([paired["t"], paired["p_two"]], [direct.statistic, direct.pvalue])
    np.testing.assert_allclose(wide.fark.var(ddof=1), wide.kosul1.var(ddof=1) + wide.kosul2.var(ddof=1) - 2 * wide.kosul1.cov(wide.kosul2))
    reverse = one_sample(-wide.fark)
    np.testing.assert_allclose(reverse["ci95"], -np.array(paired["ci95"])[::-1])
    np.testing.assert_allclose(reverse["p_two"], paired["p_two"])
    selected = teeth.loc[teeth.dose == 1]
    first = selected.loc[selected.supp == "OJ", "len"]
    second = selected.loc[selected.supp == "VC", "len"]
    welch = independent(first, second, False)
    student = independent(first, second, True)
    levene = stats.levene(first, second, center="mean")
    absolute = pd.DataFrame({"deviation": np.r_[abs(first-first.mean()), abs(second-second.mean())],
                             "group": [1]*len(first)+[2]*len(second)})
    independent_deviation = independent(absolute.loc[absolute.group == 1, "deviation"],
                                       absolute.loc[absolute.group == 2, "deviation"], True)
    np.testing.assert_allclose(levene.statistic, independent_deviation["t"] ** 2)
    teaching = wide.copy()
    teaching.loc[teaching.ID == 1, "kosul2"] = np.nan
    teaching.loc[teaching.ID == 2, "kosul1"] = np.nan
    complete = teaching.dropna(subset=["kosul1", "kosul2"])
    missing_result = one_sample(complete.kosul2 - complete.kosul1)
    scenarios = {"ana": paired, "filtre_ID_1_5": one_sample(wide.loc[wide.ID <= 5, "fark"]),
                 "iki_hucre_gizli_kurgu": missing_result,
                 "her_cifti_iki_kez_sayma_karsi_ornek": one_sample(np.repeat(wide.fark.to_numpy(), 2))}
    rows = [{"scenario": name, **{key: result[key] for key in ["n", "mean", "sd", "se", "t", "df", "p_two"]},
             "ci_lower": result["ci95"][0], "ci_upper": result["ci95"][1]} for name, result in scenarios.items()]
    pd.DataFrame(rows).to_csv(output / "durum_karsilastirmasi.csv", index=False)
    descriptive = pd.DataFrame([{ "variable": name, "n": len(wide), "mean": wide[name].mean(), "sd": wide[name].std(ddof=1)}
                                for name in ["kosul1", "kosul2", "fark"]])
    descriptive.to_csv(output / "uyku_betimsel.csv", index=False)
    selected.groupby("supp")["len"].agg(["count", "mean", "std", "var"]).to_csv(output / "doz1_betimsel.csv")
    correlation = stats.pearsonr(wide.kosul1, wide.kosul2)
    summary = {"source_hashes_LF": HASHES, "executed": {"Python": True, "SPSS": False, "R": False},
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__, "matplotlib": matplotlib.__version__},
               "paired": paired, "welch_dose1": welch, "student_dose1_comparison": student,
               "levene_mean_dose1": {"F": float(levene.statistic), "df1": 1, "df2": 18, "p": float(levene.pvalue)},
               "paired_correlation_not_mean_test": {"r": float(correlation.statistic), "p": float(correlation.pvalue)},
               "scenarios": scenarios, "teaching_missing": {"kosul1_valid": 9, "kosul2_valid": 9, "complete_pairs": 8,
                                                             "remaining_ID": complete.ID.tolist()},
               "checks": ["source hashes", "unique complete pairs", "permuted row invariance", "four invalid copies rejected",
                          "manual formulas versus SciPy", "paired versus one-sample", "covariance identity", "reversed direction",
                          "Levene versus squared pooled t on absolute deviations"],
               "remote_cells_compared": False, "main_records_deleted": False,
               "normality_tests_performed": False, "effect_size_intervals_computed": False}
    (output / "ozet.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    plt.rcParams.update({"font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(7.2, 3.4), constrained_layout=True)
    axes[0].scatter(wide.ID, wide.fark, color="#2571b5")
    axes[0].axhline(0, color="gray", linewidth=.8)
    axes[0].axhline(paired["mean"], color="#781e2d", label="Ortalama fark")
    axes[0].set(xlabel="Kaynak kişi kodu", ylabel="Koşul 2 − koşul 1 (saat)", xticks=wide.ID)
    axes[0].legend(frameon=False)
    for position, (label, result) in enumerate([("Eşli: 10 kişi", paired), ("Filtre: ilk 5 kişi", scenarios["filtre_ID_1_5"])]):
        axes[1].errorbar(result["mean"], position, xerr=np.array([[result["mean"]-result["ci95"][0]], [result["ci95"][1]-result["mean"]]]),
                         fmt="o", color=["#2571b5", "#781e2d"][position], capsize=4)
    axes[1].axvline(0, color="gray", linewidth=.8)
    axes[1].set(yticks=[0, 1], yticklabels=["10 kişi", "5 kişi"], xlabel="Ortalama fark ve %95 t aralığı", ylim=(-.6, 1.6))
    figure.savefig(root / "assets_figures/b18-durum-kontrolu.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert all((source / name).read_bytes() == data for name, data in originals.items())
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()