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

SOURCE_HASH = "8726fd25dbfc685be2d3d726e5511bbb31ba9c7b367b6864eb06e0d8669e6557"
RESAMPLES = 20000
KEYS = {"A": ["A1"], "C": ["C4", "C5"]}


def alpha(values):
    values = np.asarray(values, dtype=float)
    if values.ndim != 2 or values.shape[1] < 2 or not np.isfinite(values).all():
        raise ValueError("En az iki madde ve eksiksiz sayısal matris gerekli.")
    count = values.shape[1]
    covariance = np.cov(values, rowvar=False, ddof=1)
    total_variance = values.sum(axis=1).var(ddof=1)
    if total_variance <= 0:
        raise ValueError("Toplam puan varyansı pozitif olmalı.")
    estimate = count/(count-1)*(1-np.trace(covariance)/total_variance)
    np.testing.assert_allclose(covariance.sum(), total_variance)
    mean_variance = np.trace(covariance)/count
    mean_covariance = (covariance.sum()-np.trace(covariance))/(count*(count-1))
    alternative = count*mean_covariance/(mean_variance+(count-1)*mean_covariance)
    np.testing.assert_allclose(estimate, alternative)
    return float(estimate)


def diagnostics(frame):
    values = frame.to_numpy(dtype=float)
    covariance = np.cov(values, rowvar=False)
    correlation = np.corrcoef(values, rowvar=False)
    count = values.shape[1]
    mean_r = (correlation.sum()-count)/(count*(count-1))
    standardized = count*mean_r/(1+(count-1)*mean_r)
    normalized = (values-values.mean(axis=0))/values.std(axis=0, ddof=1)
    np.testing.assert_allclose(standardized, alpha(normalized))
    items = []
    for position, item in enumerate(frame.columns):
        rest = np.delete(values, position, axis=1)
        item_rest = stats.pearsonr(values[:, position], rest.sum(axis=1)).statistic
        covariance_rest = covariance[position].sum()-covariance[position, position]
        variance_rest = np.delete(np.delete(covariance, position, axis=0), position, axis=1).sum()
        manual_rest = covariance_rest/np.sqrt(covariance[position, position]*variance_rest)
        np.testing.assert_allclose(item_rest, manual_rest)
        items.append({"item": item, "mean": float(values[:, position].mean()),
                      "sd": float(values[:, position].std(ddof=1)), "item_rest_r": float(item_rest),
                      "item_total_r_uncorrected": float(stats.pearsonr(values[:, position], values.sum(axis=1)).statistic),
                      "alpha_if_deleted_same_cases": alpha(rest)})
    return {"n": len(frame), "k": count, "alpha_raw": alpha(values), "alpha_standardized": float(standardized),
            "average_r": float(mean_r), "item_variance_sum": float(np.trace(covariance)),
            "total_variance": float(covariance.sum()), "total_mean": float(values.sum(axis=1).mean()),
            "total_sd": float(values.sum(axis=1).std(ddof=1)), "items": items}


def bootstrap_alpha(values, seed):
    rng = np.random.default_rng(seed)
    count = values.shape[1]
    estimates = []
    for start in range(0, RESAMPLES, 1000):
        size = min(1000, RESAMPLES-start)
        indices = rng.integers(0, len(values), size=(size, len(values)))
        samples = values[indices]
        variance_sum = samples.var(axis=1, ddof=1).sum(axis=1)
        total_variance = samples.sum(axis=2).var(axis=1, ddof=1)
        if np.any(total_variance <= 0):
            raise ValueError("Sıfır toplam varyanslı bootstrap örneği; sessizce atlanmadı.")
        batch = count/(count-1)*(1-variance_sum/total_variance)
        if start == 0:
            np.testing.assert_allclose(batch[:5], [alpha(sample) for sample in samples[:5]])
        estimates.extend(batch.tolist())
    estimates = np.asarray(estimates)
    return estimates


def main():
    directory = Path(__file__).resolve().parent
    source_path = directory/"bfi-ilk100-AC.csv"
    source_bytes = source_path.read_bytes()
    assert hashlib.sha256(source_bytes.replace(b"\r\n", b"\n").rstrip(b"\n")+b"\n").hexdigest()==SOURCE_HASH, "Yerel kaynak kopyası değişmiş; kaynak ve kitap sonuçlarını birlikte denetleyin."
    source = pd.read_csv(source_path)
    item_names = [f"{scale}{number}" for scale in ["A", "C"] for number in range(1, 6)]
    assert list(source.columns)==["kaynak_satir", "kaynak_kayit"]+item_names
    np.testing.assert_array_equal(source.kaynak_satir, np.arange(1, 101))
    assert source.kaynak_kayit.is_unique
    observed = source[item_names].stack().to_numpy()
    assert np.isin(observed, np.arange(1, 7)).all()
    assert source[item_names].isna().sum().to_dict()=={item: int(item in ["A2", "C1", "C3"]) for item in item_names}
    results = {"source_sha256": hashlib.sha256(source_bytes).hexdigest(), "source_normalized_sha256": SOURCE_HASH,
               "selection": "Rdatasets psych/bfi, source rows 1-100, A1-A5 and C1-C5 only",
               "source_full_n_documented": 2800, "remote_automatic_comparison": False,
               "psych_package_values_automatically_verified": False,
               "missing_per_item": source[item_names].isna().sum().to_dict(), "scales": {},
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__}}
    output = directory/"sonuclar"
    output.mkdir(exist_ok=True)
    draws = {}
    for scale, seed in [("A", 202613), ("C", 202614)]:
        names = [f"{scale}{number}" for number in range(1, 6)]
        raw = source[names].dropna()
        keyed = raw.copy()
        for item in KEYS[scale]:
            keyed[item] = 7-keyed[item]
            np.testing.assert_array_equal(7-keyed[item], raw[item])
        summary = diagnostics(keyed)
        summary["alpha_without_reversing"] = alpha(raw)
        summary["excluded_source_rows"] = source.loc[~source.index.isin(raw.index), "kaynak_satir"].tolist()
        summary["reversed_items"] = KEYS[scale]
        draws[scale] = bootstrap_alpha(keyed.to_numpy(), seed)
        summary["bootstrap"] = {"method": "participant-row percentile, linear quantiles", "resamples": RESAMPLES,
                                "seed": seed, "ci95": np.quantile(draws[scale], [.025, .975], method="linear").tolist(),
                                "sd": float(draws[scale].std(ddof=1)), "invalid_draws": 0}
        scaled = keyed.copy()
        scaled.iloc[:, 0] *= 10
        summary["first_item_times10_raw_alpha"] = alpha(scaled)
        np.testing.assert_allclose(np.corrcoef(scaled, rowvar=False), np.corrcoef(keyed, rowvar=False))
        summary["duplicated_items_alpha"] = alpha(np.concatenate([keyed.to_numpy(), keyed.to_numpy()], axis=1))
        pd.testing.assert_frame_equal(keyed.sort_index(), keyed.sample(frac=1, random_state=seed).sort_index())
        np.testing.assert_allclose(alpha(keyed.sample(frac=1, random_state=seed)), summary["alpha_raw"])
        results["scales"][scale] = summary
        pd.DataFrame(summary["items"]).to_csv(output/f"madde_{scale}.csv", index=False)
        keyed.cov().to_csv(output/f"kovaryans_{scale}.csv")
        keyed.corr().to_csv(output/f"korelasyon_{scale}.csv")
        source.loc[keyed.index, ["kaynak_satir", "kaynak_kayit"]].join(keyed).to_csv(output/f"puanlanmis_{scale}.csv", index=False)
    joint = source[item_names].dropna().copy()
    for item in ["A1", "C4", "C5"]:
        joint[item] = 7-joint[item]
    results["mixed_ten_items"] = {"n": len(joint), "alpha": alpha(joint),
                                   "interpretation": "Counterexample only; not a validated single total score"}
    (output/"ozet.json").write_text(json.dumps(results, indent=2)+"\n", encoding="utf-8")
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.5), constrained_layout=True)
    items = results["scales"]["A"]["items"]
    positions = np.arange(len(items))
    axes[0].barh(positions, [item["item_rest_r"] for item in items], color="#781e2d")
    axes[0].set(yticks=positions, yticklabels=[item["item"] for item in items], xlabel="Düzeltilmiş madde–kalan r", title="(a) A: ortak 99 kayıt")
    axes[1].scatter([item["alpha_if_deleted_same_cases"] for item in items], positions, color="#781e2d")
    axes[1].axvline(results["scales"]["A"]["alpha_raw"], linestyle="--", color="#3c3c41")
    axes[1].set(yticks=positions, yticklabels=[item["item"] for item in items], xlabel="Madde silinirse ham alfa", title="(b) Kesikli çizgi: beş madde")
    figures = directory/"grafikler"
    figures.mkdir(exist_ok=True)
    figure.savefig(figures/"b13-madde-analizi.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.3), constrained_layout=True)
    for axis, scale in zip(axes, ["A", "C"]):
        axis.hist(draws[scale], bins=35, color="#c49b5c", edgecolor="white")
        bounds = results["scales"][scale]["bootstrap"]["ci95"]
        for value in bounds:
            axis.axvline(value, color="#781e2d", linestyle="--")
        axis.set(xlabel="Ham alfa", ylabel="Yeniden örnekleme sayısı", title=f"{scale}: 20000 satır bootstrap")
    figure.savefig(figures/"b13-bootstrap.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source_path.read_bytes()==source_bytes
    print(json.dumps(results, indent=2))
    print("Doğrulama başarılı: ters kodlama, alfa özdeşlikleri, madde-kalan korelasyonu ve bootstrap.")


if __name__ == "__main__":
    main()