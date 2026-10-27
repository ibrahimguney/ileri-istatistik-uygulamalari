"""Bölüm 21: ölçüm modelinden yapısal modele (yarım B, n = 1316).

Küçük bir RAM (reticular action model) motoru: Sigma = F (I-A)^-1 S (I-A)^-T F'.
Normal kuramlı kovaryans ML, Wishart (n-1) çarpanı, ortalama yapısı yok.
Genel amaçlı SEM yazılımı değildir; kitap örneklerini denetlenebilir kılar.
"""
import hashlib
import importlib.util
import json
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import linalg, optimize, stats

SOURCE_HASH = "6b3a399dd3aea61ab94252d81660f2c759bbf17d6084204f66a66b25da43b989"
ITEMS = [f"{prefix}{number}" for prefix in ["A", "C"] for number in range(1, 6)]
RESIDUAL_PAIRS = [("A1", "A2"), ("C1", "C2"), ("C4", "C5")]  # Bölüm 19'daki M2
BOOTSTRAP_SEED = 20261701
BOOTSTRAP_DRAWS = 2000


class Model:
    """Serbest parametreleri (matris, satır, sütun, dönüşüm) listesiyle tanımlanan RAM modeli."""

    def __init__(self, name, observed, specification, fixed):
        self.name = name
        self.observed = observed
        self.variables = observed + ["A", "C"]
        self.index = {name: position for position, name in enumerate(self.variables)}
        self.size = len(self.variables)
        self.parameters = specification  # [(etiket, "A"|"S", satır, sütun, "log"|"lin")]
        self.fixed = fixed  # [("A"|"S", satır, sütun, değer)]
        self.selection = np.zeros((len(observed), self.size))
        self.selection[np.arange(len(observed)), np.arange(len(observed))] = 1

    def matrices(self, values):
        paths = np.zeros((self.size, self.size))
        symmetric = np.zeros((self.size, self.size))
        for matrix, row, column, value in self.fixed:
            target = paths if matrix == "A" else symmetric
            target[self.index[row], self.index[column]] = value
            if matrix == "S":
                target[self.index[column], self.index[row]] = value
        for (label, matrix, row, column, transform), value in zip(self.parameters, values):
            value = np.exp(value) if transform == "log" else value
            target = paths if matrix == "A" else symmetric
            target[self.index[row], self.index[column]] = value
            if matrix == "S":
                target[self.index[column], self.index[row]] = value
        inverse = np.linalg.inv(np.eye(self.size) - paths)
        full = inverse @ symmetric @ inverse.T
        return paths, symmetric, inverse, full

    def covariance(self, values):
        return self.selection @ self.matrices(values)[3] @ self.selection.T

    def derivatives(self, values):
        _, _, inverse, full = self.matrices(values)
        result = []
        for (label, matrix, row, column, transform), value in zip(self.parameters, values):
            unit = np.zeros((self.size, self.size))
            unit[self.index[row], self.index[column]] = 1
            if matrix == "A":
                change = inverse @ unit @ full
                change = change + change.T
            else:
                if row != column:
                    unit[self.index[column], self.index[row]] = 1
                change = inverse @ unit @ inverse.T
            if transform == "log":
                change = change * np.exp(value)
            result.append(self.selection @ change @ self.selection.T)
        return np.asarray(result)

    def labels(self):
        return [item[0] for item in self.parameters]


def objective(values, sample, model):
    covariance = model.covariance(values)
    sign, logdet = np.linalg.slogdet(covariance)
    if sign <= 0:
        return 1e10, np.zeros(len(values))
    inverse = np.linalg.inv(covariance)
    value = logdet + np.trace(sample @ inverse) - np.linalg.slogdet(sample)[1] - len(sample)
    gradient = np.einsum("ij,kji->k", inverse - inverse @ sample @ inverse, model.derivatives(values))
    return float(value), gradient


def numeric_jacobian(function, point, step=1e-5):
    columns = []
    for position in range(len(point)):
        shift = np.zeros(len(point))
        shift[position] = step
        columns.append((np.asarray(function(point + shift)) - np.asarray(function(point - shift))) / (2 * step))
    return np.stack(columns, axis=-1)


def measurement(observed, extra_parameters, extra_fixed):
    specification, fixed = [], [("A", "A1", "A", 1.0), ("A", "C1", "C", 1.0)]
    for item in ITEMS:
        if item not in ("A1", "C1"):
            specification.append((f"{item[0]}=~{item}", "A", item, item[0], "lin"))
    for item in ITEMS:
        specification.append((f"{item}~~{item}", "S", item, item, "log"))
    for first, second in RESIDUAL_PAIRS:
        specification.append((f"{first}~~{second}", "S", first, second, "lin"))
    return specification + extra_parameters, fixed + extra_fixed


def build_models():
    items = list(ITEMS)
    models = {}
    spec, fixed = measurement(items, [("A~~A", "S", "A", "A", "log"), ("C~~C", "S", "C", "C", "log"),
                                      ("C~A", "A", "C", "A", "lin")], [])
    models["forward"] = Model("forward", items, spec, fixed)
    spec, fixed = measurement(items, [("C~~C", "S", "C", "C", "log"), ("A~~A", "S", "A", "A", "log"),
                                      ("A~C", "A", "A", "C", "lin")], [])
    models["reverse"] = Model("reverse", items, spec, fixed)
    spec, fixed = measurement(items, [("A~~A", "S", "A", "A", "log"), ("C~~C", "S", "C", "C", "log")], [])
    models["zero"] = Model("zero", items, spec, fixed)
    observed = items + ["K"]
    spec, fixed = measurement(observed, [("K~~K", "S", "K", "K", "log"), ("A~~A", "S", "A", "A", "log"),
                                         ("C~~C", "S", "C", "C", "log"), ("A~K", "A", "A", "K", "lin"),
                                         ("C~A", "A", "C", "A", "lin"), ("C~K", "A", "C", "K", "lin")], [])
    models["mediation"] = Model("mediation", observed, spec, fixed)
    return models


def starting_values(model, sample):
    values = []
    for label, matrix, row, column, transform in model.parameters:
        if label == "K~~K":
            values.append(np.log(sample[-1, -1]))
        elif label in ("A~~A", "C~~C"):
            values.append(np.log(.3))
        elif transform == "log":
            values.append(np.log(.6))
        elif matrix == "A" and "=~" in label:
            values.append(1.0)
        else:
            values.append(0.0)
    return np.asarray(values)


def minimize(model, sample, start, tolerance=1e-9):
    bounds = [(-12, 4) if item[4] == "log" else (-10, 10) for item in model.parameters]
    result = optimize.minimize(objective, start, args=(sample, model), jac=True, method="L-BFGS-B",
                               bounds=bounds, options={"ftol": 1e-15, "gtol": tolerance, "maxiter": 5000})
    return result


def rmsea_interval(statistic, degrees, observations):
    roots = []
    for target in [.95, .05]:
        if stats.ncx2.cdf(statistic, degrees, 0) <= target:
            root = 0.0
        else:
            upper = max(statistic, 1.0)
            while stats.ncx2.cdf(statistic, degrees, upper) > target:
                upper *= 2
            root = optimize.brentq(lambda value: stats.ncx2.cdf(statistic, degrees, value) - target, 0, upper)
        roots.append(float(np.sqrt(root / (observations * degrees))))
    return roots


def derived(model, values):
    """Yapısal büyüklükler: ham yollar, gizil varyanslar ve std.nox (gizilleri standartlaştırılmış) ölçek."""
    paths, _, _, full = model.matrices(values)
    index = model.index
    variance_a, variance_c = full[index["A"], index["A"]], full[index["C"], index["C"]]
    result = {"Var_A": variance_a, "Var_C": variance_c}
    if model.name in ("forward", "reverse", "zero"):
        covariance = full[index["A"], index["C"]]
        result["latent_correlation"] = covariance / np.sqrt(variance_a * variance_c)
    if model.name == "forward":
        gamma = paths[index["C"], index["A"]]
        result.update({"gamma": gamma, "beta_std": gamma * np.sqrt(variance_a / variance_c),
                       "R2_C": gamma ** 2 * variance_a / variance_c})
    if model.name == "reverse":
        delta = paths[index["A"], index["C"]]
        result.update({"delta": delta, "beta_std": delta * np.sqrt(variance_c / variance_a),
                       "R2_A": delta ** 2 * variance_c / variance_a})
    if model.name == "mediation":
        a, b, c = paths[index["A"], index["K"]], paths[index["C"], index["A"]], paths[index["C"], index["K"]]
        sd_a, sd_c = np.sqrt(variance_a), np.sqrt(variance_c)
        result.update({"a": a, "b": b, "c_prime": c, "indirect": a * b, "total": c + a * b,
                       "a_stdnox": a / sd_a, "b_std": b * sd_a / sd_c, "c_prime_stdnox": c / sd_c,
                       "indirect_stdnox": a * b / sd_c, "total_stdnox": (c + a * b) / sd_c,
                       "R2_A": a ** 2 * full[index["K"], index["K"]] / variance_a,
                       "R2_C": 1 - np.exp(values[model.labels().index("C~~C")]) / variance_c})
    return result


def fit(model, sample, observations, start=None):
    start = starting_values(model, sample) if start is None else start
    starts = [start]
    for loading_scale, log_shift in [(.8, -.2), (1.25, .2)]:  # belirlenimci alternatif başlangıçlar
        alternative = start.copy()
        for position, (label, matrix, row, column, transform) in enumerate(model.parameters):
            if "=~" in label:
                alternative[position] *= loading_scale
            elif transform == "log" and label != "K~~K":
                alternative[position] += log_shift
        starts.append(alternative)
    runs = []
    for position, point in enumerate(starts):
        if position == 0:
            numerical = numeric_jacobian(lambda value: objective(value, sample, model)[0], point)
            np.testing.assert_allclose(objective(point, sample, model)[1], numerical, atol=1e-6)
        result = minimize(model, sample, point)
        if np.max(np.abs(result.jac)) > 2e-5:
            raise RuntimeError(f"Başlangıç yakınsamadı: {model.name}: {result.message}")
        runs.append(result)
    best = min(runs, key=lambda run: run.fun)
    np.testing.assert_allclose([run.fun for run in runs], best.fun, atol=1e-9)
    alternate = optimize.minimize(objective, best.x, args=(sample, model), jac=True, method="BFGS",
                                  options={"gtol": 1e-8, "maxiter": 5000})
    if np.max(np.abs(alternate.jac)) > 1e-6:
        raise RuntimeError("İkinci optimizasyonda gradyan büyük.")
    np.testing.assert_allclose(alternate.fun, best.fun, atol=1e-9)
    values = alternate.x
    covariance = model.covariance(values)
    np.testing.assert_allclose(covariance, model.covariance(best.x), atol=2e-6)
    changes = model.derivatives(values)
    p = len(model.observed)
    lower = np.tril_indices(p)
    jacobian = changes[:, lower[0], lower[1]].T
    np.testing.assert_allclose(jacobian, numeric_jacobian(lambda value: model.covariance(value)[lower], values), atol=1e-6)
    rank = int(np.linalg.matrix_rank(jacobian))
    assert rank == len(values), "Yerel tanımlanabilirlik denetimi başarısız."
    inverse = np.linalg.inv(covariance)
    weighted = np.einsum("ij,kjl->kil", inverse, changes)
    information = (observations - 1) / 2 * np.einsum("aij,bji->ab", weighted, weighted)
    assert np.linalg.eigvalsh(information)[0] > 0
    parameter_covariance = np.linalg.inv(information)
    score = objective(values, sample, model)[0]
    eigenvalues = linalg.eigvalsh(sample, covariance)
    np.testing.assert_allclose(score, np.sum(eigenvalues - np.log(eigenvalues) - 1), atol=1e-10)
    statistic = (observations - 1) * score
    moments = p * (p + 1) // 2
    degrees = moments - len(values)
    baseline_df = p * (p - 1) // 2
    baseline = (observations - 1) * (np.sum(np.log(np.diag(sample))) - np.linalg.slogdet(sample)[1])
    residual = (sample - covariance) / np.sqrt(np.outer(np.diag(sample), np.diag(sample)))
    quantities = derived(model, values)
    names = list(quantities)
    delta = numeric_jacobian(lambda value: np.array([derived(model, value)[name] for name in names]), values)
    errors = np.sqrt(np.maximum(np.diag(delta @ parameter_covariance @ delta.T), 0))
    quantity_rows = {name: {"estimate": float(quantities[name]), "se_delta": float(error),
                            "wald_ci95": (quantities[name] + np.array([-1, 1]) * stats.norm.ppf(.975) * error).tolist(),
                            "z": float(quantities[name] / error) if error > 0 else None}
                     for name, error in zip(names, errors)}
    paths, symmetric, _, full = model.matrices(values)
    items = []
    for item in ITEMS:
        factor = item[0]
        loading = paths[model.index[item], model.index[factor]]
        std = loading * np.sqrt(full[model.index[factor], model.index[factor]] / covariance[model.index[item], model.index[item]])
        items.append({"item": item, "loading_marker": float(loading), "loading_std": float(std),
                      "theta": float(symmetric[model.index[item], model.index[item]]), "R2_item": float(std ** 2)})
    raw_errors = np.sqrt(np.diag(parameter_covariance))
    parameters = [{"parameter": label, "value": float(np.exp(value) if spec[4] == "log" else value),
                   "se": float(np.exp(value) * error if spec[4] == "log" else error)}
                  for label, value, error, spec in zip(model.labels(), values, raw_errors, model.parameters)]
    upper = np.triu_indices(p, 1)
    info = {"model": model.name, "observed": model.observed, "free_parameters": len(values), "moments": moments,
            "df": degrees, "F_ML": float(score), "chi2": float(statistic), "p": float(stats.chi2.sf(statistic, degrees)),
            "CFI": float(1 - max(statistic - degrees, 0) / max(statistic - degrees, baseline - baseline_df, 0)),
            "TLI": float((baseline / baseline_df - statistic / degrees) / (baseline / baseline_df - 1)),
            "RMSEA": float(np.sqrt(max((statistic - degrees) / (observations * degrees), 0))),
            "RMSEA_ci90": rmsea_interval(statistic, degrees, observations),
            "SRMR": float(np.sqrt(np.mean(residual[lower] ** 2))), "max_abs_residual": float(np.max(np.abs(residual[upper]))),
            "baseline_chi2": float(baseline), "baseline_df": baseline_df,
            "AIC_star": float(statistic + 2 * len(values)), "BIC_star": float(statistic + len(values) * np.log(observations)),
            "quantities": quantity_rows, "items": items, "parameters": parameters, "jacobian_rank": rank,
            "gradient_max": float(np.max(np.abs(alternate.jac))),
            "minimum_information_eigenvalue": float(np.linalg.eigvalsh(information)[0])}
    return info, values, covariance, residual


def standardized_sample(frame):
    keyed = frame[ITEMS].astype(float)
    z = (keyed - keyed.mean()) / keyed.std(ddof=1)
    return z


def main():
    directory = Path(__file__).parent
    source = directory.parent / "b18-faktor-analizi/yarim_B.csv"
    original = source.read_bytes()
    assert hashlib.sha256(original.rstrip(b"\n") + b"\n").hexdigest() == SOURCE_HASH, \
        "Önce Bölüm 18 betiğini çalıştırın: yarim_B.csv beklenen dosya değil."
    data = pd.read_csv(source)
    assert len(data) == 1316 and not data[ITEMS + ["gender"]].isna().any().any()
    assert data[ITEMS].isin(range(1, 7)).all().all() and set(data["gender"]) == {1, 2}
    keyed = data[ITEMS].astype(int).copy()
    for item in ["A1", "C4", "C5"]:
        keyed[item] = 7 - keyed[item]
    women = (data["gender"] == 2).astype(int).rename("K")  # kaynak kodlaması: 1 erkek, 2 kadın
    z = standardized_sample(keyed)
    matrix = np.column_stack([z.to_numpy(), women.to_numpy()])
    sample_all = np.cov(matrix, rowvar=False, ddof=1)
    sample_items = sample_all[:10, :10]
    np.testing.assert_allclose(np.diag(sample_items), 1., atol=1e-12)
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    for stale in ["standartlastirilmis.csv"]:
        (directory / stale).unlink(missing_ok=True)
    frame = data[["kaynak_satir", "kaynak_kayit"]].join(keyed).join(women)
    frame.to_csv(directory / "puanlanmis.csv", index=False)
    data[["kaynak_satir", "kaynak_kayit"]].join(z.round(12)).join(women).to_csv(directory / "standartlastirilmis.csv", index=False)
    pd.DataFrame(sample_all, index=ITEMS + ["K"], columns=ITEMS + ["K"]).to_csv(output / "orneklem_kovaryans.csv")

    models = build_models()
    results, values, covariances = {}, {}, {}
    for name, model in models.items():
        sample = sample_all if name == "mediation" else sample_items
        info, estimate, covariance, residual = fit(model, sample, len(data))
        results[name], values[name], covariances[name] = info, estimate, covariance
        labels = model.observed
        pd.DataFrame(covariance, index=labels, columns=labels).to_csv(output / f"{name}_kovaryans.csv")
        pd.DataFrame(residual, index=labels, columns=labels).to_csv(output / f"{name}_artik.csv")
        pd.DataFrame(info["items"]).to_csv(output / f"{name}_yukler.csv", index=False)
        pd.DataFrame(info["parameters"]).to_csv(output / f"{name}_parametreler.csv", index=False)

    # Denetimler: ileri/ters eşdeğerlik ve Bölüm 19 M2 ile aynı kovaryans.
    np.testing.assert_allclose(covariances["forward"], covariances["reverse"], atol=2e-6)
    np.testing.assert_allclose(results["forward"]["chi2"], results["reverse"]["chi2"], atol=1e-6)
    spec = importlib.util.spec_from_file_location("b16_reference", directory.parent / "b19-dogrulayici-faktor/analiz.py")
    reference = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reference)
    cfa_info, cfa_covariance, _, _ = reference.fit(sample_items, len(data), "resid_cov")
    np.testing.assert_allclose(covariances["forward"], cfa_covariance, atol=2e-6)
    np.testing.assert_allclose(results["forward"]["chi2"], cfa_info["chi2"], atol=1e-6)
    np.testing.assert_allclose(results["forward"]["quantities"]["beta_std"]["estimate"], cfa_info["phi"], atol=2e-6)
    difference = results["zero"]["chi2"] - results["forward"]["chi2"]
    assert difference >= 0 and results["zero"]["df"] - results["forward"]["df"] == 1

    # Aracılık: kişiler yeniden örneklenir, her çekilişte maddeler yeniden standartlaştırılır ve bütün SEM yeniden kestirilir.
    mediation = models["mediation"]
    generator = np.random.default_rng(BOOTSTRAP_SEED)
    draws, failures = [], 0
    started = time.time()
    raw = np.column_stack([keyed.to_numpy(float), women.to_numpy(float)])
    for _ in range(BOOTSTRAP_DRAWS):
        rows = generator.integers(0, len(raw), len(raw))
        sample_raw = raw[rows]
        items = sample_raw[:, :10]
        standardized = (items - items.mean(0)) / items.std(0, ddof=1)
        boot = np.cov(np.column_stack([standardized, sample_raw[:, 10]]), rowvar=False, ddof=1)
        result = minimize(mediation, boot, values["mediation"], tolerance=1e-8)
        if np.max(np.abs(result.jac)) > 1e-5 or not np.isfinite(result.fun):
            failures += 1
            continue
        quantities = derived(mediation, result.x)
        draws.append([quantities[name] for name in ["a", "b", "c_prime", "indirect", "total",
                                                    "indirect_stdnox", "total_stdnox", "c_prime_stdnox"]])
    draws = np.asarray(draws)
    boot_names = ["a", "b", "c_prime", "indirect", "total", "indirect_stdnox", "total_stdnox", "c_prime_stdnox"]
    bootstrap = {"seed": BOOTSTRAP_SEED, "draws_requested": BOOTSTRAP_DRAWS, "draws_used": int(len(draws)),
                 "nonconverged": failures, "unit": "person (row) resampling; items re-standardized within each draw",
                 "interval": "percentile 2.5/97.5 (numpy linear)", "seconds": round(time.time() - started, 1),
                 "quantities": {name: {"estimate": results["mediation"]["quantities"][name]["estimate"],
                                       "bootstrap_se": float(draws[:, position].std(ddof=1)),
                                       "percentile_ci95": np.percentile(draws[:, position], [2.5, 97.5]).tolist()}
                                for position, name in enumerate(boot_names)}}
    pd.DataFrame(draws, columns=boot_names).to_csv(output / "bootstrap_cekilisler.csv", index=False)

    group = pd.DataFrame({"K": women, "A_ort": keyed[ITEMS[:5]].mean(axis=1), "C_ort": keyed[ITEMS[5:]].mean(axis=1)})
    descriptives = {"n": int(len(data)), "women": int(women.sum()), "men": int((1 - women).sum()),
                    "women_share": float(women.mean()),
                    "item_mean_scores_by_group": group.groupby("K")[["A_ort", "C_ort"]].mean().round(6).to_dict(),
                    "corr_K_Amean": float(np.corrcoef(group.K, group.A_ort)[0, 1]),
                    "corr_K_Cmean": float(np.corrcoef(group.K, group.C_ort)[0, 1])}
    summary = {"source": "../b18-faktor-analizi/yarim_B.csv (Bölüm 18 yarım B; AFA'da kullanılmadı)",
               "source_normalized_sha256": SOURCE_HASH, "source_raw_sha256": hashlib.sha256(original).hexdigest(),
               "estimator": "normal-theory covariance ML, Wishart n-1, ddof=1 standardized items, K = 1 kadın / 0 erkek (ham), no means",
               "measurement_model": "Bölüm 19 M2: iki faktör, marker A1/C1, hata kovaryansları A1-A2, C1-C2, C4-C5",
               "descriptives": descriptives, "models": results,
               "zero_path_LR": {"chi2_difference": float(difference), "df_difference": 1,
                                "p": float(stats.chi2.sf(difference, 1))},
               "equivalence_max_abs_covariance_difference": float(np.max(np.abs(covariances["forward"] - covariances["reverse"]))),
               "cfa_reference": {"chi2": cfa_info["chi2"], "df": cfa_info["df"], "phi": cfa_info["phi"]},
               "bootstrap": bootstrap,
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__,
                            "matplotlib": matplotlib.__version__},
               "checks": ["source hash", "analytic vs numerical derivatives", "three starts and two optimizers",
                          "local Jacobian rank", "positive expected information", "objective vs generalized eigenvalues",
                          "forward-reverse covariance equality", "SEM equals Chapter 16 M2 CFA", "bootstrap convergence count"]}
    (output / "ozet.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    pd.DataFrame([{key: results[name][key] for key in ["model", "free_parameters", "df", "chi2", "p", "CFI", "TLI",
                                                         "RMSEA", "SRMR", "AIC_star", "BIC_star"]} for name in results]
                 ).to_csv(output / "uyum.csv", index=False)

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(7.2, 3.6), constrained_layout=True)
    locations = np.arange(10)
    axes[0].bar(locations, [item["loading_std"] for item in results["forward"]["items"]],
                color=["#781e2d"] * 5 + ["#3c3c41"] * 5)
    axes[0].set(xticks=locations, xticklabels=ITEMS, ylabel="Standartlaştırılmış yük", ylim=(0, 1),
                title="İleri model: standart yükler")
    image = axes[1].imshow(sample_items - covariances["forward"], vmin=-.2, vmax=.2, cmap="RdBu_r")
    axes[1].set(xticks=locations, yticks=locations, xticklabels=ITEMS, yticklabels=ITEMS,
                title="S − model kovaryansı")
    axes[1].tick_params(axis="x", labelrotation=90)
    figure.colorbar(image, ax=axes[1], fraction=.046, pad=.04)
    figures = directory.parent.parent / "assets_figures"
    figures.mkdir(exist_ok=True)
    figure.savefig(figures / "b16-yukler-artiklar.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(6.4, 3.4), constrained_layout=True)
    column = boot_names.index("indirect_stdnox")
    axis.hist(draws[:, column], bins=50, color="#781e2d", alpha=.85)
    for value in bootstrap["quantities"]["indirect_stdnox"]["percentile_ci95"]:
        axis.axvline(value, color="#3c3c41", linestyle="--", linewidth=1)
    axis.axvline(0, color="gray", linewidth=.8)
    axis.set(xlabel="Dolaylı etki K → A → C (C'nin standart sapması birimiyle)", ylabel="Çekiliş sayısı",
             title=f"Kişi yeniden örneklemesi, {len(draws)} çekiliş; kesikli çizgiler %95 yüzdelik aralık")
    figure.savefig(figures / "b16-dolayli-bootstrap.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source.read_bytes() == original
    print(json.dumps({"fit": {name: [round(info["chi2"], 3), info["df"], round(info["CFI"], 3), round(info["RMSEA"], 3)]
                              for name, info in results.items()},
                      "mediation": {name: round(row["estimate"], 4) for name, row in results["mediation"]["quantities"].items()},
                      "bootstrap": {name: [round(x, 4) for x in row["percentile_ci95"]] for name, row in bootstrap["quantities"].items()},
                      "failures": failures, "seconds": bootstrap["seconds"]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
