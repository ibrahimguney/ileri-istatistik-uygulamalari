"""Bölüm 15: Aracılık ve düzenleyicilik — simülasyon, bootstrap ve basit eğimler.

Kitap kökünden:  python uygulamalar/b15-aracilik-duzenleyicilik/analiz.py

Veri gerçek katılımcılardan gelmez; üretim kodu bu dosyadadır. İki ayrı yanıt
üretilir: aracılık için y_aracilik, düzenleyicilik için y_duzenleyicilik.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import statsmodels
import statsmodels.formula.api as smf

N, URETIM_TOHUMU, BOOT_TOHUMU, B = 160, 202609, 202610, 5000


def uret():
    rng = np.random.default_rng(URETIM_TOHUMU)
    x, w, e_m, e_y, e_d = (rng.standard_normal(N) for _ in range(5))
    araci = .6 * x + e_m
    return pd.DataFrame({
        "id": np.arange(1, N + 1), "x": x, "w": w, "araci": araci,
        "y_aracilik": .2 * x + .7 * araci + e_y,
        "y_duzenleyicilik": .3 * x + .2 * w + .5 * x * w + e_d})


def dolayli(x, m, y):
    xc = x - x.mean()
    a = xc @ (m - m.mean()) / (xc @ xc)
    Z = np.column_stack([np.ones(len(x)), x, m])
    b = np.linalg.lstsq(Z, y, rcond=None)[0][2]
    return a * b


def main():
    klasor = Path(__file__).parent
    cikti = klasor / "sonuclar"
    cikti.mkdir(exist_ok=True)
    veri = uret()
    veri.to_csv(klasor / "veri.csv", index=False, float_format="%.6f")

    # --- Aracılık: a, b, c', c ve dolaylı etki
    m_a = smf.ols("araci ~ x", data=veri).fit()
    m_b = smf.ols("y_aracilik ~ x + araci", data=veri).fit()
    m_c = smf.ols("y_aracilik ~ x", data=veri).fit()
    a, b, c_ust = m_a.params["x"], m_b.params["araci"], m_b.params["x"]
    c = m_c.params["x"]
    ab = a * b
    assert np.isclose(c, c_ust + ab)  # OLS'de toplam = doğrudan + dolaylı
    assert np.isclose(ab, dolayli(veri.x.values, veri.araci.values, veri.y_aracilik.values))

    rng = np.random.default_rng(BOOT_TOHUMU)
    X, M, Y = veri.x.values, veri.araci.values, veri.y_aracilik.values
    boot = np.array([dolayli(X[i], M[i], Y[i]) for i in (rng.integers(0, N, N) for _ in range(B))])
    ga = np.percentile(boot, [2.5, 97.5])
    assert np.allclose([ab, *ga], [.521844, .368530, .698101], atol=5e-7)

    # --- Düzenleyicilik: merkezleme ve basit eğimler
    veri["x_c"] = veri.x - veri.x.mean()
    veri["w_c"] = veri.w - veri.w.mean()
    veri["etkilesim"] = veri.x_c * veri.w_c
    m_mod = smf.ols("y_duzenleyicilik ~ x_c + w_c + etkilesim", data=veri).fit()
    m_ham = smf.ols("y_duzenleyicilik ~ x * w", data=veri).fit()
    assert np.isclose(m_mod.params["etkilesim"], m_ham.params["x:w"])  # merkezleme değişmezliği
    V = m_mod.cov_params()
    sd_w = veri.w.std(ddof=1)
    tcrit = scipy.stats.t.ppf(.975, m_mod.df_resid)
    egimler = []
    for ad, deger in [("W ortalama - 1 SS", -sd_w), ("W ortalama", 0.0), ("W ortalama + 1 SS", sd_w)]:
        est = m_mod.params["x_c"] + deger * m_mod.params["etkilesim"]
        se = np.sqrt(V.loc["x_c", "x_c"] + deger**2 * V.loc["etkilesim", "etkilesim"]
                     + 2 * deger * V.loc["x_c", "etkilesim"])
        # aynı eğim, W'yi o değere kaydırılmış modelle de elde edilmelidir
        kay = veri.assign(w_k=veri.w_c - deger, et_k=veri.x_c * (veri.w_c - deger))
        m_k = smf.ols("y_duzenleyicilik ~ x_c + w_k + et_k", data=kay).fit()
        assert np.isclose(m_k.params["x_c"], est) and np.isclose(m_k.bse["x_c"], se)
        egimler.append({"koşul": ad, "w_c": deger, "eğim": est, "SH": se,
                        "alt": est - tcrit * se, "üst": est + tcrit * se,
                        "t": est / se, "p": 2 * scipy.stats.t.sf(abs(est / se), m_mod.df_resid)})
    pd.DataFrame(egimler).to_csv(cikti / "basit_egimler.csv", index=False)

    def tablo(model, adlar):
        return {k: {"b": model.params[k], "SH": model.bse[k], "t": model.tvalues[k],
                    "p": model.pvalues[k], "alt": model.conf_int().loc[k, 0],
                    "üst": model.conf_int().loc[k, 1]} for k in adlar}

    ozet = {
        "n": N, "uretim_tohumu": URETIM_TOHUMU, "bootstrap_tohumu": BOOT_TOHUMU, "bootstrap_tekrar": B,
        "aracilik": {"a": tablo(m_a, ["x"])["x"], "b": tablo(m_b, ["araci"])["araci"],
                     "c_ussu": tablo(m_b, ["x"])["x"], "c": tablo(m_c, ["x"])["x"],
                     "ab": ab, "ab_persentil_95": list(ga), "bootstrap_sd": boot.std(ddof=1)},
        "duzenleyicilik": {"katsayilar": tablo(m_mod, ["Intercept", "x_c", "w_c", "etkilesim"]),
                           "R2": m_mod.rsquared, "sd_w": sd_w, "basit_egimler": egimler},
        "surumler": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__,
                     "statsmodels": statsmodels.__version__},
    }
    (cikti / "ozet.json").write_text(json.dumps(ozet, ensure_ascii=False, indent=2, default=float) + "\n",
                                     encoding="utf-8")

    fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
    ax[0].hist(boot, bins=50, color="#7a1e2d", alpha=.8)
    for q in ga:
        ax[0].axvline(q, color="black", ls="--", lw=1)
    ax[0].axvline(ab, color="#c49b5c", lw=2)
    ax[0].set(title="Dolaylı etkinin bootstrap dağılımı", xlabel="ab")
    xs = np.linspace(veri.x_c.min(), veri.x_c.max(), 50)
    for e, st in zip(egimler, ["--", "-", ":"]):
        yhat = m_mod.params["Intercept"] + e["w_c"] * m_mod.params["w_c"] + e["eğim"] * xs
        ax[1].plot(xs, yhat, st, color="#3c3c41", label=e["koşul"])
    ax[1].set(title="W düzeylerinde basit eğimler", xlabel="X (merkezlenmiş)", ylabel="Tahmin")
    ax[1].legend(fontsize=7, frameon=False)
    fig.tight_layout()
    sekiller = klasor.parents[1] / "assets_figures"
    sekiller.mkdir(exist_ok=True)
    fig.savefig(sekiller / "b13m-bootstrap-egimler.pdf", metadata={"CreationDate": None, "ModDate": None})

    print(f"Doğrulama başarılı: ab={ab:.6f}, %95 GA=[{ga[0]:.6f}, {ga[1]:.6f}], "
          f"etkileşim={m_mod.params['etkilesim']:.4f}")


if __name__ == "__main__":
    main()
