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

SOURCE_BASE = "https://raw.githubusercontent.com/wch/r-source/trunk/src/library/datasets/data/"


def summarize(values):
    return {"n": len(values), "mean": float(np.mean(values)),
            "sd": float(np.std(values, ddof=1))}


def one_sample(values, reference=0):
    values = np.asarray(values, dtype=float)
    estimate = values.mean() - reference
    deviation = values.std(ddof=1)
    error = deviation / np.sqrt(len(values))
    degrees = len(values) - 1
    statistic = estimate / error
    probability = 2 * stats.t.sf(abs(statistic), degrees)
    interval = estimate + np.array([-1, 1]) * stats.t.ppf(.975, degrees) * error
    tested = stats.ttest_1samp(values, popmean=reference)
    np.testing.assert_allclose([statistic, probability], [tested.statistic, tested.pvalue])
    np.testing.assert_allclose(interval, np.asarray(tested.confidence_interval()) - reference)
    result = summarize(values)
    result.update(reference=reference, estimate=float(estimate), se=float(error),
                  df=degrees, t=float(statistic), p=float(probability), ci=interval.tolist(),
                  d=float(estimate / deviation))
    return result


def independent(first, second, pooled=False):
    first, second = np.asarray(first), np.asarray(second)
    first_variance, second_variance = first.var(ddof=1), second.var(ddof=1)
    first_n, second_n = len(first), len(second)
    pooled_variance = ((first_n - 1) * first_variance + (second_n - 1) * second_variance) / (first_n + second_n - 2)
    components = [first_variance / first_n, second_variance / second_n]
    if pooled:
        error = np.sqrt(pooled_variance * (1 / first_n + 1 / second_n))
        degrees = first_n + second_n - 2
    else:
        error = np.sqrt(sum(components))
        degrees = sum(components)**2 / (components[0]**2 / (first_n-1) + components[1]**2 / (second_n-1))
    estimate = first.mean() - second.mean()
    statistic = estimate / error
    probability = 2 * stats.t.sf(abs(statistic), degrees)
    interval = estimate + np.array([-1, 1]) * stats.t.ppf(.975, degrees) * error
    tested = stats.ttest_ind(first, second, equal_var=pooled)
    np.testing.assert_allclose([statistic, probability, degrees], [tested.statistic, tested.pvalue, tested.df])
    np.testing.assert_allclose(interval, tested.confidence_interval())
    return {"first": summarize(first), "second": summarize(second), "estimate": float(estimate),
            "se": float(error), "df": float(degrees), "t": float(statistic),
            "p": float(probability), "ci": interval.tolist(),
            "pooled_sd": float(np.sqrt(pooled_variance)),
            "d_pooled": float(estimate / np.sqrt(pooled_variance))}


def main():
    directory = Path(__file__).resolve().parent
    source_paths = [directory / name for name in ["sleep.csv", "ToothGrowth.csv"]]
    hashes = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in source_paths}
    normalized_hashes = {path.name: hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n").hexdigest()
                         for path in source_paths}
    assert normalized_hashes == {
        "sleep.csv": "adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e",
        "ToothGrowth.csv": "654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3"
    }, "Yerel kaynak kopyası değişmiş; kaynak ve kitap sonuçlarını birlikte denetleyin."
    sleep, teeth = [pd.read_csv(path) for path in source_paths]
    assert sleep.shape == (20, 4) and teeth.shape == (60, 4)
    assert sleep.notna().all().all() and teeth.notna().all().all()
    np.testing.assert_array_equal(sleep.kaynak_satir, np.arange(1, 21))
    np.testing.assert_array_equal(teeth.kaynak_satir, np.arange(1, 61))
    assert not sleep.duplicated(["ID", "group"]).any()
    assert sleep.groupby("ID").group.nunique().eq(2).all()
    assert sleep.ID.nunique() == 10 and set(sleep.group) == {1, 2}
    assert set(teeth.supp) == {"OJ", "VC"} and set(teeth.dose) == {.5, 1, 2}
    assert teeth.groupby(["dose", "supp"]).size().eq(10).all()
    paired = sleep.pivot(index="ID", columns="group", values="extra").sort_index()
    difference = paired[2] - paired[1]
    first = one_sample(paired[1])
    matched = one_sample(difference)
    tested = stats.ttest_rel(paired[2], paired[1])
    np.testing.assert_allclose([matched["t"], matched["p"]], [tested.statistic, tested.pvalue])
    np.testing.assert_allclose(matched["ci"], tested.confidence_interval())
    shuffled = sleep.sample(frac=1, random_state=202610).pivot(index="ID", columns="group", values="extra").sort_index()
    np.testing.assert_array_equal(shuffled, paired)
    wrong = independent(paired[2], paired[1])
    variance_identity = paired[1].var() + paired[2].var() - 2 * paired[1].cov(paired[2])
    np.testing.assert_allclose(difference.var(), variance_identity)
    np.testing.assert_allclose(one_sample(-difference)["ci"], -np.array(matched["ci"])[::-1])
    np.testing.assert_allclose(one_sample(60 * difference)["t"], matched["t"])
    sensitivity = pd.DataFrame([{"omitted_ID": int(identifier), **one_sample(difference.drop(identifier))}
                                for identifier in paired.index])
    dose_results = {}
    for dose in [.5, 1., 2.]:
        chosen = teeth.loc[teeth.dose == dose]
        orange = chosen.loc[chosen.supp == "OJ", "len"]
        vitamin = chosen.loc[chosen.supp == "VC", "len"]
        dose_results[str(dose)] = {"welch": independent(orange, vitamin),
                                  "student": independent(orange, vitamin, pooled=True)}
    primary = teeth.loc[teeth.dose == 1]
    oj = primary.loc[primary.supp == "OJ", "len"]
    vc = primary.loc[primary.supp == "VC", "len"]
    normality = {"sleep_group1": paired[1], "sleep_difference": difference, "tooth_OJ_dose1": oj, "tooth_VC_dose1": vc}
    results = {"source_urls": [SOURCE_BASE + name for name in ["sleep.R", "ToothGrowth.R"]],
               "source_review_date": "2026-09-05", "source_csv_sha256": hashes,
               "source_normalized_sha256": normalized_hashes,
               "remote_automatic_comparison": False,
               "original_article_raw_records_verified": False,
               "one_sample_drug1": first, "paired_drug2_minus1": matched,
               "drug2_summary": summarize(paired[2]), "difference_variance_identity": float(variance_identity),
               "incorrect_independent_sleep": wrong, "tooth_by_dose": dose_results,
               "shapiro": {name: {"W": float(stats.shapiro(values).statistic), "p": float(stats.shapiro(values).pvalue)} for name, values in normality.items()},
               "levene_mean_p": float(stats.levene(oj, vc, center="mean").pvalue),
               "brown_forsythe_median_p": float(stats.levene(oj, vc, center="median").pvalue),
               "leave_one_pair_out": sensitivity.to_dict(orient="records"),
               "versions": {"numpy": np.__version__, "scipy": scipy.__version__, "pandas": pd.__version__}}
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    (output / "ozet.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    paired.rename(columns={1: "ilac1", 2: "ilac2"}).assign(fark=difference).to_csv(output / "uyku_esli.csv")
    teeth.assign(supp_kod=teeth.supp.map({"OJ": 1, "VC": 2})).to_csv(output / "dis_veri.csv", index=False)
    sensitivity.to_csv(output / "cift_duyarlilik.csv", index=False)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.5), constrained_layout=True)
    for identifier, row in paired.iterrows():
        axes[0].plot([1, 2], row.to_numpy(), "o-", color="#781e2d", alpha=.6, linewidth=.8, markersize=3)
    axes[0].set(xticks=[1, 2], xticklabels=["İlaç 1", "İlaç 2"], ylabel="Kontrole göre ek uyku (saat)", title="(a) Aynı 10 kişi")
    stats.probplot(difference, dist="norm", plot=axes[1])
    axes[1].set(title="(b) Farkların Q–Q grafiği", xlabel="Kuramsal normal kantil", ylabel="İlaç 2 − İlaç 1 (saat)")
    destinations = directory / "grafikler"
    destinations.mkdir(exist_ok=True)
    figure.savefig(destinations / "b10-uyku-eslestirme.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.5), constrained_layout=True)
    for position, (label, values) in enumerate([("OJ", oj), ("VC", vc)]):
        offsets = np.linspace(-.08, .08, len(values))
        axes[0].scatter(position + offsets, np.sort(values), color=["#781e2d", "#3c3c41"][position], s=22)
        axes[0].plot([position-.15, position+.15], [values.mean()]*2, color="black", linewidth=2)
    axes[0].set(xticks=[0, 1], xticklabels=["OJ", "VC"], ylabel="Odontoblast uzunluğu (kaynak birimi)", title="(a) 1 mg/gün: ayrı hayvanlar")
    for position, dose in enumerate([1., 2.]):
        result = dose_results[str(dose)]["welch"]
        axes[1].errorbar(result["estimate"], position, xerr=[[result["estimate"]-result["ci"][0]], [result["ci"][1]-result["estimate"]]], fmt="o", color="#781e2d", capsize=4)
    axes[1].axvline(0, color="#3c3c41", linestyle="--", linewidth=1)
    axes[1].set(yticks=[0, 1], yticklabels=["1 mg/gün", "2 mg/gün"], xlabel="OJ − VC: fark ve %95 GA", title="(b) Ayrı Welch karşılaştırmaları")
    for axis in axes:
        axis.spines[["top", "right"]].set_visible(False)
    figure.savefig(destinations / "b10-welch-farklar.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    for path in source_paths:
        assert hashlib.sha256(path.read_bytes()).hexdigest() == hashes[path.name]
    print(json.dumps(results, indent=2))
    print("Doğrulama başarılı: elle/SciPy t, sd, p, GA; ID eşleme, fark varyansı ve ölçek değişimi.")


if __name__ == "__main__":
    main()