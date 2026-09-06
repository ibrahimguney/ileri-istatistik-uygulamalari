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
import statsmodels
from statsmodels.multivariate.factor import Factor
from statsmodels.multivariate.factor_rotation import rotate_factors

SOURCE_HASH = "8726fd25dbfc685be2d3d726e5511bbb31ba9c7b367b6864eb06e0d8669e6557"
SEED = 20261401
REPEATS = 2000


def smc(correlation):
    return 1 - 1 / np.diag(np.linalg.inv(correlation))


def spectrum(correlation, reduced=False):
    matrix = correlation.copy()
    if reduced:
        np.fill_diagonal(matrix, smc(correlation))
    return np.linalg.eigvalsh(matrix)[::-1]


def suitability(values):
    correlation = np.corrcoef(values, rowvar=False)
    inverse = np.linalg.inv(correlation)
    partial = -inverse / np.sqrt(np.outer(np.diag(inverse), np.diag(inverse)))
    np.fill_diagonal(partial, 0)
    off_diagonal = correlation - np.eye(len(correlation))
    squares = np.sum(off_diagonal ** 2, axis=0)
    partial_squares = np.sum(partial ** 2, axis=0)
    count = len(correlation)
    sign, logdet = np.linalg.slogdet(correlation)
    assert sign == 1 and spectrum(correlation)[-1] > 0
    statistic = -(len(values) - 1 - (2 * count + 5) / 6) * logdet
    degrees = count * (count - 1) // 2
    return correlation, partial, {"n": len(values), "k": count,
        "KMO": float(squares.sum() / (squares.sum() + partial_squares.sum())),
        "MSA": (squares / (squares + partial_squares)).tolist(),
        "determinant": float(np.exp(logdet)), "logdet": float(logdet),
        "Bartlett_chi2": float(statistic), "Bartlett_df": degrees,
        "Bartlett_p": float(stats.chi2.sf(statistic, degrees)),
        "correlation_square_sum": float(squares.sum()),
        "partial_square_sum": float(partial_squares.sum())}


def principal_axes(correlation, count):
    communalities = smc(correlation)
    for iteration in range(1, 2001):
        reduced = correlation.copy()
        np.fill_diagonal(reduced, communalities)
        eigenvalues, eigenvectors = np.linalg.eigh(reduced)
        chosen = np.argsort(eigenvalues)[::-1][:count]
        if np.any(eigenvalues[chosen] <= 0):
            raise ValueError("İstenen sayıda pozitif çıkarım özdeğeri yok.")
        loadings = eigenvectors[:, chosen] * np.sqrt(eigenvalues[chosen])
        updated = np.sum(loadings ** 2, axis=1)
        change = np.linalg.norm(updated - communalities)
        communalities = updated
        if change < 1e-10:
            break
    else:
        raise RuntimeError("PAF yakınsamadı; sonuç raporlanmadı.")
    independent = Factor(corr=correlation, n_factor=count, method="pa", smc=True).fit(maxiter=2000, tol=1e-10)
    np.testing.assert_allclose(loadings @ loadings.T, independent.loadings @ independent.loadings.T, atol=1e-8)
    common = loadings @ loadings.T
    residual = correlation - common - np.diag(1 - communalities)
    upper = np.triu_indices(len(correlation), 1)
    return loadings, {"factors": count, "iterations": iteration, "last_change": float(change),
        "communalities": communalities.tolist(), "uniquenesses": (1 - communalities).tolist(),
        "heywood": bool(np.any(communalities > 1) or np.any(communalities < 0)),
        "off_diagonal_RMSR": float(np.sqrt(np.mean(residual[upper] ** 2))),
        "max_abs_residual": float(np.max(np.abs(residual[upper]))),
        "residual_pairs_above_05": int(np.sum(np.abs(residual[upper]) > .05)),
        "common_variance_fraction": float(communalities.sum() / len(correlation))}


def parallel_analysis(values, seed):
    rng = np.random.default_rng(seed)
    component_draws, reduced_draws = [], []
    for iteration in range(REPEATS):
        permuted = np.column_stack([rng.permutation(values[:, column]) for column in range(values.shape[1])])
        if iteration == 0:
            np.testing.assert_array_equal(np.sort(permuted, axis=0), np.sort(values, axis=0))
        correlation = np.corrcoef(permuted, rowvar=False)
        component_draws.append(spectrum(correlation))
        reduced_draws.append(spectrum(correlation, reduced=True))
    correlation = np.corrcoef(values, rowvar=False)
    result = {}
    for label, samples, reduced in [("PCA", component_draws, False), ("SMC", reduced_draws, True)]:
        observed = spectrum(correlation, reduced=reduced)
        reference = np.quantile(samples, .95, axis=0, method="linear")
        exceed = observed > reference
        retained = int(np.cumprod(exceed).sum())
        result[label] = {"observed": observed.tolist(), "reference95": reference.tolist(),
                         "exceeds": exceed.tolist(), "consecutive_retained": retained}
    return result


def main():
    directory = Path(__file__).resolve().parent
    source_path = directory / "bfi-ilk100-AC.csv"
    source_bytes = source_path.read_bytes()
    assert hashlib.sha256(source_bytes.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n").hexdigest() == SOURCE_HASH, "Yerel kaynak değişmiş; kaynak ve kitap sonuçlarını birlikte denetleyin."
    source = pd.read_csv(source_path)
    names = [f"{scale}{number}" for scale in ["A", "C"] for number in range(1, 6)]
    np.testing.assert_array_equal(source.kaynak_satir, np.arange(1, 101))
    raw = source[names].dropna()
    data = raw.copy()
    for item in ["A1", "C4", "C5"]:
        data[item] = 7 - data[item]
    excluded = source.loc[~source.index.isin(data.index), "kaynak_satir"].tolist()
    assert len(data) == 97 and excluded == [63, 66, 90]
    assert np.isin(data.to_numpy(), np.arange(1, 7)).all()
    values = data.to_numpy(dtype=float)
    correlation, partial, checks = suitability(values)
    standardized = (values - values.mean(axis=0)) / values.std(axis=0, ddof=1)
    np.testing.assert_allclose(correlation, standardized.T @ standardized / (len(data) - 1))
    for position in range(len(names)):
        remaining = np.delete(standardized, position, axis=1)
        fitted = remaining @ np.linalg.lstsq(remaining, standardized[:, position], rcond=None)[0]
        manual_smc = 1 - np.sum((standardized[:, position] - fitted) ** 2) / np.sum(standardized[:, position] ** 2)
        np.testing.assert_allclose(manual_smc, smc(correlation)[position])
    first_other = standardized[:, 2:]
    first_residuals = standardized[:, :2] - first_other @ np.linalg.lstsq(first_other, standardized[:, :2], rcond=None)[0]
    np.testing.assert_allclose(np.corrcoef(first_residuals, rowvar=False)[0, 1], partial[0, 1])
    raw_correlation, _, raw_checks = suitability(raw.to_numpy())
    np.testing.assert_allclose([checks["KMO"], checks["Bartlett_chi2"]], [raw_checks["KMO"], raw_checks["Bartlett_chi2"]])
    np.testing.assert_allclose(spectrum(correlation), spectrum(raw_correlation))
    models = {}
    for count in [1, 2, 3]:
        unrotated, summary = principal_axes(correlation, count)
        models[str(count)] = summary
        if count == 2:
            main_loadings = unrotated
    pattern, transformation = rotate_factors(main_loadings, "quartimin", tol=1e-8, max_tries=10000)
    np.testing.assert_allclose(pattern, main_loadings @ np.linalg.inv(transformation.T))
    phi = transformation.T @ transformation
    a_column = int(np.argmax(np.sum(pattern[:5] ** 2, axis=0)))
    order = [a_column, 1 - a_column]
    pattern, phi = pattern[:, order], phi[np.ix_(order, order)]
    signs = np.array([np.sign(pattern[:5, 0].sum()), np.sign(pattern[5:, 1].sum())])
    pattern, phi = pattern * signs, phi * np.outer(signs, signs)
    structure = pattern @ phi
    common = pattern @ phi @ pattern.T
    np.testing.assert_allclose(np.diag(phi), 1, atol=1e-8)
    np.testing.assert_allclose(common, main_loadings @ main_loadings.T, atol=1e-8)
    derivative_free, derivative_transform = rotate_factors(main_loadings, "quartimin", algorithm="gpa_der_free", tol=1e-8, max_tries=10000)
    np.testing.assert_allclose(derivative_free @ derivative_transform.T @ derivative_transform @ derivative_free.T, common, atol=1e-7)
    objective = lambda loadings: float(np.sum(loadings[:, 0] ** 2 * loadings[:, 1] ** 2))
    np.testing.assert_allclose(objective(pattern), objective(derivative_free), atol=1e-7)
    orthogonal, orthogonal_transform = rotate_factors(main_loadings, "varimax", tol=1e-8, max_tries=10000)
    np.testing.assert_allclose(orthogonal_transform.T @ orthogonal_transform, np.eye(2), atol=1e-8)
    np.testing.assert_allclose(orthogonal @ orthogonal.T, common, atol=1e-8)
    reduced_no_weak = correlation[np.ix_([1, 2, 4, 5, 6, 7, 8, 9], [1, 2, 4, 5, 6, 7, 8, 9])]
    _, deletion = principal_axes(reduced_no_weak, 2)
    parallel = parallel_analysis(values, SEED)
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    source.loc[data.index, ["kaynak_satir", "kaynak_kayit"]].join(data).to_csv(output / "puanlanmis.csv", index=False)
    for name, matrix, columns in [("korelasyon", correlation, names), ("kismi_korelasyon", partial, names),
                                  ("oruntu", pattern, ["A", "C"]), ("yapi", structure, ["A", "C"]),
                                  ("yeniden_uretilen", common + np.diag(1 - np.diag(common)), names),
                                  ("artik", correlation - common - np.diag(1 - np.diag(common)), names)]:
        pd.DataFrame(matrix, index=names, columns=columns).to_csv(output / f"{name}.csv")
    pd.DataFrame(phi, index=["A", "C"], columns=["A", "C"]).to_csv(output / "faktor_korelasyon.csv")
    results = {"source_url": "https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/psych/bfi.csv",
               "source_normalized_sha256": SOURCE_HASH, "source_raw_sha256": hashlib.sha256(source_bytes).hexdigest(),
               "source_remote_automatic_comparison": False, "excluded_source_rows": excluded,
               "keys": ["A1", "C4", "C5"], "items": names, "suitability": checks,
               "initial_SMC": smc(correlation).tolist(), "models": models,
               "parallel": {"seed": SEED, "repeats": REPEATS, "method": "independent within-column permutations; linear 95th percentile", **parallel},
               "rotation": {"method": "quartimin, no Kaiser row normalization", "pattern": pattern.tolist(),
                            "structure": structure.tolist(), "phi": phi.tolist(), "objective": objective(pattern)},
               "drop_A1_A4_same_97_cases": deletion,
               "PCA_two_component_fraction": float(spectrum(correlation)[:2].sum() / 10),
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__, "statsmodels": statsmodels.__version__}}
    (output / "ozet.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.5), constrained_layout=True)
    positions = np.arange(1, 11)
    for axis, label in zip(axes, ["PCA", "SMC"]):
        axis.plot(positions, parallel[label]["observed"], "o-", color="#781e2d", label="Gözlenen")
        axis.plot(positions, parallel[label]["reference95"], "s--", color="#c49b5c", label="Permütasyon %95")
        axis.set(xlabel="Sıralı özdeğer", ylabel="Özdeğer", title=label + (": köşegen 1" if label == "PCA" else ": köşegen SMC"), xticks=[1, 3, 5, 7, 9])
        axis.axhline(0, color="gray", linewidth=.5)
        axis.legend(fontsize=8)
    figures = directory / "grafikler"
    figures.mkdir(exist_ok=True)
    figure.savefig(figures / "b14-paralel-analiz.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 4.0), constrained_layout=True)
    for axis, matrix, title in zip(axes, [pattern, structure], ["Örüntü", "Yapı"]):
        image = axis.imshow(matrix, cmap="RdBu_r", vmin=-1, vmax=1, aspect="auto")
        axis.set(yticks=np.arange(10), yticklabels=names, xticks=[0, 1], xticklabels=["A", "C"], title=title)
        for row in range(10):
            for column in range(2):
                axis.text(column, row, f"{matrix[row, column]:.2f}", ha="center", va="center", color="white" if abs(matrix[row, column]) > .6 else "black")
    figure.colorbar(image, ax=axes, shrink=.75)
    figure.savefig(figures / "b14-oruntu-yapi.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source_path.read_bytes() == source_bytes
    print(json.dumps(results, indent=2))
    print("Doğrulama başarılı: KMO/SMC, PAF, rotasyon, yeniden üretilen korelasyon ve paralel analiz.")


if __name__ == "__main__":
    main()