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
import statsmodels
from statsmodels.stats.power import TTestIndPower, TTestPower

SOURCE_HASH = "adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e"


def power_t(count, effect=.5, alpha=.05, ratio=1, paired=False, sided=2):
    if not np.isfinite([count, effect, alpha, ratio]).all():
        raise ValueError("Sonlu girdiler gerekli.")
    if count < 2 or ratio <= 0 or not 0 < alpha < 1 or sided not in (1, 2):
        raise ValueError("Geçersiz n, oran, alfa veya yön.")
    if not paired and count*ratio < 2:
        raise ValueError("İkinci grupta en az iki gözlem gerekli.")
    degrees = count-1 if paired else count*(1+ratio)-2
    noncentrality = effect*np.sqrt(count if paired else count*ratio/(1+ratio))
    critical = stats.t.ppf(1-alpha/sided, degrees)
    if sided == 1:
        result = stats.nct.sf(critical, degrees, noncentrality)
    elif noncentrality == 0:
        result = stats.f.sf(critical**2, 1, degrees)
    else:
        result = stats.ncf.sf(critical**2, 1, degrees, noncentrality**2)
    if not np.isfinite(result) or not 0 <= result <= 1:
        raise ArithmeticError("Sonlu olasılık hesaplanamadı.")
    return float(result)


def minimum_count(target=.8, **settings):
    if not 0 < target < 1:
        raise ValueError("Güç hedefi 0 ile 1 arasında olmalı.")
    for count in range(3, 20001):
        current = power_t(count, **settings)
        if current >= target:
            previous = power_t(count-1, **settings)
            if previous >= target:
                raise ValueError("Alt arama sınırı yetersiz.")
            return {"n": count, "hedef": target, "onceki_guc": previous, "guc": current}
    raise ValueError("Arama sınırında hedefe ulaşılamadı.")


def fisher_power(count, rho=.3, alpha=.05):
    if count <= 3 or not -1 < rho < 1 or not 0 < alpha < 1:
        raise ValueError("Geçersiz Fisher-z girdisi.")
    shift = np.arctanh(rho)*np.sqrt(count-3)
    critical = stats.norm.ppf(1-alpha/2)
    return float(stats.norm.sf(critical-shift)+stats.norm.cdf(-critical-shift))


def main():
    base = Path(__file__).resolve().parent
    source = base / "veri.csv"
    original = source.read_bytes()
    normalized = original.replace(b"\r\n", b"\n").rstrip(b"\n")+b"\n"
    assert hashlib.sha256(normalized).hexdigest() == SOURCE_HASH
    frame = pd.read_csv(source)
    assert len(frame) == 20 and not frame.isna().any().any()
    assert not frame.duplicated(["ID", "group"]).any()
    assert set(frame.ID) == set(range(1, 11)) and set(frame.group) == {1, 2}
    wide = frame.pivot(index="ID", columns="group", values="extra").sort_index()
    assert not wide.isna().any().any()
    shuffled = frame.sample(frac=1, random_state=5).pivot(index="ID", columns="group", values="extra").sort_index()
    pd.testing.assert_frame_equal(wide, shuffled)
    differences = wide[2]-wide[1]
    deviation = float(differences.std(ddof=1))
    assert np.isclose(deviation, np.sqrt(13.616/9))
    scenarios = []
    settings_list = [
        ("ana", {}), ("d_02", {"effect": .2}), ("d_03", {"effect": .3}),
        ("d_08", {"effect": .8}), ("guc_09", {"target": .9}),
        ("alfa_01", {"alpha": .01}), ("uc_bonferroni", {"alpha": .05/3}),
        ("tek_yon", {"sided": 1}), ("ikiye_bir", {"ratio": 2}),
        ("esli_dz_05", {"paired": True})]
    for name, overrides in settings_list:
        settings = {"effect": .5, "alpha": .05, "ratio": 1, "paired": False, "sided": 2}
        target = overrides.get("target", .8)
        settings.update({key: value for key, value in overrides.items() if key != "target"})
        result = minimum_count(target=target, **settings)
        count = result["n"]
        second = 0 if settings["paired"] else count*settings["ratio"]
        result.update({"senaryo": name, **settings, "n2": second, "toplam_kisi": count+second})
        model = TTestPower() if settings["paired"] else TTestIndPower()
        arguments = {"effect_size": settings["effect"], "nobs" if settings["paired"] else "nobs1": count,
                     "alpha": settings["alpha"], "alternative": "two-sided" if settings["sided"] == 2 else "larger"}
        if not settings["paired"]:
            arguments["ratio"] = settings["ratio"]
        assert np.isclose(result["guc"], model.power(**arguments), atol=1e-10)
        degrees = count-1 if settings["paired"] else count+second-2
        noncentrality = settings["effect"]*np.sqrt(count if settings["paired"] else count*second/(count+second))
        critical = stats.t.ppf(1-settings["alpha"]/settings["sided"], degrees)
        tail_power = stats.nct.sf(critical, degrees, noncentrality)
        if settings["sided"] == 2:
            tail_power += stats.nct.cdf(-critical, degrees, noncentrality)
        assert np.isclose(result["guc"], tail_power, atol=1e-10)
        scenarios.append(result)
    continuous = float(TTestIndPower().solve_power(effect_size=.5, alpha=.05, power=.8, ratio=1))
    assert int(np.ceil(continuous)) == scenarios[0]["n"] == 64
    assert np.isclose(power_t(40, effect=0), .05)
    assert np.isclose(power_t(40, effect=.5), power_t(40, effect=-.5))
    assert power_t(40, effect=-.5, sided=1) < .05
    detectable = float(optimize.brentq(lambda effect: power_t(40, effect=effect)-.8, .01, 1))
    spreads = [{"sigma_D": spread, "delta": .5, "dz": .5/spread,
                **minimum_count(effect=.5/spread, paired=True)} for spread in (1., deviation, 1.5)]
    correlations = [{"rho": rho, "sigma_D": float(np.sqrt(2*(1-rho))),
                     **minimum_count(effect=.5/np.sqrt(2*(1-rho)), paired=True)} for rho in (.3,.5,.7)]
    needed, retention = 64, .85
    heuristic = int(np.ceil(needed/retention))
    def both_retained(enrolled):
        return float(stats.binom.sf(needed-1, enrolled, retention)**2)
    assurance_n = next(count for count in range(needed, 500) if both_retained(count) >= .9)
    assert both_retained(assurance_n-1) < .9 <= both_retained(assurance_n)
    retention_table = [{"davet_grup": count, "beklenen_tam_grup": count*retention,
                        "iki_grupta_en_az_64": both_retained(count)} for count in range(64, 91)]
    precision = lambda count: float(stats.t.ppf(.975, 2*count-2)*np.sqrt(2/count))
    precision_n = next(count for count in range(3, 20000) if precision(count) <= .2)
    assert precision(precision_n-1) > .2
    correlation_n = next(count for count in range(4, 20000) if fisher_power(count) >= .8)
    grid = pd.DataFrame([{"n_grup": count, "d": effect, "guc": power_t(count, effect=effect)}
                         for effect in (.2,.3,.5,.8) for count in range(3, 401)])
    for effect, rows in grid.groupby("d"):
        assert np.all(np.diff(rows.guc) >= -1e-10)
    for call in (lambda: power_t(1), lambda: power_t(10, alpha=1), lambda: power_t(10, effect=np.nan),
                 lambda: fisher_power(3), lambda: minimum_count(target=1)):
        try:
            call()
        except ValueError:
            pass
        else:
            raise AssertionError("Hatalı girdi reddedilmedi.")
    results = {
        "kaynak": source.name, "normalize_LF_sha256": SOURCE_HASH,
        "surumler": {"numpy": np.__version__, "scipy": scipy.__version__, "pandas": pd.__version__,
                     "statsmodels": statsmodels.__version__, "matplotlib": matplotlib.__version__},
        "yontem": "Iki yonlu merkezsiz F ile tam t gucu; tek yonlu merkezsiz t. Simulasyon degil.",
        "senaryolar": scenarios, "surekli_n": continuous,
        "sabit_40": {"guc_d05": power_t(40), "guc08_icin_d": detectable},
        "tarihsel_yayilim": {"cift": 10, "ortalama": float(differences.mean()), "s_D": deviation,
                              "plan_senaryolari": spreads}, "esli_rho": correlations,
        "kayip": {"tutulma": retention, "gereken_grup": needed, "beklenti_davet": heuristic,
                  "beklenti_iki_grup_olasilik": both_retained(heuristic), "olasilik_hedef": .9,
                  "olasilik_davet": assurance_n, "onceki": both_retained(assurance_n-1), "ulasilan": both_retained(assurance_n)},
        "hassasiyet": {"hedef_yari_genislik_sigma": .2, "n_grup": precision_n,
                       "onceki": precision(precision_n-1), "yari_genislik": precision(precision_n), "n64": precision(64)},
        "korelasyon_yaklasik": {"rho": .3, "n": correlation_n,
                               "onceki": fisher_power(correlation_n-1), "guc": fisher_power(correlation_n)},
        "kume_kurgu": {"m": 20, "ICC": .05, "DE": 1+19*.05},
        "R_SPSS_calistirildi": False}
    output = base / "sonuclar"
    output.mkdir(parents=True, exist_ok=True)
    (output / "ozet.json").write_text(json.dumps(results, ensure_ascii=False, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    for name, table in (("senaryolar", scenarios), ("pilot_yayilim", spreads), ("esli_rho", correlations),
                        ("kayip", retention_table), ("guc_egrileri", grid)):
        pd.DataFrame(table).to_csv(output / f"{name}.csv", index=False, float_format="%.10f")
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    figure, axes = plt.subplots(1, 2, figsize=(8, 4.1), layout="constrained")
    for effect, rows in grid.groupby("d"):
        axes[0].plot(rows.n_grup, rows.guc, label=f"d={effect:.1f}")
    axes[0].axhline(.8, color="gray", linestyle="--")
    axes[0].scatter([64], [power_t(64)], color="#6b233b", zorder=5)
    axes[0].set(xlabel="Analiz edilebilir kişi\n(grup başına)", ylabel="Test gücü", ylim=(0,1.02))
    axes[0].legend()
    loss = pd.DataFrame(retention_table)
    axes[1].plot(loss.davet_grup, loss.iki_grupta_en_az_64, color="#6b233b")
    axes[1].axhline(.9, color="gray", linestyle="--")
    axes[1].scatter([76,82], [both_retained(76),both_retained(82)], color="#233b52")
    axes[1].set(xlabel="Kayıt sayısı (grup başına)", ylabel="İki grupta da en az 64 kişi\nkalma olasılığı", ylim=(0,1.02))
    axes[0].set_title("İki yönlü t testi")
    axes[1].set_title("%85 tutulma varsayımı")
    figures = base / "grafikler"
    figures.mkdir(exist_ok=True)
    figure.savefig(figures / "b05-guc-planlama.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source.read_bytes() == original
    print(json.dumps({"n_grup":64, "n_esli":34, "korelasyon_yaklasik_n":correlation_n,
                      "kayip_beklentisi":heuristic, "kayip_olasiligi_n":assurance_n,
                      "kontroller":"basarili"}, ensure_ascii=False))


if __name__ == "__main__":
    main()