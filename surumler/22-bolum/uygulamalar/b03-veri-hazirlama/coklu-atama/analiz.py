"""Sürekli yanıtta MAR: uygun Bayesçi regresyon ataması ve Rubin birleştirmesi.

Gerçek bfi arşivini okumaz/değiştirmez. Tek eksik değişken Y'dir; X tam gözlenir.
Bu örnek genel amaçlı MICE/FIML veya ordinal madde atama yazılımı değildir.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import scipy
from scipy import stats

DATA_SEED = 20261025
MASK_SEED = 20261026
IMPUTE_SEED = 20261027
N = 240
PRIMARY_M = 200
CHECK_M = 1000
DELTAS = (-6.0, 0.0, 6.0)


def pool_estimates(estimates, within_variances, complete_df):
    """Rubin T ve Barnard–Rubin küçük örneklem sd; tek skaler parametre."""
    q = np.asarray(estimates, dtype=float)
    u = np.asarray(within_variances, dtype=float)
    if q.ndim != 1 or q.shape != u.shape or len(q) < 2:
        raise ValueError("En az iki, eşleşen tek boyutlu tahmin/varyans dizisi gerekir.")
    if not np.isfinite(q).all() or not np.isfinite(u).all() or np.any(u <= 0) or complete_df <= 0:
        raise ValueError("Başarısız veya geçersiz atamalar sessizce elenemez.")
    m = len(q)
    qbar, ubar, between = float(q.mean()), float(u.mean()), float(q.var(ddof=1))
    extra = (1 + 1 / m) * between
    total = ubar + extra
    lam = extra / total
    if between <= np.finfo(float).eps * max(1.0, ubar):
        df = float(complete_df)
    else:
        old_df = (m - 1) / lam ** 2
        observed_df = ((complete_df + 1) / (complete_df + 3)) * complete_df * (1 - lam)
        df = float(1 / (1 / old_df + 1 / observed_df))
    se = float(np.sqrt(total))
    critical = float(stats.t.ppf(.975, df))
    return {"m": m, "estimate": qbar, "within": ubar, "between": between,
            "total": total, "se": se, "lambda": lam, "df": df,
            "ci_lower": qbar - critical * se, "ci_upper": qbar + critical * se,
            "mcse_estimate": float(np.sqrt(between / m))}


def complete_mean(values):
    values = np.asarray(values, dtype=float)
    if len(values) < 3 or not np.isfinite(values).all():
        raise ValueError("Ortalama için sonlu ve yeterli gözlem gerekir.")
    n = len(values)
    estimate = float(values.mean())
    se = float(stats.sem(values))
    critical = float(stats.t.ppf(.975, n - 1))
    return {"n_used": n, "estimate": estimate, "se": se,
            "ci_lower": estimate - critical * se, "ci_upper": estimate + critical * se}


def impute_regression(observed_frame, m=CHECK_M, seed=IMPUTE_SEED):
    """p(beta,sigma²) ∝ 1/sigma² ile bağımsız posterior öngörü çekilişleri.

    İmpute ediciye gizlenmiş gerçek Y verilmez; girdi yalnız gözlenen dosyadır.
    """
    x = observed_frame["x"].to_numpy(dtype=float)
    y = observed_frame["y"].to_numpy(dtype=float)
    if not np.isfinite(x).all() or np.isinf(y).any() or m < 2:
        raise ValueError("X tam gözlenmeli; Y sonlu veya eksik olmalı.")
    seen = np.isfinite(y)
    if seen.all() or not (~seen).any():
        raise ValueError("Bu örnek eksik Y içeren dosya içindir.")
    design = np.column_stack([np.ones(len(x)), x])
    xo, yo = design[seen], y[seen]
    nu = len(yo) - design.shape[1]
    if nu <= 2 or np.linalg.matrix_rank(xo) != 2:
        raise ValueError("Yeterli gözlenen kayıt ve tam ranklı regresyon gerekir.")
    beta, _, _, _ = np.linalg.lstsq(xo, yo, rcond=None)
    residuals = yo - xo @ beta
    rss = float(residuals @ residuals)
    if not np.isfinite(rss) or rss <= 0:
        raise ValueError("Pozitif sonlu artık kareler toplamı gerekir.")
    inverse = np.linalg.solve(xo.T @ xo, np.eye(2))
    # Bağımsız OLS hesabı: aynı katsayıları SciPy'nin regresyonuyla karşılaştır.
    reference = stats.linregress(x[seen], y[seen])
    np.testing.assert_allclose(beta, [reference.intercept, reference.slope], rtol=1e-11)
    rng = np.random.default_rng(seed)
    completed = np.repeat(y[None, :], m, axis=0)
    records = []
    for j in range(m):
        sigma2 = rss / rng.chisquare(nu)
        draw_beta = rng.multivariate_normal(beta, sigma2 * inverse)
        completed[j, ~seen] = rng.normal(design[~seen] @ draw_beta, np.sqrt(sigma2))
        records.append({"imputation": j + 1, "beta0": float(draw_beta[0]),
                        "beta1": float(draw_beta[1]), "sigma2": float(sigma2)})
    np.testing.assert_array_equal(completed[:, seen], np.broadcast_to(y[seen], (m, seen.sum())))
    assert np.isfinite(completed).all()
    diagnostics = {"n_observed": int(seen.sum()), "residual_df": nu,
                   "ols_intercept": float(beta[0]), "ols_slope": float(beta[1]),
                   "rss": rss, "posterior_sigma2_mean": rss / (nu - 2)}
    return completed, records, diagnostics


def generate_example():
    rng = np.random.default_rng(DATA_SEED)
    x = rng.normal(size=N)
    full_y = 50 + 8 * x + rng.normal(scale=6, size=N)
    probability = 1 / (1 + np.exp(-(-.4 + .9 * x)))
    missing = np.random.default_rng(MASK_SEED).uniform(size=N) < probability
    observed_y = full_y.copy()
    observed_y[missing] = np.nan
    observed = pd.DataFrame({"id": np.arange(1, N + 1), "x": x, "y": observed_y})
    full = pd.DataFrame({"id": observed.id, "x": x, "y_full": full_y,
                         "p_missing": probability, "missing_y": missing.astype(int)})
    return observed, full


def run(output):
    output.mkdir(parents=True, exist_ok=True)
    observed, full = generate_example()
    observed_path, full_path = output / "veri_gozlenen.csv", output / "veri_tam_simulasyon.csv"
    observed.to_csv(observed_path, index=False)
    full.to_csv(full_path, index=False)
    original_bytes = observed_path.read_bytes()
    # Atama, gerçekten yalnız gözlenen veri dosyasından başlar.
    observed = pd.read_csv(observed_path)
    completed, draws, diagnostics = impute_regression(observed)
    missing = observed.y.isna().to_numpy()
    q, u = completed.mean(axis=1), completed.var(axis=1, ddof=1) / N
    primary = pool_estimates(q[:PRIMARY_M], u[:PRIMARY_M], N - 1)
    check = pool_estimates(q, u, N - 1)
    naive = observed.y.fillna(observed.y.mean()).to_numpy()
    methods = []
    for label, values in [("simulasyon_tam_veri_karsilastirma", full.y_full),
                          ("yalniz_gozlenen_y", observed.y.dropna()),
                          ("ortalama_tek_atama_naif", naive)]:
        methods.append({"method": label, **complete_mean(values)})
    methods.append({"method": "coklu_atama_m200", "n_used": N,
                    **{k: primary[k] for k in ["estimate", "se", "ci_lower", "ci_upper"]}})
    pd.DataFrame(methods).to_csv(output / "yontemler.csv", index=False)
    sensitivity = []
    for delta in DELTAS:
        shifted = completed[:PRIMARY_M].copy()
        shifted[:, missing] += delta
        shifted_q, shifted_u = shifted.mean(axis=1), shifted.var(axis=1, ddof=1) / N
        result = pool_estimates(shifted_q, shifted_u, N - 1)
        # Sabit delta yalnız eksik gruba uygulanır: ortalama kayması tam delta*k/n.
        np.testing.assert_allclose(result["estimate"] - primary["estimate"],
                                   delta * missing.mean(), atol=1e-12)
        np.testing.assert_array_equal(shifted[:, ~missing], completed[:PRIMARY_M, ~missing])
        sensitivity.append({"delta": delta, **result})
    pd.DataFrame(sensitivity).to_csv(output / "delta_duyarlilik.csv", index=False)
    pd.DataFrame(draws).assign(mean_y=q, variance_mean=u).to_csv(output / "cekimler.csv", index=False)
    pd.DataFrame([{"alan": "id", "anlam": "Simülasyon sırası; gerçek kişi kimliği değil"},
                  {"alan": "x", "anlam": "Tam gözlenen sürekli yardımcı değişken, N(0,1)"},
                  {"alan": "y", "anlam": "Gözlenen sürekli yanıt; boş hücre eksik"},
                  {"alan": "y_full", "anlam": "Yalnız öğretim karşılaştırması; atamaya girdi olmaz"},
                  {"alan": "p_missing", "anlam": "Bilinen üretim olasılığı; atamada kullanılmaz"}]).to_csv(output / "veri_sozlugu.csv", index=False)
    assert observed_path.read_bytes() == original_bytes
    summary = {"data_kind": "continuous_simulation_not_bfi", "n": N,
               "n_missing": int(missing.sum()), "missing_fraction": float(missing.mean()),
               "estimand": "Üretim anakütlesindeki Y ortalaması; bilinen değer 50",
               "seeds": {"data": DATA_SEED, "mask": MASK_SEED, "imputation": IMPUTE_SEED},
               "missingness": "MAR by design: logit P(Y missing | X)=-0.4+0.9X",
               "imputation_model": "Y|X: normal homoskedastic linear regression; prior p(beta,sigma2) proportional to 1/sigma2",
               "primary": primary, "m1000_check": check, "methods": methods,
               "delta_sensitivity": sensitivity, "regression": diagnostics,
               "observed_csv_sha256": hashlib.sha256(original_bytes).hexdigest(),
               "limitations": ["Tek simülasyon bir kapsama/yanlılık araştırması değildir.",
                               "Delta veriden tahmin edilmez; verilen deltalar için belirsizlik koşulludur.",
                               "Ordinal maddeye normal regresyon ataması uygulanmadı.",
                               "FIML/MICE ve R/SPSS doğrulaması yapılmadı."],
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__}}
    (output / "ozet.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: summary[k] for k in ["n", "n_missing", "primary", "m1000_check", "methods"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "sonuclar")
    run(parser.parse_args().output)
