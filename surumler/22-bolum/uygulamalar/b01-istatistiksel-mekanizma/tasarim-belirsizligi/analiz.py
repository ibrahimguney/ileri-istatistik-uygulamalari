"""Kapalı 80 kayıt üzerinde tasarım dağılımları; dış anakütle çıkarımı değildir."""
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 20261025
REPETITIONS = 20000
SOURCE_HASH = "51dcab9aeaa121123dd28a00156d4dfa398c38eecad69bd5699ae4cea03e5ee9"


def exact_srs_variance(values, sample_size):
    values = np.asarray(values, dtype=float)
    population_size = len(values)
    if not 1 <= sample_size <= population_size:
        raise ValueError("Örneklem büyüklüğü 1 ile N arasında olmalı")
    return float((1 - sample_size / population_size) * values.var(ddof=1) / sample_size)


def systematic_means(values, interval):
    values = np.asarray(values, dtype=float)
    if len(values) % interval:
        raise ValueError("Bu öğretim örneğinde N aralığa tam bölünmeli")
    return np.array([values[start::interval].mean() for start in range(interval)])


def main():
    root = Path(__file__).resolve().parents[2]
    source = root / "b12-regresyon/kaynak/uci-portekizce-ilk80-notlar.csv"
    original = source.read_bytes()
    assert hashlib.sha256(original.rstrip(b"\n") + b"\n").hexdigest() == SOURCE_HASH
    data = pd.read_csv(source)
    y = data.G3.to_numpy(dtype=float)
    assert len(y) == 80 and not np.isnan(y).any()
    n = 10
    mu = float(y.mean())
    exact_var = exact_srs_variance(y, n)
    starts = systematic_means(y, 8)
    np.testing.assert_allclose(starts.mean(), mu, atol=1e-12)
    rng = np.random.default_rng(SEED)
    means = np.array([y[rng.choice(len(y), n, replace=False)].mean() for _ in range(REPETITIONS)])
    # Monte Carlo örnekleri bağımsızdır; anakütle verisi yeniden üretilmez.
    mc_mean_se = np.sqrt(exact_var / REPETITIONS)
    assert abs(means.mean() - mu) < 5 * mc_mean_se
    assert abs(means.var(ddof=1) / exact_var - 1) < .05
    periodic = np.tile([1., 0., 0., 0., 0., 0., 0., 0.], 10)
    periodic_starts = systematic_means(periodic, 8)
    periodic_srs = exact_srs_variance(periodic, n)
    # Tam sayım ve sayım varyansı: deterministik matematik kontrolleri.
    assert exact_srs_variance(y, len(y)) == 0
    assert periodic_starts.mean() == periodic.mean() == .125
    np.testing.assert_allclose(periodic_starts.var(ddof=0) / periodic_srs, 79 / 7)
    result = {
        "scope": "Yalnız kapalı 80 kayıt; dış anakütleye güven aralığı değildir",
        "source_normalized_sha256": SOURCE_HASH,
        "N": len(y), "n": n, "mu": mu,
        "finite_population_variance_S2": float(y.var(ddof=1)),
        "srs_exact_variance": exact_var, "srs_exact_se": float(np.sqrt(exact_var)),
        "fpc_for_se": float(np.sqrt(1 - n / len(y))),
        "systematic_exact_variance": float(starts.var(ddof=0)),
        "systematic_exact_se": float(starts.std(ddof=0)),
        "systematic_means": starts.tolist(),
        "simulation": {"seed": SEED, "repetitions": REPETITIONS,
                       "mean": float(means.mean()), "variance": float(means.var(ddof=1)),
                       "mc_se_of_mean": float(mc_mean_se)},
        "periodic_synthetic": {"mu": float(periodic.mean()),
                               "systematic_variance": float(periodic_starts.var(ddof=0)),
                               "srs_variance": periodic_srs,
                               "variance_ratio_systematic_to_srs": float(periodic_starts.var(ddof=0) / periodic_srs)},
        "versions": {"numpy": np.__version__, "pandas": pd.__version__},
    }
    output = Path(__file__).parent / "sonuclar"
    output.mkdir(exist_ok=True)
    (output / "ozet.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    pd.DataFrame({"tekrar": np.arange(1, REPETITIONS + 1), "ortalama": means}).to_csv(output / "srs_tekrarlari.csv", index=False)
    assert source.read_bytes() == original
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
