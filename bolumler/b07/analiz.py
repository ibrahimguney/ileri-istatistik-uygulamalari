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

SOURCE_HASH = "51dcab9aeaa121123dd28a00156d4dfa398c38eecad69bd5699ae4cea03e5ee9"
SOURCE_URL = "https://archive.ics.uci.edu/static/public/320/data.csv"


def fit_model(data):
    predictors = sm.add_constant(data[["G1"]], has_constant="add")
    return sm.OLS(data["G3"], predictors, missing="raise").fit()


def main():
    directory = Path(__file__).resolve().parent
    source_path = directory / "veri.csv"
    original_bytes = source_path.read_bytes()
    normalized_bytes = original_bytes.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    assert hashlib.sha256(normalized_bytes).hexdigest() == SOURCE_HASH
    source = pd.read_csv(source_path)
    assert list(source.columns) == ["kaynak_satir", "school", "G1", "G3"]
    assert len(source) == 80 and source.notna().all().all()
    np.testing.assert_array_equal(source["kaynak_satir"], np.arange(1, 81))
    assert source["school"].eq("GP").all()
    assert source[["G1", "G3"]].apply(lambda column: column.between(0, 20).all()).all()
    data = source.iloc[:60].copy()
    transfer = source.iloc[60:80].copy()
    model = fit_model(data)
    first_grades = data["G1"].to_numpy()
    final_grades = data["G3"].to_numpy()
    independent = stats.linregress(first_grades, final_grades)
    np.testing.assert_allclose(model.params, [independent.intercept, independent.slope])
    np.testing.assert_allclose(model.pvalues.iloc[1], independent.pvalue)
    sum_xx = np.sum((first_grades - first_grades.mean()) ** 2)
    sum_xy = np.sum((first_grades - first_grades.mean()) * (final_grades - final_grades.mean()))
    np.testing.assert_allclose([first_grades.sum(), final_grades.sum(),
                               np.sum(first_grades ** 2), np.sum(first_grades * final_grades),
                               np.sum(final_grades ** 2)], [726, 767, 9170, 9505, 10039])
    residual_sd = float(np.sqrt(model.mse_resid))
    critical = stats.t.ppf(0.975, len(data) - 2)
    new_predictors = pd.DataFrame({"const": [1.0], "G1": [12.0]})
    prediction = model.get_prediction(new_predictors).summary_frame(alpha=0.05)
    factor = 1 / len(data) + (12 - first_grades.mean()) ** 2 / sum_xx
    mean_value = float(model.params.iloc[0] + 12 * model.params.iloc[1])
    manual_intervals = [mean_value - critical * residual_sd * np.sqrt(factor),
                        mean_value + critical * residual_sd * np.sqrt(factor),
                        mean_value - critical * residual_sd * np.sqrt(1 + factor),
                        mean_value + critical * residual_sd * np.sqrt(1 + factor)]
    columns = ["mean_ci_lower", "mean_ci_upper", "obs_ci_lower", "obs_ci_upper"]
    np.testing.assert_allclose(prediction[columns].iloc[0], manual_intervals)
    influence = model.get_influence()
    leave_one_out_errors = []
    leave_one_out_slopes = []
    for position in range(len(data)):
        training = data.drop(index=position)
        held_out = sm.add_constant(data.loc[[position], ["G1"]], has_constant="add")
        fitted = fit_model(training)
        leave_one_out_errors.append(final_grades[position] - fitted.predict(held_out).iloc[0])
        leave_one_out_slopes.append(float(fitted.params.iloc[1]))
    np.testing.assert_allclose(leave_one_out_errors,
                               model.resid / (1 - influence.hat_matrix_diag))
    robust = model.get_robustcov_results(cov_type="HC3", use_t=True)
    design = model.model.exog
    bread = np.linalg.inv(design.T @ design)
    adjusted_squares = model.resid.to_numpy() ** 2 / (1 - influence.hat_matrix_diag) ** 2
    hc3_cov = bread @ (design.T @ (design * adjusted_squares[:, None])) @ bread
    np.testing.assert_allclose(robust.bse, np.sqrt(np.diag(hc3_cov)))
    transfer_model = fit_model(transfer)
    intervals = model.conf_int()
    results = {
        "source_url": SOURCE_URL, "source_doi": "10.24432/C5TG7T",
        "local_projection_sha256": hashlib.sha256(original_bytes).hexdigest(),
        "normalized_LF_sha256": SOURCE_HASH,
        "selection": "Portuguese course, source rows 1-60; separate exercise rows 61-80",
        "n": len(data), "x_mean": float(first_grades.mean()),
        "y_mean": float(final_grades.mean()), "Sxx": float(sum_xx), "Sxy": float(sum_xy),
        "intercept": float(model.params.iloc[0]), "slope": float(model.params.iloc[1]),
        "slope_se": float(model.bse.iloc[1]), "slope_t": float(model.tvalues.iloc[1]),
        "slope_p": float(model.pvalues.iloc[1]), "slope_ci": intervals.iloc[1].tolist(),
        "SSE": float(model.ssr), "SST": float(model.centered_tss),
        "R_squared": float(model.rsquared), "residual_sd": residual_sd,
        "training_RMSE": float(np.sqrt(np.mean(model.resid ** 2))),
        "LOOCV_RMSE": float(np.sqrt(np.mean(np.square(leave_one_out_errors)))),
        "leave_one_out_slopes": leave_one_out_slopes,
        "HC3_slope_se": float(robust.bse[1]), "HC3_slope_p": float(robust.pvalues[1]),
        "HC3_slope_ci": robust.conf_int()[1].tolist(),
        "first_row_leverage": float(influence.hat_matrix_diag[0]),
        "first_row_cook": float(influence.cooks_distance[0][0]),
        "prediction_at_12": prediction.iloc[0].to_dict(),
        "transfer_n": len(transfer), "transfer_intercept": float(transfer_model.params.iloc[0]),
        "transfer_slope": float(transfer_model.params.iloc[1]),
        "transfer_R_squared": float(transfer_model.rsquared),
        "versions": {"numpy": np.__version__, "pandas": pd.__version__,
                     "statsmodels": sm.__version__, "scipy": scipy.__version__}
    }
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    data.to_csv(output / "not_basari.csv", index=False)
    transfer.to_csv(output / "aktarim.csv", index=False)
    pd.DataFrame({"cikarilan_kaynak_satir": data["kaynak_satir"].to_numpy(),
                  "egim": leave_one_out_slopes,
                  "LOOCV_hatasi": leave_one_out_errors}).to_csv(output / "duyarlilik.csv", index=False)
    (output / "ozet.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    data.assign(tahmin=model.fittedvalues, artik=model.resid,
                kaldirac=influence.hat_matrix_diag,
                cook=influence.cooks_distance[0]).to_csv(output / "tani.csv", index=False)
    prediction.to_csv(output / "araliklar.csv", index=False)
    grid = np.linspace(first_grades.min(), first_grades.max(), 100)
    curve = model.get_prediction(sm.add_constant(grid)).summary_frame()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.8), constrained_layout=True)
    axes[0].fill_between(grid, curve["mean_ci_lower"], curve["mean_ci_upper"],
                         color="#c49b5c", alpha=0.3)
    axes[0].plot(grid, curve["mean"], color="#781e2d")
    grouped = data.groupby(["G1", "G3"]).size().reset_index(name="adet")
    axes[0].scatter(grouped.G1, grouped.G3, color="#3c3c41", s=15 * grouped.adet, zorder=3)
    axes[0].set(xlabel="Birinci dönem notu (G1)", ylabel="Yıl sonu notu (G3)",
                title="(a) Gerçek veri", ylim=(-0.5, 20.5))
    axes[1].scatter(model.fittedvalues, model.resid, color="#781e2d", s=22, alpha=0.65)
    axes[1].axhline(0, color="#3c3c41", linewidth=1)
    axes[1].annotate("Satır 1", (model.fittedvalues.iloc[0], model.resid.iloc[0]),
                     xytext=(6, -13), textcoords="offset points", fontsize=9)
    axes[1].set(xlabel="Tahmin edilen\nyıl sonu notu", ylabel="Artık (puan)", title="(b) Artıklar")
    for axis in axes:
        axis.spines[["top", "right"]].set_visible(False)
    figures = directory / "grafikler"
    figures.mkdir(exist_ok=True)
    destination = figures / "b07-ogrenme-senaryosu.pdf"
    figure.savefig(destination, metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source_path.read_bytes() == original_bytes
    print(json.dumps(results, indent=2))
    print("Doğrulama başarılı: yerel kaynak, OLS, HC3, aralıklar ve LOOCV tutarlı.")


if __name__ == "__main__":
    main()