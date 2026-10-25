"""Çok düzeyli modeller: High School and Beyond alt örneklemi (nlme::MathAchieve, MathAchSchool).

7185 öğrenci, 160 okul. Boş model ve ICC, tasarım etkisi, naif/küme-sağlam/çok düzeyli standart hatalar,
grup ortalamasına merkezleme ve bağlamsal etki, rastgele eğim ve sınırda olabilirlik oranı testi, düzeyler arası
etkileşim. statsmodels MixedLM (REML ve ML) ile; R lme4 karşılaştırması analiz.R'dedir.
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

HASHES = {"MathAchieve.csv": "087beeed36585553ec1b69dd5b29266a99e8189c565d51a301b99e53a2a0be72",
          "MathAchSchool.csv": "f4b5327f022a2433b536bbde8cd6f7273d89b72c69bef8cd6de6bc1cd6a0cf19"}


def read(directory, name):
    path = directory / "kaynak" / name
    raw = path.read_bytes()
    assert hashlib.sha256(raw.rstrip(b"\n") + b"\n").hexdigest() == HASHES[name], f"{name} değişmiş"
    return pd.read_csv(path, dtype={"School": str})


def fit(formula, data, re_formula="1", reml=True):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = smf.mixedlm(formula, data, groups=data["School"], re_formula=re_formula)
        # statsmodels'ta lbfgs bu veride sınırda sahte bir çözümde "yakınsadı" diyebiliyor.
        # Bu yüzden BFGS, Powell ve BFGS'ten başlayan Powell çözümleri karşılaştırılır; en yüksek
        # olabilirlik seçilir ve adaylar arasında büyük fark kalmadığı denetlenir.
        first = model.fit(reml=reml, method=["bfgs"])
        second = model.fit(reml=reml, method=["powell"])
        third = model.fit(reml=reml, method=["powell"], start_params=first.params)
    candidates = [first, second, third]
    result = max(candidates, key=lambda item: item.llf)
    assert result.converged and max(item.llf for item in candidates) - min(item.llf for item in candidates) < .05, \
        (formula, [item.llf for item in candidates])
    covariance = np.atleast_2d(np.asarray(result.cov_re))
    names = list(result.cov_re.index)
    fixed = {name: {"estimate": float(result.fe_params[name]), "se": float(result.bse_fe[name]),
                    "z": float(result.fe_params[name] / result.bse_fe[name]),
                    "p": float(2 * stats.norm.sf(abs(result.fe_params[name] / result.bse_fe[name])))}
             for name in result.fe_params.index}
    random = {"variances": {name: float(covariance[i, i]) for i, name in enumerate(names)},
              "residual_variance": float(result.scale)}
    if len(names) == 2:
        random["correlation"] = float(covariance[0, 1] / np.sqrt(covariance[0, 0] * covariance[1, 1]))
    return result, {"formula": formula, "random": re_formula, "estimator": "REML" if reml else "ML",
                    "fixed": fixed, "random_effects": random, "loglik": float(result.llf),
                    "deviance": float(-2 * result.llf)}


def main():
    directory = Path(__file__).parent
    students = read(directory, "MathAchieve.csv")
    schools = read(directory, "MathAchSchool.csv")
    assert len(students) == 7185 and len(schools) == 160 and students["School"].nunique() == 160
    data = students.merge(schools[["School", "Sector", "Size"]], on="School", validate="many_to_one")
    data["katolik"] = (data["Sector"] == "Catholic").astype(int)
    data["ses_ort"] = data.groupby("School")["SES"].transform("mean")  # örneklemden hesaplanan okul ortalaması
    data["ses_m"] = data["SES"] - data["ses_ort"]                        # grup ortalamasına merkezlenmiş SES
    data["ses_g"] = data["SES"] - data["SES"].mean()                     # genel ortalamaya merkezlenmiş SES
    sizes = data.groupby("School").size()
    summary = {"n_students": len(data), "n_schools": int(len(sizes)), "cluster_size": {"min": int(sizes.min()), "max": int(sizes.max()),
               "mean": float(sizes.mean())}, "catholic_schools": int(schools["Sector"].eq("Catholic").sum()),
               "MathAch": {"mean": float(data["MathAch"].mean()), "sd": float(data["MathAch"].std(ddof=1))},
               "meanses_source_vs_sample_max_abs_diff": float((data["MEANSES"] - data["ses_ort"]).abs().max())}

    # 1) Boş model, ICC ve tasarım etkisi
    _, m0 = fit("MathAch ~ 1", data)
    tau = m0["random_effects"]["variances"]["Group"]
    sigma2 = m0["random_effects"]["residual_variance"]
    icc = tau / (tau + sigma2)
    n_bar = sizes.mean()
    m0["ICC"] = icc
    m0["design_effect"] = 1 + (n_bar - 1) * icc
    m0["effective_n"] = len(data) / m0["design_effect"]
    # Okul ortalamalarının güvenirliği: lambda_j = tau / (tau + sigma2 / n_j)
    reliability = tau / (tau + sigma2 / sizes)
    m0["reliability_of_school_means"] = {"mean": float(reliability.mean()), "min": float(reliability.min()), "max": float(reliability.max())}

    # 2) Naif OLS, küme-sağlam SE ve rastgele kesişimli model: aynı eğim, farklı belirsizlik
    ols = smf.ols("MathAch ~ SES", data).fit()
    robust = smf.ols("MathAch ~ SES", data).fit(cov_type="cluster", cov_kwds={"groups": data["School"].astype("category").cat.codes})
    _, ri = fit("MathAch ~ SES", data)
    standard_errors = {"OLS_naive": {"slope": float(ols.params["SES"]), "se": float(ols.bse["SES"]),
                                     "intercept_se": float(ols.bse["Intercept"])},
                       "OLS_cluster_robust": {"slope": float(robust.params["SES"]), "se": float(robust.bse["SES"]),
                                              "intercept_se": float(robust.bse["Intercept"])},
                       "random_intercept": {"slope": ri["fixed"]["SES"]["estimate"], "se": ri["fixed"]["SES"]["se"],
                                            "intercept_se": ri["fixed"]["Intercept"]["se"]}}

    # 3) Grup içi ve gruplar arası etki: grup ortalamasına merkezleme ve bağlamsal etki
    _, m1 = fit("MathAch ~ ses_m + ses_ort", data)
    _, m1g = fit("MathAch ~ ses_g + ses_ort", data)
    within = m1["fixed"]["ses_m"]["estimate"]
    between = m1["fixed"]["ses_ort"]["estimate"]
    contextual = m1g["fixed"]["ses_ort"]["estimate"]
    np.testing.assert_allclose(contextual, between - within, atol=1e-3)
    school_means = data.groupby("School")[["MathAch", "ses_ort"]].mean()
    between_ols = np.polyfit(school_means["ses_ort"], school_means["MathAch"], 1)[0]
    m1["variance_explained"] = {"level1_sigma2": 1 - m1["random_effects"]["residual_variance"] / sigma2,
                                "level2_tau00": 1 - m1["random_effects"]["variances"]["Group"] / tau}
    effects = {"within": within, "between": between, "contextual_from_grand_centered": contextual,
               "contextual_difference": between - within, "between_ols_on_school_means": float(between_ols)}

    # 4) Rastgele eğim: REML olabilirlik oranı, sınırda karışım dağılımı (0.5 chi2_1 + 0.5 chi2_2)
    _, m2a = fit("MathAch ~ ses_m + ses_ort + katolik", data)
    _, m2b = fit("MathAch ~ ses_m + ses_ort + katolik", data, re_formula="~ses_m")
    lr = 2 * (m2b["loglik"] - m2a["loglik"])
    slope_test = {"LR": float(lr), "p_naive_chi2_2": float(stats.chi2.sf(lr, 2)),
                  "p_mixture": float(.5 * stats.chi2.sf(lr, 1) + .5 * stats.chi2.sf(lr, 2))}

    # 5) Düzeyler arası etkileşim (Raudenbush ve Bryk'in HSB modeline yakın biçim)
    result3, m3 = fit("MathAch ~ ses_m * (ses_ort + katolik)", data, re_formula="~ses_m")
    variance_slope = m3["random_effects"]["variances"]["ses_m"]
    variance_slope_before = m2b["random_effects"]["variances"]["ses_m"]
    m3["slope_variance_explained_by_level2"] = 1 - variance_slope / variance_slope_before
    public_slope = m3["fixed"]["ses_m"]["estimate"]
    catholic_slope = public_slope + m3["fixed"]["ses_m:katolik"]["estimate"]
    m3["implied_slopes_at_mean_ses"] = {"public": public_slope, "catholic": catholic_slope}
    # ML ile sabit etki olabilirlik oranı: düzeyler arası etkileşimler birlikte
    _, full_ml = fit("MathAch ~ ses_m * (ses_ort + katolik)", data, re_formula="~ses_m", reml=False)
    _, reduced_ml = fit("MathAch ~ ses_m + ses_ort + katolik", data, re_formula="~ses_m", reml=False)
    lr_fixed = 2 * (full_ml["loglik"] - reduced_ml["loglik"])
    cross_level_test = {"LR": float(lr_fixed), "df": 2, "p": float(stats.chi2.sf(lr_fixed, 2)),
                        "note": "sabit etki karşılaştırması ML ile; REML olabilirlikleri farklı sabit yapıları karşılaştırmaz"}

    results = {"data": summary, "null_model": m0, "standard_errors": standard_errors, "contextual": m1,
               "contextual_grand_centered": m1g, "effects": effects, "slope_models": {"random_intercept": m2a, "random_slope": m2b},
               "random_slope_test": slope_test, "cross_level": m3, "cross_level_LR_ML": cross_level_test,
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__,
                            "statsmodels": statsmodels.__version__}}
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    data[["School", "Sector", "katolik", "Minority", "Sex", "SES", "ses_ort", "ses_m", "MathAch"]].to_csv(output / "analiz_verisi.csv", index=False)
    (output / "ozet.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Şekil: okul regresyon doğruları (M3 BLUP) ve grup içi/arası eğimler
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(7.4, 3.6), constrained_layout=True)
    blups = pd.DataFrame(result3.random_effects).T
    blups.columns = ["u0", "u1"]
    fe = result3.fe_params
    info = data.groupby("School")[["ses_ort", "katolik"]].first().loc[blups.index]
    grid = np.linspace(-1.5, 1.5, 2)
    for school, row in info.iterrows():
        intercept = fe["Intercept"] + fe["ses_ort"] * row.ses_ort + fe["katolik"] * row.katolik + blups.loc[school, "u0"]
        slope = fe["ses_m"] + fe["ses_m:ses_ort"] * row.ses_ort + fe["ses_m:katolik"] * row.katolik + blups.loc[school, "u1"]
        axes[0].plot(grid, intercept + slope * grid, color="#781e2d" if row.katolik else "#3c3c41", alpha=.35, linewidth=.8)
    axes[0].plot([], [], color="#3c3c41", linewidth=2, label="Devlet okulu (90)")
    axes[0].plot([], [], color="#781e2d", linewidth=2, label="Katolik okul (70)")
    axes[0].set(xlabel="Okul içi SES sapması", ylabel="Tahmini matematik başarısı", title="160 okulun tahmini doğruları")
    axes[0].legend(frameon=False, fontsize=8, loc="upper left")
    axes[1].scatter(school_means["ses_ort"], school_means["MathAch"], s=12, color="#9a9aa0", label="Okul ortalamaları")
    x = np.linspace(school_means["ses_ort"].min(), school_means["ses_ort"].max(), 2)
    center_y = data["MathAch"].mean()
    center_x = data["SES"].mean()
    axes[1].plot(x, center_y + between * (x - center_x), color="#781e2d", linewidth=2, label=f"Okullar arası eğim {between:.2f}")
    axes[1].plot(x, center_y + within * (x - center_x), color="#3c3c41", linewidth=2, linestyle="--", label=f"Okul içi eğim {within:.2f}")
    axes[1].set(xlabel="Okul ortalama SES", ylabel="Okul ortalama başarı", title="Grup içi ve gruplar arası ilişki")
    axes[1].legend(frameon=False, fontsize=8, loc="upper left")
    figures = directory.parent.parent / "assets_figures"
    figures.mkdir(exist_ok=True)
    figure.savefig(figures / "cd-okul-dogrulari.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    brief = {"data": summary, "m0": {k: m0[k] for k in ["ICC", "design_effect", "effective_n", "reliability_of_school_means"]} | {"fixed": m0["fixed"], "random": m0["random_effects"]},
             "se": standard_errors, "effects": effects, "m1": {"fixed": m1["fixed"], "random": m1["random_effects"], "R2": m1["variance_explained"]},
             "slope_test": slope_test, "m2b": m2b["random_effects"],
             "m3": {"fixed": m3["fixed"], "random": m3["random_effects"], "slopes": m3["implied_slopes_at_mean_ses"], "slope_var_expl": m3["slope_variance_explained_by_level2"]},
             "cross": cross_level_test}
    print(json.dumps(brief, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
