"""Ölçme değişmezliği: bfi yarım B, cinsiyet grupları (erkek 425, kadın 891), iki faktörlü DFA (Bölüm DFA, M2).

Çok gruplu DFA'yı ortalama yapısıyla normal kuramlı ML ile kestirir (lavaan'ın varsayılan çok gruplu
tanımı: grup başına n bölenli S, T = sum_g n_g F_g). Biçimsel (configural), metrik, skaler ve katı
değişmezlik; kısmi skaler değişmezlik; gizil ortalama farkları. R/lavaan karşılaştırması analiz.R'dedir.
"""
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import optimize, stats

SOURCE_HASH = "6b3a399dd3aea61ab94252d81660f2c759bbf17d6084204f66a66b25da43b989"
ITEMS = [f"{prefix}{number}" for prefix in ["A", "C"] for number in range(1, 6)]
PAIRS = [(0, 1), (5, 6), (8, 9)]  # A1-A2, C1-C2, C4-C5 (DFA bölümündeki önceden yazılmış M2)
GROUPS = ["Erkek", "Kadın"]
FACTOR = np.repeat([0, 1], 5)


class Specification:
    """Her grup ve her model matrisi hücresi için ya sabit değer ya da ortak parametre indeksi."""

    def __init__(self):
        self.labels, self.starts, self.cells = [], [], []

    def parameter(self, label, start):
        if label not in self.labels:
            self.labels.append(label)
            self.starts.append(start)
        return self.labels.index(label)

    def add(self, group, matrix, row, column, label, start):
        self.cells.append((group, matrix, row, column, self.parameter(label, start)))


def build(level, free_intercepts=()):
    """level: configural, metric, scalar, strict. Ölçekleme: grup 1'de gizil varyans 1 ve ortalama 0."""
    spec = Specification()
    fixed = []
    for g in range(2):
        tag = lambda name, shared: name if shared else f"{name}.g{g + 1}"
        for i in range(10):
            spec.add(g, "L", i, FACTOR[i], tag(f"lambda.{ITEMS[i]}", level != "configural"), .8)
            shared_nu = level in ("scalar", "strict") and ITEMS[i] not in free_intercepts
            spec.add(g, "nu", i, 0, tag(f"nu.{ITEMS[i]}", shared_nu), 4.0)
            spec.add(g, "Theta", i, i, tag(f"theta.{ITEMS[i]}", level == "strict"), 1.0)
        for first, second in PAIRS:
            spec.add(g, "Theta", first, second, f"theta.{ITEMS[first]}.{ITEMS[second]}.g{g + 1}", .1)
        spec.add(g, "Phi", 0, 1, f"phi.AC.g{g + 1}", .3)
        if g == 0 or level == "configural":
            fixed += [(g, "Phi", 0, 0, 1.0), (g, "Phi", 1, 1, 1.0), (g, "alpha", 0, 0, 0.0), (g, "alpha", 1, 0, 0.0)]
        else:
            spec.add(g, "Phi", 0, 0, "phi.AA.g2", 1.0)
            spec.add(g, "Phi", 1, 1, "phi.CC.g2", 1.0)
            if level in ("scalar", "strict"):
                spec.add(g, "alpha", 0, 0, "alpha.A.g2", 0.0)
                spec.add(g, "alpha", 1, 0, "alpha.C.g2", 0.0)
            else:
                fixed += [(g, "alpha", 0, 0, 0.0), (g, "alpha", 1, 0, 0.0)]
    return spec, fixed


def matrices(values, spec, fixed, g):
    out = {"L": np.zeros((10, 2)), "nu": np.zeros((10, 1)), "Theta": np.zeros((10, 10)),
           "Phi": np.zeros((2, 2)), "alpha": np.zeros((2, 1))}
    for group, matrix, row, column, value in fixed:
        if group == g:
            out[matrix][row, column] = value
    for group, matrix, row, column, index in spec.cells:
        if group == g:
            out[matrix][row, column] = values[index]
    for name in ("Theta", "Phi"):
        m = out[name]
        out[name] = np.triu(m) + np.triu(m, 1).T
    sigma = out["L"] @ out["Phi"] @ out["L"].T + out["Theta"]
    mu = (out["nu"] + out["L"] @ out["alpha"]).ravel()
    return out, sigma, mu


def objective(values, spec, fixed, data):
    total, gradient = 0.0, np.zeros(len(values))
    for g, (n, s, m) in enumerate(data):
        mats, sigma, mu = matrices(values, spec, fixed, g)
        sign, logdet = np.linalg.slogdet(sigma)
        if sign <= 0:
            return 1e10, np.zeros(len(values))
        inverse = np.linalg.inv(sigma)
        d = m - mu
        f = logdet + np.trace(s @ inverse) - np.linalg.slogdet(s)[1] - 10 + d @ inverse @ d
        total += n * f
        w = inverse - inverse @ (s + np.outer(d, d)) @ inverse
        a = inverse @ d
        L, Phi, alpha = mats["L"], mats["Phi"], mats["alpha"].ravel()
        for group, matrix, row, column, index in spec.cells:
            if group != g:
                continue
            if matrix == "L":
                unit = np.zeros((10, 2)); unit[row, column] = 1
                d_sigma = unit @ Phi @ L.T + L @ Phi @ unit.T
                d_mu = unit @ alpha
            elif matrix == "nu":
                d_sigma = np.zeros((10, 10)); d_mu = np.zeros(10); d_mu[row] = 1
            elif matrix == "Theta":
                d_sigma = np.zeros((10, 10)); d_sigma[row, column] = d_sigma[column, row] = 1; d_mu = np.zeros(10)
            elif matrix == "Phi":
                unit = np.zeros((2, 2)); unit[row, column] = unit[column, row] = 1
                d_sigma = L @ unit @ L.T; d_mu = np.zeros(10)
            else:
                unit = np.zeros(2); unit[row] = 1
                d_sigma = np.zeros((10, 10)); d_mu = L @ unit
            gradient[index] += n * (np.sum(w * d_sigma) - 2 * a @ d_mu)
    return total, gradient


def fit(level, data, free_intercepts=(), start=None):
    spec, fixed = build(level, free_intercepts)
    x0 = np.array(spec.starts, float)
    if start is not None:
        for index, label in enumerate(spec.labels):
            if label in start:
                x0[index] = start[label]
    numeric = optimize.approx_fprime(x0, lambda v: objective(v, spec, fixed, data)[0], 1e-6)
    np.testing.assert_allclose(objective(x0, spec, fixed, data)[1], numeric, rtol=1e-3, atol=1e-2)
    result = optimize.minimize(objective, x0, args=(spec, fixed, data), jac=True, method="L-BFGS-B",
                               options={"ftol": 1e-15, "gtol": 1e-8, "maxiter": 20000})
    refine = optimize.minimize(objective, result.x, args=(spec, fixed, data), jac=True, method="BFGS",
                               options={"gtol": 1e-6, "maxiter": 20000})
    best = refine if refine.fun <= result.fun else result
    assert np.max(np.abs(best.jac)) < 1e-3, (level, np.max(np.abs(best.jac)))
    values = best.x
    n_total = sum(n for n, _, _ in data)
    chi2 = float(best.fun)
    moments = 2 * (55 + 10)
    df = moments - len(values)
    estimates = dict(zip(spec.labels, values.tolist()))
    groups = []
    for g, (n, s, m) in enumerate(data):
        mats, sigma, mu = matrices(values, spec, fixed, g)
        groups.append({"loadings": mats["L"][np.arange(10), FACTOR].tolist(), "intercepts": mats["nu"].ravel().tolist(),
                       "theta": np.diag(mats["Theta"]).tolist(), "phi": mats["Phi"].tolist(),
                       "alpha": mats["alpha"].ravel().tolist(), "sigma": sigma, "mu": mu})
    return {"level": level, "free_intercepts": list(free_intercepts), "chi2": chi2, "df": int(df),
            "npar": len(values), "p": float(stats.chi2.sf(chi2, df)), "estimates": estimates,
            "groups": groups, "N": n_total}, spec, fixed, values


def fit_indices(result, baseline_chi2, baseline_df, n_total):
    chi2, df = result["chi2"], result["df"]
    cfi = 1 - max(chi2 - df, 0) / max(chi2 - df, baseline_chi2 - baseline_df, 0)
    tli = (baseline_chi2 / baseline_df - chi2 / df) / (baseline_chi2 / baseline_df - 1)
    rmsea = np.sqrt(max((chi2 - df) / (n_total * df), 0)) * np.sqrt(2)  # lavaan: çok grupta sqrt(G) çarpanı
    return {"CFI": float(cfi), "TLI": float(tli), "RMSEA": float(rmsea)}


def rmsea_interval(chi2, df, n_total, groups=2):
    roots = []
    for target in (.95, .05):
        if stats.ncx2.cdf(chi2, df, 1e-12) < target:
            roots.append(0.0)
            continue
        upper = max(chi2, 1.0)
        while stats.ncx2.cdf(chi2, df, upper) > target:
            upper *= 2
        root = optimize.brentq(lambda nc: stats.ncx2.cdf(chi2, df, nc) - target, 1e-12, upper)
        roots.append(float(np.sqrt(root / (n_total * df)) * np.sqrt(groups)))
    return roots


def main():
    directory = Path(__file__).parent
    source_path = directory.parent / "b18-faktor-analizi/yarim_B.csv"
    raw = source_path.read_bytes()
    assert hashlib.sha256(raw.rstrip(b"\n") + b"\n").hexdigest() == SOURCE_HASH, "Önce AFA betiğini çalıştırın."
    source = pd.read_csv(source_path)
    keyed = source[ITEMS].astype(int).copy()
    for item in ["A1", "C4", "C5"]:
        keyed[item] = 7 - keyed[item]
    keyed.insert(0, "grup", source["gender"].map({1: "Erkek", 2: "Kadın"}))
    assert keyed["grup"].notna().all()
    data, descriptives = [], {}
    for name in GROUPS:
        part = keyed.loc[keyed["grup"] == name, ITEMS].to_numpy(float)
        n = len(part)
        s = np.cov(part, rowvar=False, ddof=0)  # ML: n bölenli
        data.append((n, s, part.mean(axis=0)))
        descriptives[name] = {"n": n, "means": dict(zip(ITEMS, part.mean(axis=0).round(4).tolist())),
                              "sds": dict(zip(ITEMS, part.std(axis=0, ddof=1).round(4).tolist()))}
    n_total = sum(n for n, _, _ in data)
    baseline_chi2 = sum(n * (np.sum(np.log(np.diag(s))) - np.linalg.slogdet(s)[1]) for n, s, _ in data)
    baseline_df = 2 * 45

    results, fits = {}, {}
    previous = None
    for level in ("configural", "metric", "scalar", "strict"):
        result, spec, fixed, values = fit(level, data, start=previous)
        previous = result["estimates"]
        result.update(fit_indices(result, baseline_chi2, baseline_df, n_total))
        result["RMSEA_ci90"] = rmsea_interval(result["chi2"], result["df"], n_total)
        fits[level] = (result, spec, fixed, values)
        results[level] = result
    comparisons = {}
    for smaller, larger in [("configural", "metric"), ("metric", "scalar"), ("scalar", "strict")]:
        a, b = results[smaller], results[larger]
        delta = b["chi2"] - a["chi2"]
        ddf = b["df"] - a["df"]
        comparisons[f"{smaller}->{larger}"] = {"delta_chi2": float(delta), "delta_df": ddf, "p": float(stats.chi2.sf(delta, ddf)),
                                              "delta_CFI": b["CFI"] - a["CFI"], "delta_RMSEA": b["RMSEA"] - a["RMSEA"]}

    # Skaler düzeyde tek tek serbest bırakılan kesişimlerin ki-kare katkısı (ardışık: en büyük düşüşü sağlayan serbest bırakılır)
    scalar_estimates = results["scalar"]["estimates"]
    steps, freed = [], []
    current_chi2 = results["scalar"]["chi2"]
    for _ in range(3):
        trials = {}
        for item in ITEMS:
            if item in freed:
                continue
            trial, *_ = fit("scalar", data, free_intercepts=tuple(freed + [item]), start=scalar_estimates)
            trials[item] = trial["chi2"]
        item = min(trials, key=trials.get)
        drop = current_chi2 - trials[item]
        steps.append({"freed": item, "chi2_drop": float(drop), "p_drop": float(stats.chi2.sf(drop, 1)),
                      "candidates": {k: float(current_chi2 - v) for k, v in sorted(trials.items(), key=lambda kv: kv[1])}})
        if stats.chi2.sf(drop, 1) > .001:
            break
        freed.append(item)
        current_chi2 = trials[item]
    partial, *_ = fit("scalar", data, free_intercepts=tuple(freed), start=scalar_estimates)
    partial.update(fit_indices(partial, baseline_chi2, baseline_df, n_total))
    partial["RMSEA_ci90"] = rmsea_interval(partial["chi2"], partial["df"], n_total)
    delta = partial["chi2"] - results["metric"]["chi2"]
    partial["vs_metric"] = {"delta_chi2": float(delta), "delta_df": partial["df"] - results["metric"]["df"],
                            "p": float(stats.chi2.sf(delta, partial["df"] - results["metric"]["df"])),
                            "delta_CFI": partial["CFI"] - results["metric"]["CFI"],
                            "delta_RMSEA": partial["RMSEA"] - results["metric"]["RMSEA"]}

    # Gizil ortalama farkları (kadın - erkek; erkek grubunun gizil SD'si birimiyle) ve gözlenen ölçek puanları
    latent = {}
    for name, result in [("scalar", results["scalar"]), ("partial_scalar", partial)]:
        e = result["estimates"]
        latent[name] = {"A_mean_diff": e["alpha.A.g2"], "C_mean_diff": e["alpha.C.g2"],
                        "A_var_g2": e["phi.AA.g2"], "C_var_g2": e["phi.CC.g2"],
                        "A_diff_pooled_sd": e["alpha.A.g2"] / np.sqrt((425 + 891 * e["phi.AA.g2"]) / 1316),
                        "C_diff_pooled_sd": e["alpha.C.g2"] / np.sqrt((425 + 891 * e["phi.CC.g2"]) / 1316)}
    observed = {}
    for scale, columns in [("A", ITEMS[:5]), ("C", ITEMS[5:])]:
        score = keyed[columns].mean(axis=1)
        men, women = score[keyed["grup"] == "Erkek"], score[keyed["grup"] == "Kadın"]
        pooled = np.sqrt(((len(men) - 1) * men.var() + (len(women) - 1) * women.var()) / (len(men) + len(women) - 2))
        test = stats.ttest_ind(women, men)
        observed[scale] = {"men": float(men.mean()), "women": float(women.mean()), "d": float((women.mean() - men.mean()) / pooled),
                           "t": float(test.statistic), "p": float(test.pvalue)}
    # Metrik modelde kesişim farkları (kadın - erkek), sıralı: hangi madde farklı işliyor?
    metric = results["metric"]["estimates"]
    intercept_gap = {item: metric[f"nu.{item}.g2"] - metric[f"nu.{item}.g1"] for item in ITEMS}
    implied_latent_gap = {item: intercept_gap[item] / metric[f"lambda.{item}"] for item in ITEMS}

    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    keyed.to_csv(output / "analiz_verisi.csv", index=False)
    clean = lambda r: {k: v for k, v in r.items() if k != "groups"} | {
        "groups": [{k: (np.round(v, 6).tolist() if isinstance(v, np.ndarray) else v) for k, v in g.items() if k not in ("sigma", "mu")} for g in r["groups"]]}
    summary = {"source": "b18-faktor-analizi/yarim_B.csv", "source_normalized_sha256": SOURCE_HASH,
               "estimator": "normal-theory ML with mean structure; S with n divisor per group; T = sum n_g F_g (lavaan default)",
               "identification": "group 1 (Erkek): latent variances 1, latent means 0; configural: same in both groups",
               "descriptives": descriptives, "baseline": {"chi2": float(baseline_chi2), "df": baseline_df},
               "models": {k: clean(v) for k, v in results.items()}, "comparisons": comparisons,
               "partial_search": steps, "partial_scalar": clean(partial), "latent_means": latent,
               "observed_scale_scores": observed, "metric_intercept_gap_women_minus_men": intercept_gap,
               "metric_implied_latent_gap_by_item": implied_latent_gap,
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__}}
    (output / "ozet.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(7.4, 3.4), constrained_layout=True)
    config = results["configural"]["groups"]
    positions = np.arange(10)
    for g, (name, color, offset) in enumerate([("Erkek", "#3c3c41", -.18), ("Kadın", "#781e2d", .18)]):
        axes[0].bar(positions + offset, config[g]["loadings"], width=.36, color=color, label=name)
    axes[0].set(xticks=positions, xticklabels=ITEMS, ylabel="Yük (her grupta gizil varyans 1)", title="Biçimsel model: yükler")
    axes[0].legend(frameon=False, fontsize=8)
    implied = pd.Series({item: intercept_gap[item] / metric[f"lambda.{item}"] for item in ITEMS})
    axes[1].bar(positions, implied.values, color=["#781e2d" if item in freed else "#9a9aa0" for item in ITEMS])
    for scale, columns, key in [("A", slice(-.4, 4.4), "A_mean_diff"), ("C", slice(4.6, 9.4), "C_mean_diff")]:
        axes[1].hlines(latent["scalar"][key], columns.start, columns.stop, color="#3c3c41", linestyle="--", linewidth=1)
    axes[1].axhline(0, color="gray", linewidth=.7)
    axes[1].set(xticks=positions, xticklabels=ITEMS, ylabel="Kesişim farkı / yük",
                title="Maddeye göre ima edilen gizil fark")
    figures = directory.parent.parent / "assets_figures"
    figures.mkdir(exist_ok=True)
    figure.savefig(figures / "od-yuk-kesisim.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    print(json.dumps({"fit": {k: {m: round(v[m], 4) if isinstance(v[m], float) else v[m] for m in ["chi2", "df", "npar", "CFI", "TLI", "RMSEA", "RMSEA_ci90"]} for k, v in results.items()},
                      "comparisons": comparisons, "steps": [{k: s[k] for k in ("freed", "chi2_drop", "p_drop")} for s in steps],
                      "partial": {m: partial[m] for m in ["chi2", "df", "CFI", "TLI", "RMSEA", "vs_metric", "free_intercepts"]},
                      "latent": latent, "observed": observed, "gaps": {k: round(v, 3) for k, v in intercept_gap.items()}},
                     ensure_ascii=False, indent=1, default=float))


if __name__ == "__main__":
    main()
