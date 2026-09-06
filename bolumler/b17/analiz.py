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
import statsmodels.api as sm

SOURCE_HASH = "654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3"
DOSES = [.5, 1., 2.]
GROUPS = ["VC", "OJ"]


def design(data, model, center=1.):
    if model not in {"additive", "interaction", "cells"}:
        raise ValueError("Bilinmeyen model adı.")
    if not {"supp", "dose"}.issubset(data.columns):
        raise ValueError("supp ve dose sütunları gerekli.")
    if data[["supp", "dose"]].isna().any().any() or not data.supp.isin(GROUPS).all():
        raise ValueError("Eksik veya bilinmeyen grup/doz girdisi.")
    if not np.isfinite(data.dose.to_numpy(dtype=float)).all() or not np.isfinite(center):
        raise ValueError("Sonlu doz ve merkez gerekli.")
    if model == "cells" and not data.dose.isin(DOSES).all():
        raise ValueError("Hücre modeli yalnız gözlenen üç doz için tanımlı.")
    group = data["supp"].eq("OJ").to_numpy(dtype=float)
    centered = data["dose"].to_numpy() - center
    if model == "cells":
        return np.column_stack([(data["supp"].eq(group_name) & data["dose"].eq(dose)).to_numpy(dtype=float)
                                for group_name in GROUPS for dose in DOSES])
    columns = [np.ones(len(data)), group, centered]
    if model == "interaction":
        columns.append(group * centered)
    return np.column_stack(columns)


def fit(response, matrix):
    assert np.linalg.matrix_rank(matrix) == matrix.shape[1]
    model = sm.OLS(response, matrix).fit()
    manual = np.linalg.lstsq(matrix, response, rcond=None)[0]
    np.testing.assert_allclose(model.params, manual, atol=1e-10)
    inverse = np.linalg.inv(matrix.T @ matrix)
    np.testing.assert_allclose(model.cov_params(), inverse * model.mse_resid, atol=1e-10)
    influence = model.get_influence()
    leverage = np.sum(matrix * (matrix @ inverse), axis=1)
    np.testing.assert_allclose(leverage, influence.hat_matrix_diag)
    weights = model.resid ** 2 / (1 - leverage) ** 2
    hc3 = inverse @ (matrix.T @ (matrix * weights[:, None])) @ inverse
    np.testing.assert_allclose(hc3, model.get_robustcov_results(cov_type="HC3").cov_params(), atol=1e-10)
    return model, hc3


def comparison(reduced, full):
    degrees = int(reduced.df_resid - full.df_resid)
    extra_ss = float(reduced.ssr - full.ssr)
    statistic = extra_ss / degrees / full.mse_resid
    probability = stats.f.sf(statistic, degrees, full.df_resid)
    np.testing.assert_allclose([statistic, probability, degrees], full.compare_f_test(reduced), atol=1e-10)
    return {"extra_SS": extra_ss, "df_num": degrees, "df_den": int(full.df_resid),
            "F": float(statistic), "p": float(probability),
            "partial_eta_squared": extra_ss / (extra_ss + full.ssr)}


def linear_summary(model, covariance, vector, family=1):
    vector = np.asarray(vector, dtype=float)
    estimate = float(vector @ model.params)
    error = float(np.sqrt(vector @ covariance @ vector))
    statistic = estimate / error
    probability = float(2 * stats.t.sf(abs(statistic), model.df_resid))
    critical = stats.t.ppf(1 - .05 / (2 * family), model.df_resid)
    interval = estimate + np.array([-1, 1]) * critical * error
    return {"estimate": estimate, "se": error, "df": int(model.df_resid), "t": statistic,
            "p_raw": probability, "p_adjusted": min(1., family * probability),
            "ci95": interval.tolist(), "family_size": family}


def main():
    directory = Path(__file__).parent
    source_path = directory / "ToothGrowth.csv"
    original = source_path.read_bytes()
    assert hashlib.sha256(original.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n").hexdigest() == SOURCE_HASH
    data = pd.read_csv(source_path)
    assert list(data.columns) == ["kaynak_satir", "len", "supp", "dose"]
    assert len(data) == 60 and data.notna().all().all()
    np.testing.assert_array_equal(data.kaynak_satir, np.arange(1, 61))
    assert data.groupby(["supp", "dose"]).size().eq(10).all()
    assert set(data.supp) == set(GROUPS) and set(data.dose) == set(DOSES)
    for invalid, name in ((data, "unknown"), (data.assign(supp="XX"), "additive"),
                          (data.assign(dose=np.nan), "interaction"), (data.assign(dose=3.), "cells")):
        try:
            design(invalid, name)
        except ValueError:
            pass
        else:
            raise AssertionError("Geçersiz tasarım sessizce kabul edildi.")
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    data.assign(oj=data.supp.eq("OJ").astype(int), dose_c=data.dose - 1).to_csv(output / "doz_uzunluk.csv", index=False)
    response = data.len.to_numpy()
    models = {name: fit(response, design(data, name)) for name in ["additive", "interaction", "cells"]}
    additive, interaction, cells = [models[name][0] for name in models]
    shuffled = data.sample(frac=1, random_state=17)
    for name, (model, _) in models.items():
        reordered = sm.OLS(shuffled.len.to_numpy(), design(shuffled, name)).fit()
        np.testing.assert_allclose(reordered.params, model.params, atol=1e-10)
        np.testing.assert_allclose(reordered.ssr, model.ssr, atol=1e-10)
    dose_only = fit(response, np.column_stack([np.ones(len(data)), data.dose - 1]))[0]
    group_only = fit(response, np.column_stack([np.ones(len(data)), data.supp.eq("OJ").astype(int)]))[0]
    tests = {"group_in_additive": comparison(dose_only, additive),
             "dose_in_additive": comparison(group_only, additive),
             "interaction_vs_additive": comparison(additive, interaction),
             "lack_of_linear_fit": comparison(interaction, cells)}
    np.testing.assert_allclose(tests["interaction_vs_additive"]["F"], interaction.tvalues[3] ** 2)
    manual_ss = sum(((frame.len - frame.len.mean()) ** 2).sum() for _, frame in data.groupby(["supp", "dose"]))
    np.testing.assert_allclose(cells.ssr, manual_ss)
    np.testing.assert_allclose(cells.params, [data.loc[data.supp.eq(group) & data.dose.eq(dose), "len"].mean()
                                            for group in GROUPS for dose in DOSES])
    refitted = fit(response, design(data, "interaction", center=2.))[0]
    np.testing.assert_allclose(interaction.fittedvalues, refitted.fittedvalues, atol=1e-10)
    np.testing.assert_allclose(refitted.params[1], interaction.params[1] + interaction.params[3], atol=1e-10)
    summaries, contrasts, adjusted = {}, {}, {}
    for name, (model, hc3) in models.items():
        summaries[name] = {"parameters": model.params.tolist(), "df_resid": int(model.df_resid),
                           "SSE": float(model.ssr), "MSE": float(model.mse_resid), "R_squared": float(model.rsquared)}
        contrasts[name], adjusted[name] = {}, {}
        for dose in DOSES:
            rows = pd.DataFrame({"supp": GROUPS, "dose": [dose, dose]})
            matrix = design(rows, name)
            vector = matrix[1] - matrix[0]
            family = 1 if name == "additive" else 3
            contrasts[name][str(dose)] = {"OLS": linear_summary(model, model.cov_params(), vector, family),
                                         "HC3": linear_summary(model, hc3, vector, family)}
            if name != "cells":
                reference = model.t_test(vector)
                np.testing.assert_allclose(contrasts[name][str(dose)]["OLS"]["se"], np.asarray(reference.sd).item())
            adjusted[name][str(dose)] = {group: linear_summary(model, model.cov_params(), matrix[position])
                                        for position, group in enumerate(GROUPS)}
        pd.DataFrame(model.cov_params()).to_csv(output / f"{name}_covariance.csv", index=False)
        pd.DataFrame(hc3).to_csv(output / f"{name}_HC3.csv", index=False)
    slopes = {"VC": linear_summary(interaction, interaction.cov_params(), [0, 0, 1, 0]),
              "OJ": linear_summary(interaction, interaction.cov_params(), [0, 0, 1, 1]),
              "difference": linear_summary(interaction, interaction.cov_params(), [0, 0, 0, 1]),
              "difference_HC3": linear_summary(interaction, models["interaction"][1], [0, 0, 0, 1])}
    leave_one_out = []
    for position in range(len(data)):
        subset = data.drop(index=position)
        model = sm.OLS(subset.len.to_numpy(), design(subset, "interaction")).fit()
        leave_one_out.append({"excluded_source_row": int(data.kaynak_satir.iloc[position]),
                              "difference_at_1": float(model.params[1]), "slope_difference": float(model.params[3])})
    pd.DataFrame(leave_one_out).to_csv(output / "birini_disarida.csv", index=False)
    groups = [frame.len.to_numpy() for _, frame in data.groupby(["supp", "dose"])]
    levene = stats.levene(*groups, center="median")
    descriptive = data.groupby(["supp", "dose"]).len.agg(["count", "mean", "std", "min", "max"])
    descriptive.to_csv(output / "hucre_ozetleri.csv")
    results = {"source_normalized_sha256": SOURCE_HASH, "source_raw_sha256": hashlib.sha256(original).hexdigest(),
               "remote_automatically_verified": False, "n": len(data), "center": 1., "reference": "VC; contrast OJ minus VC",
               "models": summaries, "nested_tests": tests, "slopes": slopes,
               "adjusted_means": adjusted, "contrasts": contrasts,
               "raw_group_means": data.groupby("supp").len.mean().to_dict(),
               "dose_mean_by_group": data.groupby("supp").dose.mean().to_dict(),
               "levene_median_six_cells": {"statistic": float(levene.statistic), "p": float(levene.pvalue)},
               "leave_one_out_ranges": {key: [min(row[key] for row in leave_one_out), max(row[key] for row in leave_one_out)]
                                        for key in ["difference_at_1", "slope_difference"]},
               "inference": "OLS t/F; HC3 t with residual df as sensitivity; three-dose Bonferroni contrasts within each model",
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__, "statsmodels": sm.__version__}}
    (output / "ozet.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    mean_rows = [{"model": name, "dose": dose, "group": group, **summary}
                 for name, doses in adjusted.items() for dose, groups in doses.items()
                 for group, summary in groups.items()]
    pd.DataFrame(mean_rows).to_csv(output / "duzeltilmis_ortalamalar.csv", index=False)
    long_contrasts = [{"model": name, "dose": dose, "covariance": method, **summary}
                      for name, dose_values in contrasts.items() for dose, methods in dose_values.items()
                      for method, summary in methods.items()]
    pd.DataFrame(long_contrasts).to_csv(output / "karsilastirmalar.csv", index=False)
    influence = interaction.get_influence()
    data.assign(tahmin=interaction.fittedvalues, artik=interaction.resid, kaldirac=influence.hat_matrix_diag,
                cook=influence.cooks_distance[0]).to_csv(output / "tanilar.csv", index=False)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.4), constrained_layout=True)
    generator = np.random.default_rng(20260906)
    grid = np.linspace(.5, 2, 100)
    for group, color in [("VC", "#3c3c41"), ("OJ", "#781e2d")]:
        frame = data.loc[data.supp.eq(group)]
        axes[0].scatter(frame.dose + generator.uniform(-.035, .035, len(frame)), frame.len, s=12, color=color, alpha=.65)
        curve = interaction.predict(design(pd.DataFrame({"supp": group, "dose": grid}), "interaction"))
        axes[0].plot(grid, curve, color=color, label=group)
    axes[0].set(xlabel="Doz (mg/gün)", ylabel="Uzunluk (kaynak ölçeği)", title="(a) Ayrı doğrusal eğimler", xticks=DOSES)
    axes[0].legend()
    for name, shift, color, label in [("interaction", -.035, "#781e2d", "Doğrusal"), ("cells", .035, "#3c3c41", "Hücre")]:
        means = np.array([contrasts[name][str(dose)]["OLS"]["estimate"] for dose in DOSES])
        bounds = np.array([contrasts[name][str(dose)]["OLS"]["ci95"] for dose in DOSES])
        axes[1].errorbar(np.asarray(DOSES) + shift, means, yerr=np.array([means - bounds[:, 0], bounds[:, 1] - means]),
                         fmt="o", color=color, capsize=3, label=label)
    axes[1].axhline(0, color="gray", linewidth=.8)
    axes[1].set(xlabel="Doz (mg/gün)", ylabel="OJ − VC ve Bonferroni GA", title="(b) Koşullu farklar", xticks=DOSES)
    axes[1].legend()
    figures = directory / "grafikler"
    figures.mkdir(exist_ok=True)
    figure.savefig(figures / "b17-egimler-karsilastirmalar.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source_path.read_bytes() == original
    print(json.dumps(results, indent=2))
    print("Doğrulama başarılı: OLS, HC3, iç içe F, hücre ortalamaları, merkezleme ve kontrastlar.")


if __name__ == "__main__":
    main()