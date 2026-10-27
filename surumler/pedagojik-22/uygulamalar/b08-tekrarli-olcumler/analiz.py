"""Tekrarlı ölçümler ve karma desenler: sleepstudy (tek grup, 8 gün) ve Orthodont (cinsiyet x yaş).

Bütün kareler toplamları elle kurulur; küresellik (Mauchly), Greenhouse-Geisser ve Huynh-Feldt
düzeltmeleri, çok değişkenli yaklaşım (Hotelling T^2), doğrusal eğilim karşıtlığı ve karma etkiler
modeli (statsmodels MixedLM, REML) hesaplanır. R/afex ve lme4 ile karşılaştırma analiz.R'dedir.
"""
import hashlib
import json
import warnings
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import statsmodels
import statsmodels.formula.api as smf
from scipy import stats

HASHES = {"sleepstudy.csv": "e4783c6b6ac6dcbfdf0e6731e4f0024166ca7416243873a480a64c40839a0af6",
          "Orthodont.csv": "2eacb310cb54353189058bd1acdfec400009bb9bd28d1afbdb012c90265284a0"}


def read_source(directory, name):
    path = directory / "kaynak" / name
    raw = path.read_bytes()
    assert hashlib.sha256(raw.rstrip(b"\n") + b"\n").hexdigest() == HASHES[name], f"{name} değişmiş"
    return pd.read_csv(path), hashlib.sha256(raw).hexdigest()


def orthonormal_contrasts(levels):
    """Ortogonal polinom karşıtlıkları (sütunlar birim uzunlukta, ortalamaya dik)."""
    x = np.arange(levels, dtype=float)
    basis = np.vander(x - x.mean(), levels, increasing=True)
    q, _ = np.linalg.qr(basis)
    q = q[:, 1:] * np.sign(q[-1, 1:])  # son düzeyde pozitif işaret: doğrusal karşıtlık artan
    np.testing.assert_allclose(q.T @ q, np.eye(levels - 1), atol=1e-12)
    np.testing.assert_allclose(q.sum(axis=0), 0, atol=1e-12)
    return q


def sphericity(error_matrix, error_df):
    """Mauchly W, ki-kare yaklaşımı, GG ve HF (özgün ve Lecoutre düzeltmeli) epsilonları."""
    p = error_matrix.shape[0]
    covariance = error_matrix / error_df
    w = np.linalg.det(covariance) / (np.trace(covariance) / p) ** p
    factor = error_df - (2 * p ** 2 + p + 2) / (6 * p)
    chi2 = -factor * np.log(w)
    df = p * (p + 1) / 2 - 1
    gg = np.trace(covariance) ** 2 / (p * np.trace(covariance @ covariance))
    # R mauchly.test ile aynı ikinci dereceden düzeltme (Anderson 2003, Bölüm 10.7):
    rho = 1 - (2 * p ** 2 + p + 2) / (6 * p * error_df)
    omega = (p + 2) * (p - 1) * (p - 2) * (2 * p ** 3 + 6 * p ** 2 + 3 * p + 2) / (288 * (error_df * p * rho) ** 2)
    first, second = stats.chi2.sf(chi2, df), stats.chi2.sf(chi2, df + 4)
    return {"W": float(w), "chi2": float(chi2), "df": int(df), "p_first_order": float(first),
            "p": float(first + omega * (second - first)),
            "epsilon_GG": float(gg), "epsilon_lower_bound": 1 / p}


def huynh_feldt(gg, p, subjects, groups):
    original = (subjects * p * gg - 2) / (p * (subjects - groups - p * gg))
    lecoutre = ((subjects - groups + 1) * p * gg - 2) / (p * (subjects - groups - p * gg))
    return {"epsilon_HF_original": float(min(original, 1)), "epsilon_HF_lecoutre": float(min(lecoutre, 1))}


def corrected(f_value, df1, df2, epsilon):
    return float(stats.f.sf(f_value, df1 * epsilon, df2 * epsilon))


def one_way_repeated(wide):
    n, k = wide.shape
    grand = wide.mean()
    subject_means, level_means = wide.mean(axis=1), wide.mean(axis=0)
    ss_total = ((wide - grand) ** 2).sum()
    ss_subjects = k * ((subject_means - grand) ** 2).sum()
    ss_time = n * ((level_means - grand) ** 2).sum()
    ss_error = ss_total - ss_subjects - ss_time
    df_time, df_error = k - 1, (k - 1) * (n - 1)
    f_value = (ss_time / df_time) / (ss_error / df_error)
    contrasts = orthonormal_contrasts(k)
    scores = wide @ contrasts
    centered = scores - scores.mean(axis=0)
    error_sscp = centered.T @ centered
    np.testing.assert_allclose(np.trace(error_sscp), ss_error, rtol=1e-10)
    np.testing.assert_allclose(n * (scores.mean(axis=0) ** 2).sum(), ss_time, rtol=1e-10)
    sph = sphericity(error_sscp, n - 1)
    sph.update(huynh_feldt(sph["epsilon_GG"], k - 1, n, 1))
    # Çok değişkenli yaklaşım: k-1 karşıtlık puanının ortalama vektörü sıfır mı? (Hotelling T^2)
    mean_vector = scores.mean(axis=0)
    covariance = error_sscp / (n - 1)
    t2 = n * mean_vector @ np.linalg.solve(covariance, mean_vector)
    p = k - 1
    f_multi = (n - p) / ((n - 1) * p) * t2
    wilks = 1 / (1 + t2 / (n - 1))
    # Doğrusal eğilim: kişi başına doğrusal karşıtlık puanı, tek örneklem t (küresellik gerektirmez).
    linear = scores[:, 0]
    t_linear = linear.mean() / (linear.std(ddof=1) / np.sqrt(n))
    ss_linear = n * linear.mean() ** 2
    return {"n_subjects": n, "levels": k, "grand_mean": float(grand), "level_means": level_means.tolist(),
            "level_sd": wide.std(axis=0, ddof=1).tolist(),
            "SS_total": float(ss_total), "SS_subjects": float(ss_subjects), "SS_time": float(ss_time),
            "SS_error": float(ss_error), "df_time": df_time, "df_error": df_error,
            "MS_time": float(ss_time / df_time), "MS_error": float(ss_error / df_error),
            "F": float(f_value), "p_sphericity_assumed": float(stats.f.sf(f_value, df_time, df_error)),
            "p_GG": corrected(f_value, df_time, df_error, sph["epsilon_GG"]),
            "p_HF": corrected(f_value, df_time, df_error, sph["epsilon_HF_lecoutre"]),
            "p_lower_bound": corrected(f_value, df_time, df_error, 1 / df_time),
            "partial_eta2": float(ss_time / (ss_time + ss_error)),
            "generalized_eta2": float(ss_time / (ss_time + ss_subjects + ss_error)),
            "sphericity": sph, "covariance_of_levels": np.cov(wide, rowvar=False).tolist(),
            "hotelling": {"T2": float(t2), "F": float(f_multi), "df1": p, "df2": n - p,
                          "p": float(stats.f.sf(f_multi, p, n - p)), "wilks_lambda": float(wilks)},
            "linear_trend": {"coefficients": contrasts[:, 0].tolist(), "mean_score": float(linear.mean()),
                             "sd_score": float(linear.std(ddof=1)), "t": float(t_linear), "df": n - 1,
                             "p": float(2 * stats.t.sf(abs(t_linear), n - 1)), "SS_linear": float(ss_linear),
                             "share_of_SS_time": float(ss_linear / ss_time)}}


def mixed_anova(frame, subject, between, within, response):
    wide = frame.pivot(index=subject, columns=within, values=response)
    groups = frame.groupby(subject)[between].first().loc[wide.index]
    y = wide.to_numpy()
    n, k = y.shape
    labels = sorted(groups.unique())
    g = len(labels)
    # Aradaki kısım: kişi ortalamaları üzerinde tek yönlü ANOVA (tek aradaki faktörde Tip I=II=III).
    means = y.mean(axis=1)
    grand_of_subjects = means.mean()
    group_mean = {label: means[groups.to_numpy() == label].mean() for label in labels}
    counts = {label: int((groups == label).sum()) for label in labels}
    ss_between = k * sum(counts[label] * (group_mean[label] - grand_of_subjects) ** 2 for label in labels)
    ss_subjects_error = k * sum(((means[groups.to_numpy() == label] - group_mean[label]) ** 2).sum() for label in labels)
    df_between, df_subjects_error = g - 1, n - g
    f_between = (ss_between / df_between) / (ss_subjects_error / df_subjects_error)
    # İçerideki kısım: karşıtlık puanlarının çok değişkenli doğrusal modeli (Tip III, toplam-sıfır kodlama).
    contrasts = orthonormal_contrasts(k)
    scores = y @ contrasts
    design = np.column_stack([np.ones(n), np.where(groups.to_numpy() == labels[0], 1.0, -1.0)])
    xtx_inverse = np.linalg.inv(design.T @ design)
    coefficients = xtx_inverse @ design.T @ scores
    residual = scores - design @ coefficients
    error_sscp = residual.T @ residual
    hypothesis = {name: np.outer(coefficients[row], coefficients[row]) / xtx_inverse[row, row]
                  for name, row in [("within", 0), ("interaction", 1)]}
    p = k - 1
    df_error = p * (n - g)
    ms_error = np.trace(error_sscp) / df_error
    sph = sphericity(error_sscp, n - g)
    sph.update(huynh_feldt(sph["epsilon_GG"], p, n, g))
    rows = {}
    ss_error_total = np.trace(error_sscp)
    for name, matrix in hypothesis.items():
        ss = np.trace(matrix)
        f_value = (ss / p) / ms_error
        rows[name] = {"SS": float(ss), "df": p, "F": float(f_value),
                      "p": float(stats.f.sf(f_value, p, df_error)),
                      "p_GG": corrected(f_value, p, df_error, sph["epsilon_GG"]),
                      "p_HF": corrected(f_value, p, df_error, sph["epsilon_HF_lecoutre"]),
                      "partial_eta2": float(ss / (ss + ss_error_total)),
                      "generalized_eta2": float(ss / (ss + ss_subjects_error + ss_error_total))}
    rows["between"] = {"SS": float(ss_between), "df": df_between, "F": float(f_between),
                       "p": float(stats.f.sf(f_between, df_between, df_subjects_error)),
                       "partial_eta2": float(ss_between / (ss_between + ss_subjects_error)),
                       "generalized_eta2": float(ss_between / (ss_between + ss_subjects_error + ss_error_total))}
    cell = frame.groupby([between, within])[response].agg(["mean", "std", "count"])
    # Basit etkiler: her yaşta cinsiyet farkı (Welch) ve kişi başına doğrusal büyüme hızı.
    simple = {}
    for level in wide.columns:
        a = wide.loc[groups == labels[0], level]
        b = wide.loc[groups == labels[1], level]
        test = stats.ttest_ind(a, b, equal_var=False)
        simple[str(level)] = {"difference": float(a.mean() - b.mean()), "t": float(test.statistic),
                              "df": float(test.df), "p": float(test.pvalue)}
    ages = np.asarray(wide.columns, dtype=float)
    slopes = np.polyfit(ages, y.T, 1)[0]
    slope_frame = pd.Series(slopes, index=wide.index)
    slope_test = stats.ttest_ind(slope_frame[groups == labels[0]], slope_frame[groups == labels[1]], equal_var=False)
    return {"n_subjects": n, "groups": counts, "levels": wide.columns.tolist(), "labels": labels,
            "rows": rows, "SS_subjects_within_groups": float(ss_subjects_error), "df_subjects_within_groups": df_subjects_error,
            "SS_within_error": float(ss_error_total), "df_within_error": df_error, "MS_within_error": float(ms_error),
            "sphericity": sph, "cells": {f"{a}|{b}": {"mean": float(r["mean"]), "sd": float(r["std"]), "n": int(r["count"])}
                                         for (a, b), r in cell.iterrows()},
            "simple_effects_sex_at_age": simple,
            "growth_slopes": {"mean_by_group": {label: float(slope_frame[groups == label].mean()) for label in labels},
                              "sd_by_group": {label: float(slope_frame[groups == label].std(ddof=1)) for label in labels},
                              "welch_t": float(slope_test.statistic), "df": float(slope_test.df), "p": float(slope_test.pvalue)},
            "per_subject_slopes": slope_frame.round(6).to_dict()}


def mixed_model(frame):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = smf.mixedlm("Reaction ~ DaysB", frame, groups=frame["Subject"], re_formula="~DaysB")
        result = model.fit(reml=True, method=["lbfgs"])
    covariance = np.asarray(result.cov_re)
    fixed = result.fe_params
    errors = result.bse_fe
    random_sd = np.sqrt(np.diag(covariance))
    subject_effects = pd.DataFrame(result.random_effects).T
    subject_effects.columns = ["intercept_dev", "slope_dev"]
    fitted_slopes = fixed["DaysB"] + subject_effects["slope_dev"]
    # Kişi başına ayrı OLS eğimleri (tamamen havuzlanmamış) ile karşılaştırma: büzülme.
    ols = frame.groupby("Subject").apply(lambda d: np.polyfit(d["DaysB"], d["Reaction"], 1)[0], include_groups=False)
    return {"estimator": "REML, statsmodels MixedLM (lbfgs)", "converged": bool(result.converged),
            "intercept": float(fixed["Intercept"]), "intercept_se": float(errors["Intercept"]),
            "slope": float(fixed["DaysB"]), "slope_se": float(errors["DaysB"]),
            "slope_t": float(fixed["DaysB"] / errors["DaysB"]),
            "random_sd_intercept": float(random_sd[0]), "random_sd_slope": float(random_sd[1]),
            "random_correlation": float(covariance[0, 1] / np.prod(random_sd)),
            "residual_sd": float(np.sqrt(result.scale)), "REML_criterion": float(-2 * result.llf),
            "slope_prediction_interval_95": (fixed["DaysB"] + np.array([-1.96, 1.96]) * random_sd[1]).tolist(),
            "subjects_with_negative_predicted_slope": int((fitted_slopes < 0).sum()),
            "ols_slopes": ols.round(6).to_dict(), "blup_slopes": fitted_slopes.round(6).to_dict(),
            "ols_slope_sd": float(ols.std(ddof=1)), "blup_slope_sd": float(fitted_slopes.std(ddof=1))}


def main():
    directory = Path(__file__).parent
    sleep, sleep_hash = read_source(directory, "sleepstudy.csv")
    ortho, ortho_hash = read_source(directory, "Orthodont.csv")
    assert len(sleep) == 180 and sleep.groupby("Subject").size().eq(10).all() and not sleep.isna().any().any()
    assert len(ortho) == 108 and ortho.groupby("Subject").size().eq(4).all() and not ortho.isna().any().any()
    # Belenky vd. (2003): 0-1. günler uyum/eğitim, 2. gün temel ölçüm; yoksunluk 2. günden sonra başlar.
    deprivation = sleep[sleep["Days"] >= 2].copy()
    deprivation["DaysB"] = deprivation["Days"] - 2
    wide = deprivation.pivot(index="Subject", columns="Days", values="Reaction")
    assert wide.shape == (18, 8)
    oneway = one_way_repeated(wide.to_numpy())
    day2, day9 = wide[2], wide[9]
    paired = stats.ttest_rel(day9, day2)
    difference = day9 - day2
    oneway["paired_day9_vs_day2"] = {"mean_difference": float(difference.mean()), "sd": float(difference.std(ddof=1)),
                                     "t": float(paired.statistic), "df": 17, "p": float(paired.pvalue),
                                     "dz": float(difference.mean() / difference.std(ddof=1)),
                                     "r_day2_day9": float(np.corrcoef(day2, day9)[0, 1])}
    # Günler arası korelasyonlar: bitişik günler uzak günlerden daha ilişkili mi? (küreselliğin görünür ihlali)
    correlation = np.corrcoef(wide.to_numpy(), rowvar=False)
    oneway["correlation_adjacent_mean"] = float(np.mean(np.diag(correlation, 1)))
    oneway["correlation_day2_day9"] = float(correlation[0, -1])
    lmm = mixed_model(deprivation)
    ortho["Sex"] = ortho["Sex"].map({"Male": "Erkek", "Female": "Kiz"})
    mixed = mixed_anova(ortho, "Subject", "Sex", "age", "distance")
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    wide.rename(columns=lambda day: f"gun{day}").round(4).to_csv(output / "uyku_genis.csv")
    deprivation[["Subject", "Days", "DaysB", "Reaction"]].to_csv(output / "uyku_uzun.csv", index=False)
    ortho_wide = ortho.pivot(index="Subject", columns="age", values="distance").rename(columns=lambda age: f"yas{age}")
    ortho_wide.insert(0, "cinsiyet", ortho.groupby("Subject")["Sex"].first().loc[ortho_wide.index].map({"Erkek": 1, "Kiz": 2}))
    ortho_wide.to_csv(output / "orthodont_genis.csv")
    summary = {"sources": {"sleepstudy.csv": {"package": "lme4 1.1-35.1", "sha256_raw": sleep_hash,
                                              "analysis_rows": "Days 2-9 (8 ölçüm x 18 kişi)"},
                           "Orthodont.csv": {"package": "nlme 3.1-164", "sha256_raw": ortho_hash}},
               "sleep_oneway": oneway, "sleep_mixed_model": lmm, "orthodont_mixed_anova": mixed,
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__,
                            "statsmodels": statsmodels.__version__}}
    (output / "ozet.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    figures = directory.parent.parent / "assets_figures"
    figures.mkdir(exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(7.4, 3.5), constrained_layout=True, sharey=True)
    for subject, row in wide.iterrows():
        axes[0].plot(wide.columns - 2, row.values, color="#9a9aa0", linewidth=.8, alpha=.8)
    axes[0].plot(wide.columns - 2, wide.mean(), color="#781e2d", linewidth=2.4, marker="o", label="Gün ortalaması")
    axes[0].set(xlabel="Yoksunluk günü (0 = temel)", ylabel="Tepki süresi (ms)", title="18 kişinin profilleri")
    axes[0].legend(loc="upper left", frameon=False)
    ols = pd.Series(lmm["ols_slopes"])
    blup = pd.Series(lmm["blup_slopes"]).loc[ols.index]
    order = ols.sort_values().index
    positions = np.arange(len(order))
    axes[1].remove()
    axis = figure.add_subplot(1, 2, 2)
    axis.scatter(ols.loc[order], positions, color="#3c3c41", s=18, label="Kişiye ayrı OLS")
    axis.scatter(blup.loc[order], positions, color="#781e2d", s=18, marker="D", label="Karma model (BLUP)")
    for position, subject in enumerate(order):
        axis.plot([ols[subject], blup[subject]], [position, position], color="#9a9aa0", linewidth=.8)
    axis.axvline(lmm["slope"], color="#781e2d", linestyle="--", linewidth=1)
    axis.set(yticks=positions, yticklabels=order, xlabel="Günlük eğim (ms/gün)", title="Eğimlerin büzülmesi")
    axis.tick_params(axis="y", labelsize=7)
    axis.legend(loc="upper left", frameon=False, fontsize=8)
    figure.savefig(figures / "tk-uyku-profilleri.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(5.6, 3.4), constrained_layout=True)
    for label, color, offset in [("Erkek", "#3c3c41", -.15), ("Kiz", "#781e2d", .15)]:
        cells = [mixed["cells"][f"{label}|{age}"] for age in mixed["levels"]]
        means = np.array([cell["mean"] for cell in cells])
        errors = np.array([stats.t.ppf(.975, cell["n"] - 1) * cell["sd"] / np.sqrt(cell["n"]) for cell in cells])
        axis.errorbar(np.array(mixed["levels"]) + offset, means, yerr=errors, marker="o", capsize=3,
                      color=color, label=f"{'Kız' if label == 'Kiz' else label} (n = {mixed['groups'][label]})")
    axis.set(xticks=mixed["levels"], xlabel="Yaş (yıl)", ylabel="Uzaklık (mm)",
             title="Hücre ortalamaları ve %95 GA (hücre içi t)")
    axis.legend(frameon=False)
    figure.savefig(figures / "tk-orthodont-profil.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    brief = {"oneway": {key: oneway[key] for key in ["F", "p_GG", "partial_eta2", "generalized_eta2"]},
             "sphericity": oneway["sphericity"], "hotelling": oneway["hotelling"], "linear": oneway["linear_trend"]["t"],
             "lmm": {key: lmm[key] for key in ["slope", "slope_se", "random_sd_slope", "random_correlation", "residual_sd"]},
             "mixed": {name: {k: round(v, 5) for k, v in row.items() if isinstance(v, float)} for name, row in mixed["rows"].items()},
             "mixed_sphericity": mixed["sphericity"]}
    print(json.dumps(brief, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
