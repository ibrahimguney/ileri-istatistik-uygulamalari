import hashlib
import json
from itertools import combinations
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import stats
import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.oneway import anova_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

DOSES = [.5, 1., 2.]
SOURCE_HASH = "654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3"


def one_way(data):
    groups = [data.loc[data.dose == dose, "len"].to_numpy() for dose in DOSES]
    counts = np.array([len(group) for group in groups])
    means = np.array([group.mean() for group in groups])
    variances = np.array([group.var(ddof=1) for group in groups])
    total_n = counts.sum()
    grand = np.average(means, weights=counts)
    between = float(np.sum(counts * (means - grand)**2))
    within = float(sum(np.sum((group - group.mean())**2) for group in groups))
    total = float(np.sum((data.len - grand)**2))
    np.testing.assert_allclose(between + within, total)
    group_df = len(groups) - 1
    error_df = int(total_n - len(groups))
    mse = within / error_df
    statistic = between / group_df / mse
    probability = stats.f.sf(statistic, group_df, error_df)
    tested = stats.f_oneway(*groups)
    np.testing.assert_allclose([statistic, probability], tested)
    weights = counts / variances
    normalized = weights / weights.sum()
    weighted_mean = np.sum(normalized * means)
    correction = np.sum((1 - normalized)**2 / (counts - 1))
    welch_f = np.sum(weights * (means - weighted_mean)**2) / group_df
    welch_f /= 1 + 2 * (len(groups) - 2) / (len(groups)**2 - 1) * correction
    welch_df = (len(groups)**2 - 1) / (3 * correction)
    welch_p = stats.f.sf(welch_f, group_df, welch_df)
    independent_welch = anova_oneway(groups, use_var="unequal", welch_correction=True)
    np.testing.assert_allclose([welch_f, welch_p, welch_df],
                               [independent_welch.statistic, independent_welch.pvalue, independent_welch.df_denom])
    np.testing.assert_allclose([welch_f, welch_p], stats.f_oneway(*groups, equal_var=False))
    tukey = stats.tukey_hsd(*groups)
    games = stats.tukey_hsd(*groups, equal_var=False)
    tukey_ci, games_ci = tukey.confidence_interval(), games.confidence_interval()
    reference_tukey = pairwise_tukeyhsd(data.len, data.dose)
    pairs = []
    for pair_index, (lower, upper) in enumerate(combinations(range(3), 2)):
        delta = means[upper] - means[lower]
        pooled_scale = np.sqrt(mse / 2 * (1/counts[lower] + 1/counts[upper]))
        tukey_p = stats.studentized_range.sf(abs(delta) / pooled_scale, 3, error_df)
        tukey_bounds = delta + np.array([-1, 1]) * stats.studentized_range.ppf(.95, 3, error_df) * pooled_scale
        components = variances[[lower, upper]] / counts[[lower, upper]]
        pair_df = components.sum()**2 / np.sum(components**2 / (counts[[lower, upper]] - 1))
        games_scale = np.sqrt(components.sum() / 2)
        games_p = stats.studentized_range.sf(abs(delta) / games_scale, 3, pair_df)
        games_bounds = delta + np.array([-1, 1]) * stats.studentized_range.ppf(.95, 3, pair_df) * games_scale
        np.testing.assert_allclose([delta, tukey_p, *tukey_bounds],
                                   [tukey.statistic[upper, lower], tukey.pvalue[upper, lower], tukey_ci.low[upper, lower], tukey_ci.high[upper, lower]])
        np.testing.assert_allclose([games_p, *games_bounds],
                                   [games.pvalue[upper, lower], games_ci.low[upper, lower], games_ci.high[upper, lower]])
        np.testing.assert_allclose(tukey_p, reference_tukey.pvalues[pair_index], rtol=1e-6, atol=1e-12)
        np.testing.assert_allclose(tukey_bounds, reference_tukey.confint[pair_index])
        pairs.append({"comparison": f"{DOSES[upper]:g}-{DOSES[lower]:g}", "difference": float(delta),
                      "tukey_p": float(tukey_p), "tukey_ci": tukey_bounds.tolist(),
                      "games_howell_p": float(games_p), "games_howell_ci": games_bounds.tolist(),
                      "games_howell_df": float(pair_df)})
    return {"n": int(total_n), "grand_mean": float(grand), "SSG": between, "SSW": within, "SST": total,
            "df_between": group_df, "df_within": error_df, "MSE": mse, "F": float(statistic), "p": float(probability),
            "eta_squared": between / total, "omega_squared": (between - group_df*mse) / (total + mse),
            "welch_F": float(welch_f), "welch_df": float(welch_df), "welch_p": float(welch_p),
            "means": means.tolist(), "sd": np.sqrt(variances).tolist(), "pairs": pairs}


def main():
    directory = Path(__file__).resolve().parent
    source = directory / "ToothGrowth.csv"
    source_bytes = source.read_bytes()
    normalized_hash = hashlib.sha256(source_bytes.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n").hexdigest()
    assert normalized_hash == SOURCE_HASH, "Yerel kaynak kopyası değişmiş; kaynak ve kitap sonuçlarını birlikte denetleyin."
    data = pd.read_csv(source)
    assert data.shape == (60, 4) and data.notna().all().all()
    np.testing.assert_array_equal(data.kaynak_satir, np.arange(1, 61))
    assert set(data.supp) == {"OJ", "VC"} and set(data.dose) == set(DOSES)
    assert data.groupby(["supp", "dose"]).size().eq(10).all()
    one_way_results = {supp: one_way(data.loc[data.supp == supp]) for supp in ["OJ", "VC"]}
    data["dose_f"] = pd.Categorical(data.dose, categories=DOSES, ordered=True)
    formula = "len ~ C(supp, Sum) * C(dose_f, Sum)"
    model = smf.ols(formula, data=data).fit()
    table = sm.stats.anova_lm(model, typ=2)
    third = sm.stats.anova_lm(model, typ=3)
    cells = data.groupby(["supp", "dose"], observed=True).len.agg(["size", "mean", "std"])
    grand = data.len.mean()
    supp_means = data.groupby("supp").len.mean()
    dose_means = data.groupby("dose").len.mean()
    ss_supp = float(30 * np.sum((supp_means - grand)**2))
    ss_dose = float(20 * np.sum((dose_means - grand)**2))
    ss_interaction = float(sum(10 * (row["mean"] - supp_means[supp] - dose_means[dose] + grand)**2
                               for (supp, dose), row in cells.iterrows()))
    error = float(sum(np.sum((group.len-group.len.mean())**2) for _, group in data.groupby(["supp", "dose"])))
    total = float(np.sum((data.len - grand)**2))
    np.testing.assert_allclose(ss_supp + ss_dose + ss_interaction + error, total)
    np.testing.assert_allclose(table.sum_sq, [ss_supp, ss_dose, ss_interaction, error])
    np.testing.assert_allclose(third.loc[table.index].sum_sq, table.sum_sq)
    numpy_fit = model.model.exog @ np.linalg.lstsq(model.model.exog, data.len, rcond=None)[0]
    np.testing.assert_allclose(numpy_fit, model.fittedvalues)
    reordered = smf.ols(formula, data=data.sample(frac=1, random_state=202611)).fit()
    np.testing.assert_allclose(reordered.params, model.params, atol=1e-12)
    full_mse = error / 54
    for term in table.index[:-1]:
        np.testing.assert_allclose(table.loc[term, "F"], table.loc[term, "sum_sq"] / table.loc[term, "df"] / full_mse)
    cell_order = [(supp, dose) for supp in ["OJ", "VC"] for dose in DOSES]
    cell_design = np.column_stack([((data.supp == supp) & (data.dose == dose)).astype(float) for supp, dose in cell_order])
    cell_model = sm.OLS(data.len, cell_design).fit()
    robust = cell_model.get_robustcov_results(cov_type="HC3", use_t=True)
    inverse = np.linalg.inv(cell_design.T @ cell_design)
    adjusted = (cell_model.resid / (1 - cell_model.get_influence().hat_matrix_diag))**2
    manual_hc3 = inverse @ (cell_design.T @ (cell_design * adjusted.to_numpy()[:, None])) @ inverse
    np.testing.assert_allclose(manual_hc3, robust.cov_params(), atol=1e-12)
    interaction_contrasts = np.array([[-1, 1, 0, 1, -1, 0], [-1, 0, 1, 1, 0, -1]])
    classical_interaction = cell_model.f_test(interaction_contrasts)
    robust_interaction = robust.f_test(interaction_contrasts)
    np.testing.assert_allclose(classical_interaction.fvalue, table.iloc[2]["F"])
    contrast_estimates = interaction_contrasts @ robust.params
    contrast_covariance = interaction_contrasts @ manual_hc3 @ interaction_contrasts.T
    manual_wald = contrast_estimates @ np.linalg.solve(contrast_covariance, contrast_estimates) / 2
    np.testing.assert_allclose(manual_wald, robust_interaction.fvalue)
    simple = []
    critical = stats.t.ppf(1 - .05 / (2 * 3), 54)
    for position, dose in enumerate(DOSES):
        vector = np.zeros(6)
        vector[position], vector[position+3] = 1, -1
        tested = cell_model.t_test(vector)
        estimate = float((vector @ cell_model.params).item())
        standard_error = float(np.sqrt(vector @ cell_model.cov_params() @ vector))
        np.testing.assert_allclose(standard_error, np.sqrt(full_mse * .2))
        interval = estimate + np.array([-1, 1])*critical*standard_error
        np.testing.assert_allclose(interval, tested.conf_int(alpha=.05/3)[0])
        simple.append({"dose": dose, "difference_OJ_minus_VC": estimate, "se": standard_error,
                       "df": 54, "p_unadjusted": float(tested.pvalue),
                       "p_bonferroni_3": min(1., 3 * float(tested.pvalue)), "ci_family95": interval.tolist()})
    effects = [{"term": name, "SS": float(row.sum_sq), "df": float(row.df),
                "MS": float(row.sum_sq / row.df), "F": float(row.F), "p": float(row["PR(>F)"]),
                "partial_eta_squared": float(row.sum_sq / (row.sum_sq + error))}
               for name, row in table.iloc[:-1].iterrows()]
    results = {"source_relative_to_package": "ToothGrowth.csv",
               "source_url": "https://raw.githubusercontent.com/wch/r-source/trunk/src/library/datasets/data/ToothGrowth.R",
               "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
               "source_normalized_sha256": normalized_hash,
               "same_chapter10_snapshot_verified": True,
               "remote_automatic_comparison": False, "original_article_raw_records_verified": False,
               "one_way": one_way_results, "cells": cells.reset_index().to_dict(orient="records"),
               "factorial": {"n": 60, "effects": effects, "SSE": error, "df_error": 54, "MSE": full_mse,
                             "SST": total, "simple_effects": simple, "interaction_HC3_F": float(robust_interaction.fvalue),
                             "interaction_HC3_p": float(robust_interaction.pvalue), "interaction_HC3_df": [2, 54]},
               "diagnostics": {"residual_shapiro_p": float(stats.shapiro(model.resid).pvalue),
                               "brown_forsythe_six_cells_p": float(stats.levene(*[group.len for _, group in data.groupby(["supp", "dose"])], center="median").pvalue)},
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__, "statsmodels": statsmodels.__version__}}
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    (output / "ozet.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    cells.to_csv(output / "hucreler.csv")
    table.to_csv(output / "faktoriyel_anova.csv")
    pd.DataFrame(simple).to_csv(output / "basit_etkiler.csv", index=False)
    for supp in ["OJ", "VC"]:
        pd.DataFrame(one_way_results[supp]["pairs"]).to_csv(output / f"ikili_{supp}.csv", index=False)
    data.drop(columns="dose_f").assign(supp_kod=data.supp.map({"OJ": 1, "VC": 2}),
                                       dose_kod=data.dose.map({.5: 1, 1.: 2, 2.: 3})).to_csv(output / "analiz_veri.csv", index=False)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.5), constrained_layout=True)
    oj = data.loc[data.supp == "OJ"]
    for position, dose in enumerate(DOSES):
        values = np.sort(oj.loc[oj.dose == dose, "len"])
        axes[0].scatter(position + np.linspace(-.08, .08, len(values)), values, color="#781e2d", s=20)
        axes[0].plot([position-.15, position+.15], [values.mean()]*2, color="#3c3c41", linewidth=2)
    axes[0].set(xticks=[0, 1, 2], xticklabels=["0.5", "1", "2"], xlabel="Doz (mg/gün; kategoriler)", ylabel="Uzunluk (kaynak birimi)", title="(a) OJ: 30 ayrı hayvan")
    for position, pair in enumerate(one_way_results["OJ"]["pairs"]):
        value, bounds = pair["difference"], pair["tukey_ci"]
        axes[1].errorbar(value, position, xerr=[[value-bounds[0]], [bounds[1]-value]], fmt="o", color="#781e2d", capsize=4)
    axes[1].axvline(0, color="#3c3c41", linestyle="--", linewidth=1)
    axes[1].set(yticks=[0, 1, 2], yticklabels=[row["comparison"] for row in one_way_results["OJ"]["pairs"]], xlabel="Ortalama farkı", title="(b) Tukey: aile %95 GA")
    figures = directory / "grafikler"
    figures.mkdir(exist_ok=True)
    figure.savefig(figures / "b11-oj-tukey.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.5), constrained_layout=True)
    for supp, color in [("OJ", "#781e2d"), ("VC", "#3c3c41")]:
        axes[0].plot(DOSES, cells.loc[supp, "mean"], "o-", color=color, label=supp)
    axes[0].legend(frameon=False)
    axes[0].set(xticks=DOSES, xlabel="Doz (mg/gün)", ylabel="Ortalama uzunluk", title="(a) 2 × 3 hücre ortalamaları")
    for position, row in enumerate(simple):
        value, bounds = row["difference_OJ_minus_VC"], row["ci_family95"]
        axes[1].errorbar(value, position, xerr=[[value-bounds[0]], [bounds[1]-value]], fmt="o", color="#781e2d", capsize=4)
    axes[1].axvline(0, color="#3c3c41", linestyle="--", linewidth=1)
    axes[1].set(yticks=[0, 1, 2], yticklabels=["0.5", "1", "2"], ylabel="Doz (mg/gün)", xlabel="OJ − VC farkı", title="(b) Bonferroni: aile %95 GA")
    figure.savefig(figures / "b11-etkilesim.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.1), constrained_layout=True)
    axes[0].scatter(model.fittedvalues, model.resid, color="#781e2d", s=18, alpha=.7)
    axes[0].axhline(0, color="#3c3c41", linewidth=1)
    axes[0].set(xlabel="Tahmin edilen hücre ortalaması", ylabel="Artık", title="(a) Artıklar ve tahminler")
    stats.probplot(model.resid, plot=axes[1])
    axes[1].get_lines()[0].set_color("#3c3c41")
    axes[1].get_lines()[1].set_color("#781e2d")
    axes[1].set(xlabel="Kuramsal normal kantil", ylabel="Artık", title="(b) Normal Q–Q grafiği")
    figure.savefig(figures / "b11-tanilar.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source.read_bytes() == source_bytes
    print(json.dumps(results, indent=2))
    print("Doğrulama başarılı: KT ayrıştırması, klasik/Welch, Tukey/Games–Howell, etkileşim ve aile aralıkları.")


if __name__ == "__main__":
    main()