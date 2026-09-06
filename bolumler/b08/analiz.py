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
from scipy.special import expit
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

SOURCE_HASH = "3ad427ac4ce8da8f4fc8d12fcb271d6f0a2699a0e086dc18d9ae4400636462b5"
SOURCE_URL = "https://archive.ics.uci.edu/static/public/320/data.csv"
OUTCOME_CUTOFF = 14
THRESHOLDS = (0.3, 0.5, 0.7)


def prepare(source):
    return source.assign(age_c=source.age - 16,
                         hedef14=(source.G3 >= OUTCOME_CUTOFF).astype(int))


def design(data):
    return sm.add_constant(data[["G1", "age_c"]], has_constant="add")


def coefficients(model, logistic=False):
    intervals = np.asarray(model.conf_int())
    return {name: {"estimate": float(model.params[position]),
                   "se": float(model.bse[position]),
                   "p": float(model.pvalues[position]),
                   "ci": intervals[position].tolist(),
                   **({"OR": float(np.exp(model.params[position])),
                       "OR_wald_ci": np.exp(intervals[position]).tolist()} if logistic else {})}
            for position, name in enumerate(["const", "G1", "age_c"])}


def classification(observed, probabilities, threshold):
    observed = np.asarray(observed, dtype=int)
    predicted = np.asarray(probabilities) >= threshold
    true_positive = int(np.sum((observed == 1) & predicted))
    false_negative = int(np.sum((observed == 1) & ~predicted))
    true_negative = int(np.sum((observed == 0) & ~predicted))
    false_positive = int(np.sum((observed == 0) & predicted))
    assert true_positive + false_negative + true_negative + false_positive == len(observed)
    return {"threshold": threshold, "TP": true_positive, "FN": false_negative,
            "TN": true_negative, "FP": false_positive,
            "sensitivity": true_positive / int(np.sum(observed == 1)),
            "specificity": true_negative / int(np.sum(observed == 0)),
            "accuracy": (true_positive + true_negative) / len(observed)}


def performance(observed, probabilities, baseline):
    observed = np.asarray(observed, dtype=int)
    probabilities = np.asarray(probabilities)
    assert np.isin(observed, [0, 1]).all() and len(np.unique(observed)) == 2
    assert np.all((probabilities > 0) & (probabilities < 1))
    positive = probabilities[observed == 1]
    negative = probabilities[observed == 0]
    auc = np.mean((positive[:, None] > negative) + 0.5 * (positive[:, None] == negative))
    ranks = stats.rankdata(probabilities, method="average")
    rank_auc = (ranks[observed == 1].sum() - len(positive) * (len(positive) + 1) / 2)
    np.testing.assert_allclose(auc, rank_auc / (len(positive) * len(negative)))
    return {"n": len(observed), "events": int(observed.sum()), "AUC": float(auc),
            "Brier": float(np.mean((observed - probabilities) ** 2)),
            "baseline_Brier": float(np.mean((observed - baseline) ** 2)),
            "always_zero_accuracy": float(np.mean(observed == 0)),
            "thresholds": [classification(observed, probabilities, value) for value in THRESHOLDS]}


def main():
    directory = Path(__file__).resolve().parent
    source_path = directory / "veri.csv"
    source_bytes = source_path.read_bytes()
    normalized_bytes = source_bytes.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    assert hashlib.sha256(normalized_bytes).hexdigest() == SOURCE_HASH
    source = pd.read_csv(source_path)
    assert list(source.columns) == ["kaynak_satir", "school", "age", "G1", "G3"]
    assert len(source) == 80 and source.notna().all().all()
    np.testing.assert_array_equal(source.kaynak_satir, np.arange(1, 81))
    assert source.school.eq("GP").all() and source.age.between(15, 22).all()
    assert source[["G1", "G3"]].apply(lambda column: column.between(0, 20).all()).all()
    data = prepare(source.iloc[:60].copy())
    transfer = prepare(source.iloc[60:].copy())
    predictors = design(data)
    matrix = predictors.to_numpy()
    linear = sm.OLS(data.G3.to_numpy(), matrix, missing="raise").fit()
    simple = sm.OLS(data.G3.to_numpy(), matrix[:, :2]).fit()
    logistic = sm.Logit(data.hedef14.to_numpy(), matrix, missing="raise").fit(disp=False)
    assert logistic.mle_retvals["converged"]
    np.testing.assert_allclose(linear.params, np.linalg.lstsq(matrix, data.G3, rcond=None)[0])
    np.testing.assert_allclose(linear.rsquared_adj,
                               1 - (1 - linear.rsquared) * (len(data) - 1) / (len(data) - 3))
    residual_g1 = sm.OLS(data.G1.to_numpy(), matrix[:, [0, 2]]).fit().resid
    residual_g3 = sm.OLS(data.G3.to_numpy(), matrix[:, [0, 2]]).fit().resid
    np.testing.assert_allclose(linear.params[1], residual_g1 @ residual_g3 / (residual_g1 @ residual_g1))
    nested_f, nested_p, difference_df = linear.compare_f_test(simple)
    np.testing.assert_allclose(nested_f, linear.tvalues[2] ** 2)
    np.testing.assert_allclose(nested_p, linear.pvalues[2], rtol=1e-10, atol=0)
    influence = linear.get_influence()
    robust = linear.get_robustcov_results(cov_type="HC3", use_t=True)
    bread = np.linalg.inv(matrix.T @ matrix)
    adjusted = (linear.resid / (1 - influence.hat_matrix_diag)) ** 2
    covariance_hc3 = bread @ (matrix.T @ (matrix * adjusted[:, None])) @ bread
    np.testing.assert_allclose(robust.bse, np.sqrt(np.diag(covariance_hc3)))
    glm = sm.GLM(data.hedef14.to_numpy(), matrix, family=sm.families.Binomial()).fit()
    np.testing.assert_allclose(logistic.params, glm.params, rtol=1e-7, atol=1e-7)
    observed = data.hedef14.to_numpy()
    def objective(parameters):
        linear_predictor = matrix @ parameters
        return np.sum(np.logaddexp(0, linear_predictor) - observed * linear_predictor)
    def gradient(parameters):
        return matrix.T @ (expit(matrix @ parameters) - observed)
    def hessian(parameters):
        probability = expit(matrix @ parameters)
        return matrix.T @ (matrix * (probability * (1 - probability))[:, None])
    independent = optimize.minimize(objective, np.zeros(3), jac=gradient, hess=hessian,
                                    method="trust-exact", options={"gtol": 1e-8})
    assert np.linalg.norm(gradient(independent.x)) < 1e-6
    np.testing.assert_allclose(logistic.params, independent.x, rtol=1e-6, atol=1e-6)
    information = hessian(logistic.params)
    assert np.linalg.eigvalsh(information).min() > 0
    np.testing.assert_allclose(logistic.bse, np.sqrt(np.diag(np.linalg.inv(information))))
    linear_no_first = sm.OLS(data.G3.to_numpy()[1:], matrix[1:]).fit()
    logistic_no_first = sm.Logit(observed[1:], matrix[1:]).fit(disp=False)
    probabilities = logistic.predict(matrix)
    transfer_matrix = design(transfer).to_numpy()
    transfer_probabilities = logistic.predict(transfer_matrix)
    baseline = observed.mean()
    profiles = pd.DataFrame({"G1": [12, 13, 14, 14], "age": [16, 16, 16, 15]})
    profile_matrix = sm.add_constant(profiles.assign(age_c=profiles.age - 16)[["G1", "age_c"]],
                                     has_constant="add").to_numpy()
    profiles["G3_tahmin"] = linear.predict(profile_matrix)
    profiles["hedef14_olasilik"] = logistic.predict(profile_matrix)
    results = {
        "source_doi": "10.24432/C5TG7T", "source_url": SOURCE_URL,
        "local_projection_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "official_csv_automatically_verified": False,
        "normalized_LF_sha256": SOURCE_HASH,
        "selection": "Source rows 1-60 fit; rows 61-80 frozen-model exercise; all GP",
        "outcome_definition": "hedef14 = 1 if G3 >= 14, else 0; teaching threshold, not official pass mark",
        "n": len(data), "events": int(observed.sum()),
        "simple_R_squared": float(simple.rsquared),
        "linear": {"coefficients": coefficients(linear), "HC3": coefficients(robust),
                   "R_squared": float(linear.rsquared), "adjusted_R_squared": float(linear.rsquared_adj),
                   "F": float(linear.fvalue), "F_p": float(linear.f_pvalue),
                   "delta_R_squared": float(linear.rsquared - simple.rsquared),
                   "nested_F": float(nested_f), "nested_p": float(nested_p),
                   "VIF": {name: float(variance_inflation_factor(matrix, position))
                           for position, name in [(1, "G1"), (2, "age_c")]},
                   "first_row_leverage": float(influence.hat_matrix_diag[0]),
                   "first_row_Cook": float(influence.cooks_distance[0][0]),
                   "without_first": coefficients(linear_no_first)},
        "logistic": {"coefficients": coefficients(logistic, logistic=True),
                     "log_likelihood": float(logistic.llf), "LR": float(logistic.llr),
                     "LR_p": float(logistic.llr_pvalue), "McFadden_R_squared": float(logistic.prsquared),
                     "without_first": coefficients(logistic_no_first, logistic=True)},
        "training": performance(observed, probabilities, baseline),
        "transfer": performance(transfer.hedef14, transfer_probabilities, baseline),
        "profiles": profiles.to_dict(orient="records"),
        "versions": {"numpy": np.__version__, "pandas": pd.__version__,
                     "scipy": scipy.__version__, "statsmodels": sm.__version__}
    }
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    (output / "ozet.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    prepare(source).to_csv(output / "hazirlanmis.csv", index=False)
    data.assign(G3_tahmin=linear.fittedvalues, artik=linear.resid,
                kaldirac=influence.hat_matrix_diag, cook=influence.cooks_distance[0],
                hedef14_olasilik=probabilities).to_csv(output / "tani.csv", index=False)
    transfer.assign(G3_tahmin=linear.predict(transfer_matrix),
                    hedef14_olasilik=transfer_probabilities).to_csv(output / "aktarim.csv", index=False)
    profiles.to_csv(output / "profiller.csv", index=False)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.6), constrained_layout=True)
    grouped = data.groupby(["G1", "G3"]).size().reset_index(name="adet")
    axes[0].scatter(grouped.G1, grouped.G3, s=14 * grouped.adet, color="#3c3c41", alpha=0.55)
    for age, color in [(15, "#781e2d"), (16, "#b08743")]:
        age_subset = data.loc[data.age == age, "G1"]
        grid = np.linspace(age_subset.min(), age_subset.max(), 150)
        prediction_matrix = np.column_stack([np.ones(len(grid)), grid, np.full(len(grid), age - 16)])
        axes[0].plot(grid, linear.predict(prediction_matrix), label=f"Yaş {age}", color=color)
        axes[1].plot(grid, logistic.predict(prediction_matrix), label=f"Yaş {age}", color=color)
    axes[0].set(xlabel="Birinci dönem notu (G1)", ylabel="Yıl sonu notu (G3)", title="(a) Koşullu ortalama")
    axes[1].axhline(0.5, color="#777777", linestyle=":", linewidth=1)
    axes[1].set(xlabel="Birinci dönem notu (G1)", ylabel="P(G3 ≥ 14)",
                title="(b) Model olasılığı", ylim=(-0.03, 1.03))
    for axis in axes:
        axis.spines[["top", "right"]].set_visible(False)
        axis.legend(frameon=False, fontsize=8)
    assets = directory / "grafikler"
    assets.mkdir(exist_ok=True)
    figure.savefig(assets / "b08-uci-modeller.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.2), constrained_layout=True)
    axes[0].scatter(linear.fittedvalues, linear.resid, color="#781e2d", s=20)
    axes[0].axhline(0, color="#777777", linewidth=1)
    axes[0].annotate("Satır 1", (linear.fittedvalues[0], linear.resid[0]),
                     xytext=(5, 5), textcoords="offset points", fontsize=8)
    axes[0].set(xlabel="Tahmin edilen G3", ylabel="Artık", title="(a) Artıklar")
    axes[1].scatter(influence.hat_matrix_diag, influence.cooks_distance[0], color="#781e2d", s=20)
    axes[1].annotate("Satır 1", (influence.hat_matrix_diag[0], influence.cooks_distance[0][0]),
                     xytext=(-37, -12), textcoords="offset points", fontsize=8)
    axes[1].set(xlabel="Kaldıraç", ylabel="Cook uzaklığı", title="(b) Gözlem etkisi")
    for axis in axes:
        axis.spines[["top", "right"]].set_visible(False)
    figure.savefig(assets / "b08-uci-tani.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source_path.read_bytes() == source_bytes
    print(json.dumps(results, indent=2))
    print("Doğrulama başarılı: yerel hash, OLS/FWL/HC3, logit/GLM/SciPy ve sınıflandırma.")


if __name__ == "__main__":
    main()