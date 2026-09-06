import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import linalg, optimize, stats

SOURCE_HASH = "8726fd25dbfc685be2d3d726e5511bbb31ba9c7b367b6864eb06e0d8669e6557"
MODELS = ["orthogonal", "correlated", "cross_A2"]


def decode(parameters, model):
    loadings = np.zeros((10, 2))
    loadings[np.arange(10), np.repeat([0, 1], 5)] = parameters[:10]
    uniqueness = np.exp(parameters[10:20])
    phi = np.eye(2)
    if model != "orthogonal":
        phi[0, 1] = phi[1, 0] = np.tanh(parameters[20])
    if model == "cross_A2":
        loadings[1, 1] = parameters[21]
    covariance = loadings @ phi @ loadings.T + np.diag(uniqueness)
    return loadings, uniqueness, phi, covariance


def derivatives(parameters, model):
    loadings, uniqueness, phi, _ = decode(parameters, model)
    result = []
    for position in range(10):
        change = np.zeros_like(loadings)
        change[position, position // 5] = 1
        result.append(change @ phi @ loadings.T + loadings @ phi @ change.T)
    for position in range(10):
        change = np.zeros((10, 10))
        change[position, position] = uniqueness[position]
        result.append(change)
    if model != "orthogonal":
        change = np.array([[0, 1], [1, 0]]) * (1 - phi[0, 1] ** 2)
        result.append(loadings @ change @ loadings.T)
    if model == "cross_A2":
        change = np.zeros_like(loadings)
        change[1, 1] = 1
        result.append(change @ phi @ loadings.T + loadings @ phi @ change.T)
    return np.asarray(result)


def objective(parameters, sample, model):
    covariance = decode(parameters, model)[3]
    sign, logdet = np.linalg.slogdet(covariance)
    if sign <= 0:
        raise ValueError("Model kovaryansı pozitif tanımlı değil.")
    inverse = np.linalg.inv(covariance)
    value = logdet + np.trace(sample @ inverse) - np.linalg.slogdet(sample)[1] - len(sample)
    score_matrix = inverse - inverse @ sample @ inverse
    gradient = np.einsum("ij,kji->k", score_matrix, derivatives(parameters, model))
    return float(value), gradient


def numeric_jacobian(function, point):
    columns = []
    for position in range(len(point)):
        step = np.zeros_like(point)
        step[position] = 1e-5
        columns.append((function(point + step) - function(point - step)) / (2e-5))
    return np.stack(columns, axis=-1)


def rmsea_interval(statistic, degrees, observations):
    roots = []
    for target in [.95, .05]:
        if stats.ncx2.cdf(statistic, degrees, 0) <= target:
            root = 0.0
        else:
            upper = max(statistic, 1.0)
            while stats.ncx2.cdf(statistic, degrees, upper) > target:
                upper *= 2
            root = optimize.brentq(lambda noncentrality: stats.ncx2.cdf(statistic, degrees, noncentrality) - target, 0, upper)
            np.testing.assert_allclose(stats.ncx2.cdf(statistic, degrees, root), target, atol=1e-9)
        roots.append(float(np.sqrt(root / (observations * degrees))))
    return roots


def fit(sample, observations, model):
    bounds = [(-3, 3)] * 10 + [(-12, 3)] * 10
    if model != "orthogonal":
        bounds.append((-4, 4))
    if model == "cross_A2":
        bounds.append((-3, 3))
    runs = []
    for loading, correlation in [(.35, .1), (.55, .3), (.75, .5), (.65, -.1)]:
        initial = np.r_[np.full(10, loading), np.full(10, np.log(1 - loading ** 2))]
        if model != "orthogonal":
            initial = np.r_[initial, np.arctanh(correlation)]
        if model == "cross_A2":
            initial = np.r_[initial, .1]
        numerical = numeric_jacobian(lambda params: np.asarray(objective(params, sample, model)[0]), initial)
        np.testing.assert_allclose(objective(initial, sample, model)[1], numerical, atol=1e-7)
        result = optimize.minimize(objective, initial, args=(sample, model), jac=True,
                                   method="L-BFGS-B", bounds=bounds,
                                   options={"ftol": 1e-14, "gtol": 1e-9, "maxiter": 4000})
        if not result.success or np.linalg.norm(result.jac, ord=np.inf) > 2e-5:
            raise RuntimeError(f"Optimizasyon denetimi başarısız: {model}, {result.message}")
        runs.append(result)
    best = min(runs, key=lambda result: result.fun)
    np.testing.assert_allclose([result.fun for result in runs], best.fun, atol=1e-9)
    alternate = optimize.minimize(objective, best.x, args=(sample, model), jac=True,
                                  method="BFGS", options={"gtol": 1e-8, "maxiter": 4000})
    if np.linalg.norm(alternate.jac, ord=np.inf) > 1e-6:
        raise RuntimeError("İkinci algoritmada gradyan küçük değil.")
    np.testing.assert_allclose(alternate.fun, best.fun, atol=1e-9)
    np.testing.assert_allclose(decode(alternate.x, model)[3], decode(best.x, model)[3], atol=2e-6)
    parameters = alternate.x
    assert all(lower + 1e-4 < value < upper - 1e-4 for value, (lower, upper) in zip(parameters, bounds))
    loadings, uniqueness, phi, covariance = decode(parameters, model)
    assert np.all(loadings[np.arange(10), np.repeat([0, 1], 5)] > 0)
    changes = derivatives(parameters, model)
    lower = np.tril_indices(10)
    jacobian = changes[:, lower[0], lower[1]].T
    assert np.linalg.matrix_rank(jacobian) == len(parameters)
    numeric = numeric_jacobian(lambda params: decode(params, model)[3][lower], parameters)
    np.testing.assert_allclose(jacobian, numeric, atol=1e-8)
    inverse = np.linalg.inv(covariance)
    weighted = np.einsum("ij,kjl->kil", inverse, changes)
    information = (observations - 1) / 2 * np.einsum("aij,bji->ab", weighted, weighted)
    expected_hessian = numeric_jacobian(lambda params: objective(params, covariance, model)[1], parameters)
    np.testing.assert_allclose(information, (observations - 1) / 2 * expected_hessian, atol=1e-5)
    eigenvalues = np.linalg.eigvalsh(information)
    assert eigenvalues[0] > 0
    parameter_covariance = np.linalg.inv(information)
    standardized = loadings / np.sqrt(np.diag(covariance))[:, None]
    standard_function = lambda params: (decode(params, model)[0] / np.sqrt(np.diag(decode(params, model)[3]))[:, None])[np.arange(10), np.repeat([0, 1], 5)]
    delta = numeric_jacobian(standard_function, parameters)
    standardized_se = np.sqrt(np.diag(delta @ parameter_covariance @ delta.T))
    score = objective(parameters, sample, model)[0]
    generalized_eigenvalues = linalg.eigvalsh(sample, covariance)
    np.testing.assert_allclose(score, np.sum(generalized_eigenvalues - np.log(generalized_eigenvalues) - 1), atol=1e-10)
    statistic = (observations - 1) * score
    degrees = 55 - len(parameters)
    baseline = -(observations - 1) * np.linalg.slogdet(sample)[1]
    denominator = max(statistic - degrees, baseline - 45, 0)
    cfi = 1 - max(statistic - degrees, 0) / denominator
    tli = (baseline / 45 - statistic / degrees) / (baseline / 45 - 1)
    residual = (sample - covariance) / np.sqrt(np.outer(np.diag(sample), np.diag(sample)))
    srmr = np.sqrt(np.mean(residual[lower] ** 2))
    upper = np.triu_indices(10, 1)
    primary = standardized[np.arange(10), np.repeat([0, 1], 5)]
    items = [{"item": f"{prefix}{position % 5 + 1}", "loading": float(loadings[position, position // 5]),
              "loading_std": float(primary[position]), "loading_std_se": float(standardized_se[position]),
              "loading_std_ci95": (primary[position] + np.array([-1, 1]) * stats.norm.ppf(.975) * standardized_se[position]).tolist(),
              "theta": float(uniqueness[position]), "theta_std": float(uniqueness[position] / covariance[position, position]),
              "R_squared": float(1 - uniqueness[position] / covariance[position, position])}
             for position, prefix in enumerate(["A"] * 5 + ["C"] * 5)]
    result = {"model": model, "free_parameters": len(parameters), "df": degrees, "F_ML": score,
              "chi2": statistic, "p": float(stats.chi2.sf(statistic, degrees)),
              "CFI": cfi, "TLI": tli, "RMSEA": float(np.sqrt(max((statistic - degrees) / (observations * degrees), 0))),
              "RMSEA_ci90": rmsea_interval(statistic, degrees, observations), "SRMR": float(srmr),
              "RMSR_off": float(np.sqrt(np.mean(residual[upper] ** 2))), "baseline_chi2": baseline, "baseline_df": 45,
              "AIC_star": float(statistic + 2 * len(parameters)), "BIC_star": float(statistic + np.log(observations) * len(parameters)),
              "phi": float(phi[0, 1]), "items": items, "minimum_theta": float(uniqueness.min()),
              "jacobian_rank": int(np.linalg.matrix_rank(jacobian)), "information_min_eigenvalue": float(eigenvalues[0]),
              "gradient_max": float(np.max(np.abs(alternate.jac))), "start_objectives": [float(run.fun) for run in runs],
              "optimizer_alternate_success": bool(alternate.success),
              "max_abs_residual": float(np.max(np.abs(residual[upper])))}
    if model != "orthogonal":
        z_se = np.sqrt(parameter_covariance[20, 20])
        result["phi_se"] = float((1 - phi[0, 1] ** 2) * z_se)
        result["phi_ci95"] = np.tanh(parameters[20] + np.array([-1, 1]) * stats.norm.ppf(.975) * z_se).tolist()
    if model == "cross_A2":
        result["A2_cross_loading"] = float(loadings[1, 1])
        result["A2_cross_loading_std"] = float(standardized[1, 1])
    if model == "correlated":
        result["AVE_CR"] = {}
        for scale, indices in [("A", np.arange(5)), ("C", np.arange(5, 10))]:
            squared_sum = primary[indices].sum() ** 2
            errors = sum(items[position]["theta_std"] for position in indices)
            result["AVE_CR"][scale] = {"AVE": float(np.mean(primary[indices] ** 2)),
                                      "CR_standardized_sum": float(squared_sum / (squared_sum + errors))}
    return result, covariance, residual, standardized


def main():
    directory = Path(__file__).resolve().parent
    source_path = directory / "bfi-ilk100-AC.csv"
    original = source_path.read_bytes()
    assert hashlib.sha256(original.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n").hexdigest() == SOURCE_HASH, "Yerel kaynak değişmiş; kaynak ve kitap sonuçlarını birlikte denetleyin."
    source = pd.read_csv(source_path)
    names = [f"{prefix}{number}" for prefix in ["A", "C"] for number in range(1, 6)]
    raw = source[names].dropna().copy()
    for item in ["A1", "C4", "C5"]:
        raw[item] = 7 - raw[item]
    excluded = source.loc[~source.index.isin(raw.index), "kaynak_satir"].tolist()
    assert len(raw) == 97 and excluded == [63, 66, 90]
    standardized = (raw - raw.mean()) / raw.std(ddof=1)
    sample = standardized.cov().to_numpy()
    np.testing.assert_allclose(sample, raw.corr().to_numpy())
    assert np.linalg.eigvalsh(sample)[0] > 0
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    source.loc[raw.index, ["kaynak_satir", "kaynak_kayit"]].join(raw).to_csv(output / "puanlanmis.csv", index=False)
    standardized.to_csv(output / "standartlastirilmis.csv", index=False)
    pd.DataFrame(sample, index=names, columns=names).to_csv(output / "orneklem_kovaryans.csv")
    results = {"n": len(raw), "source_normalized_sha256": SOURCE_HASH,
               "source_raw_sha256": hashlib.sha256(original).hexdigest(),
               "source_remote_automatic_verification": False, "independent_CFA_validation": False,
               "estimator": "normal-theory covariance ML, Wishart multiplier n-1, no mean structure",
               "RMSEA_denominator": "n * df (lavaan convention)", "SRMR_definition": "sample-variance standardized covariance residuals, 55 lower-triangular entries including diagonal",
               "standard_errors": "expected normal-theory information, delta method for standardized loadings; not robust",
               "excluded_source_rows": excluded, "models": {}, "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__}}
    for model in MODELS:
        info, covariance, residual, loadings = fit(sample, len(raw), model)
        results["models"][model] = info
        for label, matrix in [("model", covariance), ("artik", residual)]:
            pd.DataFrame(matrix, index=names, columns=names).to_csv(output / f"{model}_{label}.csv")
        pd.DataFrame(info["items"]).to_csv(output / f"{model}_yukler.csv", index=False)
    main_info = results["models"]["correlated"]
    comparisons = {}
    for constrained, free in [("orthogonal", "correlated"), ("correlated", "cross_A2")]:
        difference = results["models"][constrained]["chi2"] - results["models"][free]["chi2"]
        degrees = results["models"][constrained]["df"] - results["models"][free]["df"]
        assert difference >= 0 and degrees == 1
        comparisons[f"{constrained}_vs_{free}"] = {"chi2_difference": difference, "df_difference": degrees,
                                                   "nominal_p": float(stats.chi2.sf(difference, degrees))}
    results["comparisons"] = comparisons
    (output / "ozet.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axis = plt.subplots(figsize=(6.4, 3.6), constrained_layout=True)
    for offset, prefix in [(0, "A"), (5, "C")]:
        positions = np.arange(offset, offset + 5)
        estimates = [main_info["items"][position]["loading_std"] for position in positions]
        errors = [stats.norm.ppf(.975) * main_info["items"][position]["loading_std_se"] for position in positions]
        axis.errorbar(positions, estimates, yerr=errors, fmt="o", capsize=4, label=prefix,
                      color="#781e2d" if prefix == "A" else "#3c3c41")
    axis.axhline(0, color="gray", linewidth=.7)
    axis.set(xticks=np.arange(10), xticklabels=names, ylabel="Standart yük ve yaklaşık %95 GA", xlabel="Madde", title="İlişkili iki faktör: model temelli, sağlam olmayan aralıklar")
    axis.legend()
    figures = directory / "grafikler"
    figures.mkdir(exist_ok=True)
    figure.savefig(figures / "b15-yuk-araliklari.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source_path.read_bytes() == original
    print(json.dumps(results, indent=2))
    print("Doğrulama başarılı: türevler, çoklu başlangıç, iki optimizer, bilgi matrisi ve uyum hesapları.")


if __name__ == "__main__":
    main()