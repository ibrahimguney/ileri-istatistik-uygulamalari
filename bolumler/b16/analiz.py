import hashlib
import importlib.util
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
NAMES = [f"{prefix}{number}" for prefix in ["A", "C"] for number in range(1, 6)]
FREE_ROWS = np.array([1, 2, 3, 4, 6, 7, 8, 9])
FACTOR_INDEX = np.repeat([0, 1], 5)


def decode(parameters, direction):
    if direction not in ["forward", "reverse", "zero"]:
        raise ValueError("Bilinmeyen yapısal model.")
    loadings = np.zeros((10, 2))
    loadings[0, 0] = loadings[5, 1] = 1.
    loadings[FREE_ROWS, FACTOR_INDEX[FREE_ROWS]] = parameters[:8]
    theta = np.exp(parameters[8:18])
    variance, disturbance = np.exp(parameters[18:20])
    path = 0. if direction == "zero" else parameters[20]
    latent = np.array([[variance, path * variance],
                       [path * variance, path ** 2 * variance + disturbance]])
    if direction == "reverse":
        latent = latent[::-1, ::-1]
    covariance = loadings @ latent @ loadings.T + np.diag(theta)
    return loadings, theta, latent, covariance


def derivatives(parameters, direction):
    loadings, theta, _, _ = decode(parameters, direction)
    latent = decode(parameters, direction)[2]
    result = []
    for row in FREE_ROWS:
        change = np.zeros((10, 2))
        change[row, FACTOR_INDEX[row]] = 1.
        result.append(change @ latent @ loadings.T + loadings @ latent @ change.T)
    for row in range(10):
        change = np.zeros((10, 10))
        change[row, row] = theta[row]
        result.append(change)
    variance, disturbance = np.exp(parameters[18:20])
    path = 0. if direction == "zero" else parameters[20]
    changes = [np.array([[variance, path * variance], [path * variance, path ** 2 * variance]]),
               np.array([[0., 0.], [0., disturbance]])]
    if direction != "zero":
        changes.append(np.array([[0., variance], [variance, 2 * path * variance]]))
    for change in changes:
        if direction == "reverse":
            change = change[::-1, ::-1]
        result.append(loadings @ change @ loadings.T)
    return np.asarray(result)


def objective(parameters, sample, direction):
    covariance = decode(parameters, direction)[3]
    sign, logdet = np.linalg.slogdet(covariance)
    if sign <= 0:
        raise ValueError("Pozitif tanımlı olmayan model kovaryansı.")
    inverse = np.linalg.inv(covariance)
    value = logdet + np.trace(sample @ inverse) - np.linalg.slogdet(sample)[1] - len(sample)
    gradient = np.einsum("ij,kji->k", inverse - inverse @ sample @ inverse,
                         derivatives(parameters, direction))
    return float(value), gradient


def numeric_jacobian(function, parameters):
    changes = []
    for position in range(len(parameters)):
        shift = np.zeros(len(parameters))
        shift[position] = 1e-5
        changes.append((function(parameters + shift) - function(parameters - shift)) / 2e-5)
    return np.stack(changes, axis=-1)


def initial_from_cfa(info, direction):
    raw = np.array([item["loading"] for item in info["items"]])
    markers = raw[[0, 5]]
    loads = raw / markers[FACTOR_INDEX]
    variances = markers ** 2
    correlation = info["phi"]
    exogenous, endogenous = (1, 0) if direction == "reverse" else (0, 1)
    variance = variances[exogenous]
    disturbance = variances[endogenous] * (1 - correlation ** 2)
    path = correlation * markers[endogenous] / markers[exogenous]
    if direction == "zero":
        disturbance = variances[endogenous]
    parameters = np.r_[loads[FREE_ROWS], np.log([item["theta"] for item in info["items"]]),
                       np.log(variance), np.log(disturbance)]
    return parameters if direction == "zero" else np.r_[parameters, path]


def derived(parameters, direction):
    variance, disturbance = np.exp(parameters[18:20])
    path = 0. if direction == "zero" else parameters[20]
    total = path ** 2 * variance + disturbance
    standardized = path * np.sqrt(variance / total)
    return np.array([path, variance, disturbance, total, standardized, standardized ** 2])


def fit(sample, observations, direction, initial, rmsea_interval):
    bounds = [(-10, 10)] * 8 + [(-12, 4)] * 12
    if direction != "zero":
        bounds.append((-10, 10))
    generator = np.random.default_rng(20260906)
    starts = [initial, initial + generator.normal(0, .15, len(initial)),
              initial + generator.normal(0, .30, len(initial))]
    runs = []
    for start in starts:
        numeric = numeric_jacobian(lambda point: np.asarray(objective(point, sample, direction)[0]), start)
        np.testing.assert_allclose(numeric, objective(start, sample, direction)[1], atol=1e-7)
        result = optimize.minimize(objective, start, args=(sample, direction), jac=True,
                                   method="L-BFGS-B", bounds=bounds,
                                   options={"ftol": 1e-14, "gtol": 1e-9, "maxiter": 5000})
        if not result.success or np.max(np.abs(result.jac)) > 2e-5:
            raise RuntimeError(f"Başlangıç yakınsamadı: {direction}: {result.message}")
        runs.append(result)
    best = min(runs, key=lambda result: result.fun)
    np.testing.assert_allclose([result.fun for result in runs], best.fun, atol=1e-9)
    alternate = optimize.minimize(objective, best.x, args=(sample, direction), jac=True,
                                  method="BFGS", options={"gtol": 1e-8, "maxiter": 5000})
    if np.max(np.abs(alternate.jac)) > 1e-6:
        raise RuntimeError("İkinci optimizasyonda gradyan büyük.")
    np.testing.assert_allclose(alternate.fun, best.fun, atol=1e-9)
    parameters = alternate.x
    assert all(lower + 1e-4 < value < upper - 1e-4 for value, (lower, upper) in zip(parameters, bounds))
    loadings, theta, latent, covariance = decode(parameters, direction)
    np.testing.assert_allclose(covariance, decode(best.x, direction)[3], atol=2e-6)
    changes = derivatives(parameters, direction)
    lower_indices = np.tril_indices(10)
    jacobian = changes[:, lower_indices[0], lower_indices[1]].T
    np.testing.assert_allclose(jacobian,
                              numeric_jacobian(lambda point: decode(point, direction)[3][lower_indices], parameters),
                              atol=1e-7)
    rank = int(np.linalg.matrix_rank(jacobian))
    assert rank == len(parameters)
    inverse = np.linalg.inv(covariance)
    weighted = np.einsum("ij,kjl->kil", inverse, changes)
    information = (observations - 1) / 2 * np.einsum("aij,bji->ab", weighted, weighted)
    expected_hessian = numeric_jacobian(lambda point: objective(point, covariance, direction)[1], parameters)
    np.testing.assert_allclose(information, (observations - 1) / 2 * expected_hessian, atol=2e-5)
    assert np.linalg.eigvalsh(information)[0] > 0
    parameter_covariance = np.linalg.inv(information)
    values = derived(parameters, direction)
    delta = numeric_jacobian(lambda point: derived(point, direction), parameters)
    errors = np.sqrt(np.maximum(np.diag(delta @ parameter_covariance @ delta.T), 0))
    quantities = {}
    for name, estimate, error in zip(["path", "exogenous_variance", "disturbance_variance", "endogenous_variance", "path_std", "R2"], values, errors):
        quantities[name] = {"estimate": float(estimate), "se_delta": float(error),
                            "wald_ci95": (estimate + np.array([-1, 1]) * stats.norm.ppf(.975) * error).tolist()}
    if direction != "zero":
        transformed = np.arctanh(values[4])
        gradient = numeric_jacobian(lambda point: np.asarray(np.arctanh(derived(point, direction)[4])), parameters)
        error = np.sqrt(gradient @ parameter_covariance @ gradient)
        interval = np.tanh(transformed + np.array([-1, 1]) * stats.norm.ppf(.975) * error)
        quantities["path_std"]["transformed_ci95"] = interval.tolist()
        quantities["R2"]["transformed_ci95"] = [0. if interval[0] <= 0 <= interval[1] else float(np.min(interval ** 2)), float(np.max(interval ** 2))]
        quantities["path"]["wald_p"] = float(2 * stats.norm.sf(abs(values[0] / errors[0])))
    score = objective(parameters, sample, direction)[0]
    eigenvalues = linalg.eigvalsh(sample, covariance)
    np.testing.assert_allclose(score, np.sum(eigenvalues - np.log(eigenvalues) - 1), atol=1e-10)
    statistic = (observations - 1) * score
    degrees = 55 - len(parameters)
    baseline = (observations - 1) * (np.linalg.slogdet(np.diag(np.diag(sample)))[1] - np.linalg.slogdet(sample)[1])
    residual = (sample - covariance) / np.sqrt(np.outer(sample.diagonal(), sample.diagonal()))
    standardized_loads = loadings * np.sqrt(np.diag(latent))[None, :] / np.sqrt(np.diag(covariance))[:, None]
    item_rows = [{"item": name, "loading": float(loadings[row, FACTOR_INDEX[row]]),
                  "loading_std": float(standardized_loads[row, FACTOR_INDEX[row]]),
                  "theta": float(theta[row]), "R2_item": float(1 - theta[row] / covariance[row, row])}
                 for row, name in enumerate(NAMES)]
    info = {"direction": direction, "free_parameters": len(parameters), "df": degrees,
            "F_ML": float(score), "chi2": float(statistic), "chi2_p": float(stats.chi2.sf(statistic, degrees)),
            "CFI": float(1 - max(statistic - degrees, 0) / max(statistic - degrees, baseline - 45, 0)),
            "TLI": float((baseline / 45 - statistic / degrees) / (baseline / 45 - 1)),
            "RMSEA": float(np.sqrt(max((statistic - degrees) / (observations * degrees), 0))),
            "RMSEA_ci90": rmsea_interval(statistic, degrees, observations),
            "SRMR": float(np.sqrt(np.mean(residual[lower_indices] ** 2))),
            "baseline_chi2": float(baseline), "baseline_df": 45,
            "AIC_star": float(statistic + 2 * len(parameters)),
            "BIC_star": float(statistic + len(parameters) * np.log(observations)),
            "quantities": quantities, "latent_covariance": latent.tolist(), "items": item_rows,
            "jacobian_rank": rank, "gradient_max": float(np.max(np.abs(alternate.jac))),
            "minimum_theta": float(theta.min()), "minimum_information_eigenvalue": float(np.linalg.eigvalsh(information)[0]),
            "start_objectives": [float(run.fun) for run in runs], "alternate_success": bool(alternate.success)}
    return info, covariance, residual, parameters


def main():
    directory = Path(__file__).resolve().parent
    source = directory / "bfi-ilk100-AC.csv"
    original = source.read_bytes()
    normalized = original.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    assert hashlib.sha256(normalized).hexdigest() == SOURCE_HASH, "Yerel kaynak değişmiş; kaynak ve kitap sonuçlarını birlikte denetleyin."
    data = pd.read_csv(source)
    assert list(data.columns) == ["kaynak_satir", "kaynak_kayit"] + NAMES
    assert len(data) == 100 and not data.kaynak_satir.duplicated().any()
    np.testing.assert_array_equal(data.kaynak_satir, np.arange(1, 101))
    observed = data[NAMES].stack().to_numpy()
    assert np.isin(observed, np.arange(1, 7)).all()
    complete = data[NAMES].notna().all(axis=1)
    excluded = data.loc[~complete, "kaynak_satir"].tolist()
    assert excluded == [63, 66, 90]
    keyed = data.loc[complete, NAMES].copy()
    for item in ["A1", "C4", "C5"]:
        keyed[item] = 7 - keyed[item]
    standardized = (keyed - keyed.mean()) / keyed.std(ddof=1)
    sample = np.cov(standardized.to_numpy(), rowvar=False, ddof=1)
    assert len(keyed) == 97 and np.linalg.eigvalsh(sample)[0] > 0
    np.testing.assert_allclose(np.diag(sample), 1., atol=1e-10)
    spec = importlib.util.spec_from_file_location("b15_reference", directory / "dfa_referans.py")
    reference = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reference)
    cfa_info, cfa_covariance, _, _ = reference.fit(sample, len(keyed), "correlated")
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    data.loc[complete, ["kaynak_satir", "kaynak_kayit"]].join(keyed).to_csv(output / "puanlanmis.csv", index=False)
    data.loc[complete, ["kaynak_satir", "kaynak_kayit"]].join(standardized).to_csv(output / "standartlastirilmis.csv", index=False)
    pd.DataFrame(sample, index=NAMES, columns=NAMES).to_csv(output / "orneklem_kovaryans.csv")
    results = {}
    covariances = {}
    for direction in ["forward", "reverse", "zero"]:
        initial = initial_from_cfa(cfa_info, direction)
        if direction != "zero":
            np.testing.assert_allclose(decode(initial, direction)[3], cfa_covariance, atol=1e-9)
        info, covariance, residual, parameters = fit(sample, len(keyed), direction, initial, reference.rmsea_interval)
        results[direction] = info
        covariances[direction] = covariance
        pd.DataFrame(covariance, index=NAMES, columns=NAMES).to_csv(output / f"{direction}_kovaryans.csv")
        pd.DataFrame(residual, index=NAMES, columns=NAMES).to_csv(output / f"{direction}_artik.csv")
        pd.DataFrame(info["items"]).to_csv(output / f"{direction}_yukler.csv", index=False)
        if direction != "zero":
            np.testing.assert_allclose(covariance, cfa_covariance, atol=2e-6)
            np.testing.assert_allclose(info["chi2"], cfa_info["chi2"], atol=1e-6)
            np.testing.assert_allclose(info["quantities"]["path_std"]["estimate"], cfa_info["phi"], atol=2e-6)
    forward = results["forward"]
    reverse = results["reverse"]
    np.testing.assert_allclose(covariances["forward"], covariances["reverse"], atol=2e-6)
    difference = results["zero"]["chi2"] - forward["chi2"]
    assert difference >= 0 and results["zero"]["df"] - forward["df"] == 1
    summary = {"n": len(keyed), "source": source.name,
               "source_normalized_sha256": SOURCE_HASH, "source_raw_sha256": hashlib.sha256(original).hexdigest(),
               "excluded_source_rows": excluded, "official_source_automatically_verified": False,
               "estimator": "normal-theory covariance ML, Wishart n-1, ddof=1 standardized indicators, no means",
               "executed": {"Python": True, "R_lavaan": False, "AMOS": False},
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__, "matplotlib": matplotlib.__version__},
               "models": results, "cfa_reference": {key: cfa_info[key] for key in ["chi2", "df", "phi", "phi_ci95"]},
               "zero_path_LR": {"chi2_difference": float(difference), "df_difference": 1,
                                "nominal_p": float(stats.chi2.sf(difference, 1))},
               "equivalence_max_abs_covariance_difference": float(np.max(np.abs(covariances["forward"] - covariances["reverse"]))),
               "hypothetical_mediation": {"a": .48, "b": .41, "c_prime": .19, "ab": .48 * .41,
                                         "total": .19 + .48 * .41, "estimated_from_real_data": False},
               "checks": ["source hash", "keying and complete records", "analytic vs numerical derivatives",
                          "three starts and two optimizers", "local Jacobian rank", "positive expected information",
                          "information vs numerical expected Hessian", "objective vs generalized eigenvalues",
                          "CFA-to-SEM scaling", "forward-reverse covariance equality", "standardized path equals CFA correlation"]}
    pd.DataFrame([{key: results[direction][key] for key in ["direction", "free_parameters", "df", "chi2", "chi2_p", "CFI", "TLI", "RMSEA", "SRMR", "AIC_star", "BIC_star"]}
                  for direction in results]).to_csv(output / "uyum.csv", index=False)
    rows = []
    for direction, info in results.items():
        for quantity, values in info["quantities"].items():
            rows.append({"direction": direction, "quantity": quantity, "estimate": values["estimate"],
                         "se_delta": values["se_delta"], "wald_lower": values["wald_ci95"][0],
                         "wald_upper": values["wald_ci95"][1]})
    pd.DataFrame(rows).to_csv(output / "yapisal_parametreler.csv", index=False)
    figure, axes = plt.subplots(1, 2, figsize=(7.2, 3.6), constrained_layout=True)
    plt.rcParams.update({"font.size": 10})
    locations = np.arange(10)
    axes[0].bar(locations, [item["loading_std"] for item in forward["items"]], color=["#781e2d"] * 5 + ["#2571b5"] * 5)
    axes[0].set(xticks=locations, xticklabels=NAMES, ylabel="Standartlaştırılmış yük", ylim=(0, 1))
    residual = sample - covariances["forward"]
    image = axes[1].imshow(residual, vmin=-.2, vmax=.2, cmap="RdBu_r")
    axes[1].set(xticks=locations, yticks=locations, xticklabels=NAMES, yticklabels=NAMES,
                title="S − model kovaryansı")
    axes[1].tick_params(axis="x", labelrotation=90)
    figure.colorbar(image, ax=axes[1], fraction=.046, pad=.04)
    figure_directory = directory / "grafikler"
    figure_directory.mkdir(exist_ok=True)
    figure.savefig(figure_directory / "b16-yukler-artiklar.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source.read_bytes() == original
    (output / "ozet.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"forward": forward["quantities"], "reverse": reverse["quantities"],
                      "fit": {name: info["chi2"] for name, info in results.items()}, "LR": summary["zero_path_LR"]},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()