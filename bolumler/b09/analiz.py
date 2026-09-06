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

SOURCE_HASH = "b196e8c713269cd77736669c1e6cb3469f38f9fcfea9e23ec7a6a8b092daaafa"
BOOTSTRAP_SEED = 202610
BOOTSTRAP_REPLICATES = 5000


def load_data(path):
    payload = path.read_bytes()
    normalized = payload.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    if hashlib.sha256(normalized).hexdigest() != SOURCE_HASH:
        raise ValueError("Dondurulmuş simülasyon dosyasının hash'i uyuşmuyor.")
    data = pd.read_csv(path)
    assert list(data.columns) == ["kayit", "x", "araci", "w", "y_aracilik", "y_duzenleyicilik"]
    assert len(data) == 160 and np.isfinite(data.to_numpy()).all()
    np.testing.assert_array_equal(data.kayit, np.arange(1, 161))
    return data


def fit(response, matrix):
    if np.linalg.matrix_rank(matrix) != matrix.shape[1]:
        raise ValueError("Tasarım matrisi tam ranklı değil; sonuç üretilmedi.")
    model = sm.OLS(response, matrix, missing="raise").fit()
    np.testing.assert_allclose(model.params, np.linalg.lstsq(matrix, response, rcond=None)[0])
    return model


def paths(predictor, mediator, outcome):
    mediator_design = np.column_stack([np.ones(len(predictor)), predictor])
    outcome_design = np.column_stack([np.ones(len(predictor)), predictor, mediator])
    mediator_coefficients, _, mediator_rank, _ = np.linalg.lstsq(mediator_design, mediator, rcond=None)
    outcome_coefficients, _, outcome_rank, _ = np.linalg.lstsq(outcome_design, outcome, rcond=None)
    if mediator_rank != 2 or outcome_rank != 3:
        raise ValueError("Bootstrap örneği rank kaybetti; tekrar sessizce atlanmadı.")
    return float(mediator_coefficients[1]), float(outcome_coefficients[2])


def bootstrap_indirect(data, repeats=BOOTSTRAP_REPLICATES, seed=BOOTSTRAP_SEED):
    generator = np.random.default_rng(seed)
    values = data[["x", "araci", "y_aracilik"]].to_numpy()
    indirect = np.empty(repeats)
    for repeat in range(repeats):
        indices = generator.integers(0, len(values), size=len(values))
        sample = values[indices]
        path_a, path_b = paths(sample[:, 0], sample[:, 1], sample[:, 2])
        indirect[repeat] = path_a * path_b
        if repeat < 5:
            mediator_model = fit(sample[:, 1], np.column_stack([np.ones(len(sample)), sample[:, 0]]))
            outcome_model = fit(sample[:, 2], np.column_stack([np.ones(len(sample)), sample[:, 0], sample[:, 1]]))
            np.testing.assert_allclose(indirect[repeat], mediator_model.params[1] * outcome_model.params[2])
    if not np.isfinite(indirect).all():
        raise ValueError("Sonlu olmayan bootstrap sonucu; analiz durduruldu.")
    return indirect


def coefficient_table(model, names):
    intervals = np.asarray(model.conf_int())
    return {name: {"estimate": float(model.params[position]),
                   "se": float(model.bse[position]), "t": float(model.tvalues[position]),
                   "p": float(model.pvalues[position]), "ci95": intervals[position].tolist()}
            for position, name in enumerate(names)}


def analyze(data):
    predictor = data.x.to_numpy()
    mediator = data.araci.to_numpy()
    moderator = data.w.to_numpy()
    outcome = data.y_aracilik.to_numpy()
    basic_design = np.column_stack([np.ones(len(data)), predictor])
    mediator_model = fit(mediator, basic_design)
    total_model = fit(outcome, basic_design)
    outcome_model = fit(outcome, np.column_stack([np.ones(len(data)), predictor, mediator]))
    indirect = float(mediator_model.params[1] * outcome_model.params[2])
    direct = float(outcome_model.params[1])
    total = float(total_model.params[1])
    np.testing.assert_allclose(total, direct + indirect, rtol=1e-10, atol=1e-12)
    bootstrap = bootstrap_indirect(data)
    bootstrap_interval = np.quantile(bootstrap, [0.025, 0.975], method="linear")
    predictor_centered = predictor - predictor.mean()
    moderator_centered = moderator - moderator.mean()
    centered_design = np.column_stack([np.ones(len(data)), predictor_centered,
                                       moderator_centered, predictor_centered * moderator_centered])
    raw_design = np.column_stack([np.ones(len(data)), predictor, moderator, predictor * moderator])
    moderation = fit(data.y_duzenleyicilik.to_numpy(), centered_design)
    raw_moderation = fit(data.y_duzenleyicilik.to_numpy(), raw_design)
    np.testing.assert_allclose(moderation.fittedvalues, raw_moderation.fittedvalues, atol=1e-12)
    np.testing.assert_allclose(moderation.params[3], raw_moderation.params[3])
    moderator_sd = moderator.std(ddof=1)
    covariance = moderation.cov_params()
    critical = stats.t.ppf(0.975, moderation.df_resid)
    slopes = []
    for label, centered_level in [("ortalama-1SS", -moderator_sd), ("ortalama", 0.0), ("ortalama+1SS", moderator_sd)]:
        contrast = np.array([0.0, 1.0, 0.0, centered_level])
        slope = float(contrast @ moderation.params)
        variance = float(covariance[1, 1] + centered_level**2 * covariance[3, 3]
                         + 2 * centered_level * covariance[1, 3])
        standard_error = float(np.sqrt(variance))
        interval = [slope - critical * standard_error, slope + critical * standard_error]
        test = moderation.t_test(contrast)
        np.testing.assert_allclose(test.conf_int()[0], interval)
        np.testing.assert_allclose(test.sd.item(), standard_error)
        slopes.append({"level": label, "w": float(moderator.mean() + centered_level),
                       "w_centered": float(centered_level), "slope": slope, "se": standard_error,
                       "ci95_pointwise": interval, "p_pointwise": float(test.pvalue)})
    results = {
        "data_kind": "SIMULATION; no real participants", "n": len(data), "generation_seed": 202609,
        "normalized_LF_sha256": SOURCE_HASH,
        "mediation": {"a_model": coefficient_table(mediator_model, ["intercept", "a"]),
                      "outcome_model": coefficient_table(outcome_model, ["intercept", "c_prime", "b"]),
                      "total_model": coefficient_table(total_model, ["intercept", "c"]),
                      "indirect_ab": indirect, "direct_c_prime": direct, "total_c": total,
                      "bootstrap": {"method": "paired-row percentile; linear quantiles; not BCa",
                                    "seed": BOOTSTRAP_SEED, "requested": BOOTSTRAP_REPLICATES,
                                    "completed": len(bootstrap), "failed": 0,
                                    "ci95": bootstrap_interval.tolist(),
                                    "bootstrap_se": float(bootstrap.std(ddof=1))}},
        "moderation": {"coefficients": coefficient_table(moderation, ["intercept", "x_c", "w_c", "interaction"]),
                       "x_mean": float(predictor.mean()), "w_mean": float(moderator.mean()),
                       "w_sd": float(moderator_sd), "df_resid": float(moderation.df_resid),
                       "R_squared": float(moderation.rsquared), "simple_slopes": slopes},
        "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__, "statsmodels": sm.__version__}}
    return results, bootstrap, moderation


def main():
    directory = Path(__file__).resolve().parent
    source_path = directory / "veri.csv"
    source_bytes = source_path.read_bytes()
    data = load_data(source_path)
    results, bootstrap, moderation = analyze(data)
    output = directory / "sonuclar"
    figures = directory / "grafikler"
    output.mkdir(exist_ok=True)
    figures.mkdir(exist_ok=True)
    (output / "ozet.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pd.DataFrame({"tekrar": np.arange(1, len(bootstrap) + 1), "ab": bootstrap}).to_csv(output / "bootstrap.csv", index=False)
    pd.DataFrame(results["moderation"]["simple_slopes"]).to_csv(output / "basit-egimler.csv", index=False)
    data.assign(x_c=data.x - data.x.mean(), w_c=data.w - data.w.mean()).to_csv(output / "merkezlenmis.csv", index=False)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(8, 3.8), constrained_layout=True)
    axes[0].hist(bootstrap, bins=35, color="#c49b5c", edgecolor="white")
    axes[0].axvline(results["mediation"]["indirect_ab"], color="#781e2d", label="Örneklem ab")
    for endpoint in results["mediation"]["bootstrap"]["ci95"]:
        axes[0].axvline(endpoint, color="#3c3c41", linestyle="--")
    axes[0].set(xlabel="Dolaylı yol çarpımı ab", ylabel="Tekrar sayısı", title="Simülasyon: 5000 bootstrap")
    axes[0].legend(frameon=False)
    grid = np.linspace(data.x.quantile(0.05), data.x.quantile(0.95), 100)
    centered_grid = grid - data.x.mean()
    for row, color in zip(results["moderation"]["simple_slopes"], ["#781e2d", "#b08743", "#3c3c41"]):
        level = row["w_centered"]
        matrix = np.column_stack([np.ones(len(grid)), centered_grid, np.full(len(grid), level), centered_grid * level])
        axes[1].plot(grid, moderation.predict(matrix), color=color, label=row["level"])
    axes[1].set(xlabel="X (keyfî birim)", ylabel="Tahmin edilen Y_duzenleyicilik", title="Simülasyon: basit eğimler")
    axes[1].legend(frameon=False, fontsize=8)
    for axis in axes:
        axis.spines[["top", "right"]].set_visible(False)
    figure.savefig(figures / "b09-simulasyon.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source_path.read_bytes() == source_bytes
    print(json.dumps(results, ensure_ascii=False, indent=2))
    print("Simülasyon hesabı doğrulandı; gerçek araştırma veya nedensellik kanıtı değildir.")


if __name__ == "__main__":
    main()