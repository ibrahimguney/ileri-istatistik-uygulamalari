"""MANOVA: psych::sat.act (SAPA öz bildirim yetenek puanları, n = 700).

Kareler ve çapraz çarpımlar (SSCP) matrisleri elle kurulur; dört çok değişkenli istatistik, F yaklaşımları,
Box M, Mahalanobis uç değer taraması, iki grup Hotelling T^2, ayırma fonksiyonu katsayıları ve iki faktörlü
Tip II MANOVA hesaplanır. statsmodels MANOVA ile karşılaştırılır; R car::Manova analiz.R'dedir.
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
import statsmodels
from scipy import linalg, stats
from statsmodels.multivariate.manova import MANOVA

SOURCE_HASH = "1eebcf05961dd2f569b545e5456c0fd2e5c8b5a79cd82770f3b0a06c31230fce"
DVS = ["ACT", "SATV", "SATQ"]


def sscp(matrix):
    centered = matrix - matrix.mean(axis=0)
    return centered.T @ centered


def multivariate_tests(hypothesis, error, df_h, df_e):
    p = hypothesis.shape[0]
    eigenvalues = np.sort(np.real(linalg.eigvals(np.linalg.solve(error, hypothesis))))[::-1]
    eigenvalues = np.clip(eigenvalues, 0, None)
    s = min(p, df_h)
    eigenvalues = eigenvalues[:s]
    m = (abs(p - df_h) - 1) / 2
    n_ = (df_e - p - 1) / 2
    wilks = float(np.prod(1 / (1 + eigenvalues)))
    pillai = float(np.sum(eigenvalues / (1 + eigenvalues)))
    hotelling = float(np.sum(eigenvalues))
    roy = float(eigenvalues[0])
    # Wilks: Rao F yaklaşımı
    if p ** 2 + df_h ** 2 - 5 > 0:
        t = np.sqrt((p ** 2 * df_h ** 2 - 4) / (p ** 2 + df_h ** 2 - 5))
    else:
        t = 1.0
    df1_w = p * df_h
    df2_w = (df_e - (p - df_h + 1) / 2) * t - (p * df_h - 2) / 2
    f_w = (1 - wilks ** (1 / t)) / wilks ** (1 / t) * df2_w / df1_w
    df1_p, df2_p = s * (2 * m + s + 1), s * (2 * n_ + s + 1)
    f_p = (2 * n_ + s + 1) / (2 * m + s + 1) * pillai / (s - pillai)
    df1_h, df2_h = s * (2 * m + s + 1), 2 * (s * n_ + 1)
    f_h = df2_h * hotelling / (s ** 2 * (2 * m + s + 1))
    r = max(p, df_h)
    df1_r, df2_r = r, df_e - r + df_h
    f_r = roy * df2_r / df1_r
    rows = {"Wilks": (wilks, f_w, df1_w, df2_w), "Pillai": (pillai, f_p, df1_p, df2_p),
            "Hotelling-Lawley": (hotelling, f_h, df1_h, df2_h), "Roy": (roy, f_r, df1_r, df2_r)}
    result = {name: {"value": float(v), "F": float(f), "df1": float(a), "df2": float(b), "p": float(stats.f.sf(f, a, b))}
              for name, (v, f, a, b) in rows.items()}
    result["Roy"]["note"] = "F üst sınırdır; p alt sınırdır"
    result["eigenvalues"] = eigenvalues.tolist()
    result["canonical_correlations"] = np.sqrt(eigenvalues / (1 + eigenvalues)).tolist()
    result["s"] = int(s)
    result["multivariate_eta2_wilks"] = float(1 - wilks ** (1 / s))
    result["pillai_over_s"] = float(pillai / s)
    return result


def one_way(data, factor):
    y = data[DVS].to_numpy(float)
    groups = data[factor].to_numpy()
    levels = np.unique(groups)
    total = sscp(y)
    error = sum(sscp(y[groups == level]) for level in levels)
    hypothesis = total - error
    df_h, df_e = len(levels) - 1, len(y) - len(levels)
    tests = multivariate_tests(hypothesis, error, df_h, df_e)
    univariate = {}
    for position, name in enumerate(DVS):
        ss_h, ss_e = hypothesis[position, position], error[position, position]
        f_value = (ss_h / df_h) / (ss_e / df_e)
        univariate[name] = {"SS_between": float(ss_h), "SS_within": float(ss_e), "F": float(f_value),
                            "p": float(stats.f.sf(f_value, df_h, df_e)), "eta2": float(ss_h / (ss_h + ss_e)),
                            "p_bonferroni": float(min(1, 3 * stats.f.sf(f_value, df_h, df_e)))}
    # Ayırma fonksiyonları: E^{-1}H özvektörleri; ortak grup içi SD ile standartlaştırılmış katsayılar ve yapı katsayıları.
    values, vectors = linalg.eig(hypothesis, error)
    order = np.argsort(np.real(values))[::-1]
    vectors = np.real(vectors[:, order])
    within_cov = error / df_e
    standardized = vectors * np.sqrt(np.diag(within_cov))[:, None]
    standardized = standardized / np.abs(standardized).max(axis=0)
    scores = y @ vectors
    within_corr = within_cov / np.sqrt(np.outer(np.diag(within_cov), np.diag(within_cov)))
    structure = within_corr @ standardized / np.sqrt(np.diag(standardized.T @ within_corr @ standardized))
    means = data.groupby(factor)[DVS].mean()
    counts = data.groupby(factor).size()
    return {"H": hypothesis.tolist(), "E": error.tolist(), "df_h": df_h, "df_e": df_e, "tests": tests,
            "univariate": univariate, "means": means.round(4).to_dict(orient="index"),
            "n": counts.to_dict(), "discriminant_standardized_first": dict(zip(DVS, standardized[:, 0].round(4).tolist())),
            "discriminant_structure_first": dict(zip(DVS, structure[:, 0].round(4).tolist()))}


def box_m(data, factor):
    y = data[DVS].to_numpy(float)
    groups = data[factor].to_numpy()
    levels = np.unique(groups)
    p, g, n_total = y.shape[1], len(levels), len(y)
    covariances = [np.cov(y[groups == level], rowvar=False) for level in levels]
    sizes = [int((groups == level).sum()) for level in levels]
    pooled = sum((n - 1) * c for n, c in zip(sizes, covariances)) / (n_total - g)
    m = (n_total - g) * np.linalg.slogdet(pooled)[1] - sum((n - 1) * np.linalg.slogdet(c)[1] for n, c in zip(sizes, covariances))
    c1 = (sum(1 / (n - 1) for n in sizes) - 1 / (n_total - g)) * (2 * p ** 2 + 3 * p - 1) / (6 * (p + 1) * (g - 1))
    chi2 = m * (1 - c1)
    df = p * (p + 1) * (g - 1) / 2
    sds = {str(level): np.sqrt(np.diag(c)).round(3).tolist() for level, c in zip(levels, covariances)}
    return {"M": float(m), "chi2": float(chi2), "df": float(df), "p": float(stats.chi2.sf(chi2, df)), "group_sds": sds}


def two_group(data):
    y = data[["SATV", "SATQ"]].to_numpy(float)
    male = data["gender"].to_numpy() == 1
    a, b = y[male], y[~male]
    n1, n2 = len(a), len(b)
    difference = a.mean(axis=0) - b.mean(axis=0)
    pooled = ((n1 - 1) * np.cov(a, rowvar=False) + (n2 - 1) * np.cov(b, rowvar=False)) / (n1 + n2 - 2)
    d2 = difference @ np.linalg.solve(pooled, difference)
    t2 = n1 * n2 / (n1 + n2) * d2
    p = 2
    f_value = (n1 + n2 - p - 1) / (p * (n1 + n2 - 2)) * t2
    weights = np.linalg.solve(pooled, difference)
    univariate = {}
    for position, name in enumerate(["SATV", "SATQ"]):
        test = stats.ttest_ind(a[:, position], b[:, position])
        univariate[name] = {"male_mean": float(a[:, position].mean()), "female_mean": float(b[:, position].mean()),
                            "difference": float(difference[position]), "t": float(test.statistic), "p": float(test.pvalue),
                            "d": float(difference[position] / np.sqrt(pooled[position, position]))}
    gap_a, gap_b = a[:, 1] - a[:, 0], b[:, 1] - b[:, 0]
    gap = stats.ttest_ind(gap_a, gap_b)
    return {"n_male": n1, "n_female": n2, "univariate": univariate, "pooled_cov": pooled.tolist(),
            "pooled_correlation": float(pooled[0, 1] / np.sqrt(pooled[0, 0] * pooled[1, 1])),
            "mahalanobis_D": float(np.sqrt(d2)), "T2": float(t2), "F": float(f_value), "df1": p, "df2": n1 + n2 - p - 1,
            "p": float(stats.f.sf(f_value, p, n1 + n2 - p - 1)),
            "discriminant_raw": dict(zip(["SATV", "SATQ"], weights.tolist())),
            "discriminant_standardized": dict(zip(["SATV", "SATQ"], (weights * np.sqrt(np.diag(pooled))).tolist())),
            "gap_SATQ_minus_SATV": {"male_mean": float(gap_a.mean()), "female_mean": float(gap_b.mean()),
                                    "t": float(gap.statistic), "p": float(gap.pvalue),
                                    "d": float((gap_a.mean() - gap_b.mean()) / np.sqrt(((n1 - 1) * gap_a.var(ddof=1) + (n2 - 1) * gap_b.var(ddof=1)) / (n1 + n2 - 2)))}}


def design_matrix(data, terms):
    columns = [np.ones(len(data))]
    gender = np.where(data["gender"].to_numpy() == 1, 1.0, -1.0)
    education = pd.get_dummies(data["education"]).to_numpy(float)
    education = education[:, :-1] - education[:, [-1]]  # toplam-sıfır kodlama
    if "gender" in terms:
        columns.append(gender)
    if "education" in terms:
        columns.extend(education.T)
    if "interaction" in terms:
        columns.extend((education * gender[:, None]).T)
    return np.column_stack(columns)


def residual_sscp(data, terms):
    x = design_matrix(data, terms)
    y = data[DVS].to_numpy(float)
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    residual = y - x @ beta
    return residual.T @ residual, x.shape[1]


def two_way_type2(data):
    full, rank_full = residual_sscp(data, ["gender", "education", "interaction"])
    df_e = len(data) - rank_full
    comparisons = {"gender": (["education"], ["gender", "education"]),
                   "education": (["gender"], ["gender", "education"]),
                   "gender:education": (["gender", "education"], ["gender", "education", "interaction"])}
    result = {}
    for name, (reduced_terms, bigger_terms) in comparisons.items():
        reduced, rank_r = residual_sscp(data, reduced_terms)
        bigger, rank_b = residual_sscp(data, bigger_terms)
        hypothesis = reduced - bigger
        result[name] = multivariate_tests(hypothesis, full, rank_b - rank_r, df_e)
        result[name]["df_hypothesis"] = rank_b - rank_r
    result["df_error"] = df_e
    return result


def main():
    directory = Path(__file__).parent
    path = directory / "kaynak" / "sat_act.csv"
    raw = path.read_bytes()
    assert hashlib.sha256(raw.rstrip(b"\n") + b"\n").hexdigest() == SOURCE_HASH
    source = pd.read_csv(path)
    assert len(source) == 700
    missing = source[DVS].isna().sum().to_dict()
    data = source.dropna(subset=DVS).copy()
    assert len(data) == 687 and missing["SATQ"] == 13
    # Mahalanobis uç değer taraması (bütün örneklem kovaryansıyla, p = 3, ki-kare .999 eşiği).
    y = data[DVS].to_numpy(float)
    centered = y - y.mean(axis=0)
    distance = np.einsum("ij,ij->i", centered @ np.linalg.inv(np.cov(y, rowvar=False)), centered)
    cutoff = stats.chi2.ppf(.999, 3)
    data["mahalanobis2"] = distance
    outliers = data[distance > cutoff].sort_values("mahalanobis2", ascending=False)
    results = {"n_source": 700, "n_complete": len(data), "missing": missing,
               "descriptives": {"mean": data[DVS].mean().round(4).to_dict(), "sd": data[DVS].std(ddof=1).round(4).to_dict(),
                                "correlation": data[DVS].corr().round(4).to_dict()},
               "outliers": {"cutoff_chi2_999": float(cutoff), "count": int(len(outliers)),
                            "records": outliers[["kayit", "gender", "education"] + DVS + ["mahalanobis2"]].round(3).to_dict(orient="records")},
               "two_group_gender": two_group(data),
               "oneway_education": one_way(data, "education"),
               "box_m_education": box_m(data, "education"), "box_m_gender": box_m(data, "gender"),
               "two_way_type2": two_way_type2(data)}
    clean = data[distance <= cutoff]
    results["sensitivity_without_outliers"] = {"n": len(clean), "education": one_way(clean, "education")["tests"],
                                               "gender_two_group": {k: v for k, v in two_group(clean).items() if k in ("T2", "F", "p", "mahalanobis_D")}}
    # statsmodels ile karşılaştırma (tek yönlü eğitim MANOVA'sı).
    frame = data.assign(egitim=data["education"].astype(str))
    stats_table = MANOVA.from_formula("ACT + SATV + SATQ ~ egitim", frame).mv_test().results["egitim"]["stat"]
    mine = results["oneway_education"]["tests"]
    for label, name in [("Wilks' lambda", "Wilks"), ("Pillai's trace", "Pillai"),
                        ("Hotelling-Lawley trace", "Hotelling-Lawley"), ("Roy's greatest root", "Roy")]:
        np.testing.assert_allclose(float(stats_table.loc[label, "Value"]), mine[name]["value"], rtol=1e-8)
        if name != "Hotelling-Lawley":  # statsmodels McKeon yaklaşımını kullanır; R/SPSS ile aynı olan Pillai-Samson burada
            np.testing.assert_allclose(float(stats_table.loc[label, "F Value"]), mine[name]["F"], rtol=1e-6)
    results["versions"] = {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__,
                           "statsmodels": statsmodels.__version__}
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    data.drop(columns="mahalanobis2").to_csv(output / "analiz_verisi.csv", index=False)
    (output / "ozet.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(7.4, 3.6), constrained_layout=True)
    colors = {1: "#3c3c41", 2: "#781e2d"}
    names = {1: "Erkek", 2: "Kadın"}
    for code in (1, 2):
        part = data.loc[data["gender"] == code, ["SATV", "SATQ"]].to_numpy(float)
        center = part.mean(axis=0)
        covariance = np.cov(part, rowvar=False) / len(part)  # ortalama vektörünün kovaryansı
        values, vectors = np.linalg.eigh(covariance)
        radius = np.sqrt(stats.chi2.ppf(.95, 2))
        angles = np.linspace(0, 2 * np.pi, 200)
        ellipse = center + (vectors @ np.diag(np.sqrt(values) * radius) @ np.vstack([np.cos(angles), np.sin(angles)])).T
        axes[0].fill(ellipse[:, 0], ellipse[:, 1], color=colors[code], alpha=.18)
        axes[0].plot(ellipse[:, 0], ellipse[:, 1], color=colors[code], linewidth=1)
        axes[0].scatter(*center, s=40, color=colors[code], label=f"{names[code]} (n = {len(part)})", zorder=3)
    axes[0].set(xlabel="SATV ortalaması", ylabel="SATQ ortalaması", title="Ortalama vektörleri, %95 güven elipsi")
    axes[0].legend(frameon=False, loc="upper left", fontsize=8)
    means = data.groupby("education")[DVS].mean()
    counts = data.groupby("education").size()
    standardized = (means - data[DVS].mean()) / data[DVS].std(ddof=1)
    for position, name in enumerate(DVS):
        axes[1].plot(standardized.index, standardized[name], marker="o", label=name,
                     color=["#781e2d", "#3c3c41", "#9a9aa0"][position])
    axes[1].axhline(0, color="gray", linewidth=.7)
    axes[1].set(xticks=standardized.index, xticklabels=[f"{level}\n(n={counts[level]})" for level in standardized.index],
                xlabel="Eğitim kodu", ylabel="Ortalama (z birimi)", title="Eğitim düzeylerinde ortalamalar")
    axes[1].tick_params(axis="x", labelsize=7)
    axes[1].legend(frameon=False, fontsize=8)
    figures = directory.parent.parent / "assets_figures"
    figures.mkdir(exist_ok=True)
    figure.savefig(figures / "mv-sat-gruplar.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    print(json.dumps({"gender": {k: results["two_group_gender"][k] for k in ["T2", "F", "p", "mahalanobis_D", "discriminant_standardized", "gap_SATQ_minus_SATV", "univariate"]},
                      "education": {k: v for k, v in results["oneway_education"]["tests"].items()},
                      "univariate": results["oneway_education"]["univariate"],
                      "disc": [results["oneway_education"]["discriminant_standardized_first"], results["oneway_education"]["discriminant_structure_first"]],
                      "box": [results["box_m_education"], results["box_m_gender"]],
                      "two_way": {k: (v["Pillai"] if isinstance(v, dict) else v) for k, v in results["two_way_type2"].items()},
                      "outliers": results["outliers"]["count"], "sens": results["sensitivity_without_outliers"]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
