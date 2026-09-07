from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import scipy
from scipy import stats

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "sonuclar"

EXPECTED_NORMALIZED_HASHES = {
    "sleep.csv": "adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e",
    "ToothGrowth.csv": "654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3",
}


def normalized_sha256(path: Path) -> str:
    raw = path.read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    return hashlib.sha256(raw).hexdigest()


def summarize(values) -> dict:
    x = np.asarray(values, dtype=float)
    return {"n": int(len(x)), "ortalama": float(x.mean()), "s": float(x.std(ddof=1))}


def one_sample(values) -> dict:
    x = np.asarray(values, dtype=float)
    result = stats.ttest_1samp(x, 0)
    ci = result.confidence_interval(confidence_level=0.95)
    sd = x.std(ddof=1)
    return {
        "n": int(len(x)),
        "ortalama": float(x.mean()),
        "s": float(sd),
        "SH": float(sd / np.sqrt(len(x))),
        "t": float(result.statistic),
        "sd": int(len(x) - 1),
        "p_iki_yonlu": float(result.pvalue),
        "GA95": [float(ci.low), float(ci.high)],
    }


def independent(first, second, equal_var: bool) -> dict:
    a = np.asarray(first, dtype=float)
    b = np.asarray(second, dtype=float)
    result = stats.ttest_ind(a, b, equal_var=equal_var)
    ci = result.confidence_interval(confidence_level=0.95)
    return {
        "fark": float(a.mean() - b.mean()),
        "SH": float((a.mean() - b.mean()) / result.statistic),
        "t": float(result.statistic),
        "sd": float(result.df),
        "p_iki_yonlu": float(result.pvalue),
        "GA95": [float(ci.low), float(ci.high)],
    }


def main() -> None:
    sleep_path = HERE / "sleep.csv"
    tooth_path = HERE / "ToothGrowth.csv"

    hashes = {name: normalized_sha256(HERE / name) for name in EXPECTED_NORMALIZED_HASHES}
    assert hashes == EXPECTED_NORMALIZED_HASHES, "Yerel kaynak kopyası değişmiş."

    sleep = pd.read_csv(sleep_path)
    teeth = pd.read_csv(tooth_path)
    assert sleep.shape == (20, 4) and teeth.shape == (60, 4)
    assert sleep.notna().all().all() and teeth.notna().all().all()
    assert not sleep.duplicated(["ID", "group"]).any()
    assert sleep["ID"].nunique() == 10
    assert sleep.groupby("ID")["group"].nunique().eq(2).all()
    assert set(sleep["group"]) == {1, 2}
    assert set(teeth["supp"]) == {"OJ", "VC"}
    assert set(teeth["dose"]) == {0.5, 1.0, 2.0}
    assert teeth.groupby(["dose", "supp"]).size().eq(10).all()

    pivot = sleep.pivot(index="ID", columns="group", values="extra").sort_index()
    wide = pd.DataFrame({
        "ID": pivot.index.astype(int),
        "kosul1": pivot[1].to_numpy(),
        "kosul2": pivot[2].to_numpy(),
    })
    wide["fark"] = (wide["kosul2"] - wide["kosul1"]).round(10)
    wide.to_csv(HERE / "uyku_esli.csv", index=False)

    dis = teeth.copy()
    dis["supp_kod"] = dis["supp"].map({"OJ": 1, "VC": 2}).astype(int)
    dis.to_csv(HERE / "dis_veri.csv", index=False)

    difference = wide["fark"].to_numpy(dtype=float)
    paired_test = one_sample(difference)
    corr = stats.pearsonr(wide["kosul1"], wide["kosul2"])
    paired_test["dz"] = float(difference.mean() / difference.std(ddof=1))

    dose1 = dis.loc[np.isclose(dis["dose"], 1.0)]
    oj = dose1.loc[dose1["supp"] == "OJ", "len"].to_numpy(dtype=float)
    vc = dose1.loc[dose1["supp"] == "VC", "len"].to_numpy(dtype=float)
    levene = stats.levene(oj, vc, center="mean")
    pooled_sd = np.sqrt(((len(oj) - 1) * oj.var(ddof=1) + (len(vc) - 1) * vc.var(ddof=1)) / (len(oj) + len(vc) - 2))

    first5 = one_sample(wide.loc[wide["ID"] <= 5, "fark"])
    repeated = one_sample(np.repeat(difference, 2))

    missing_copy = wide.copy()
    missing_copy.loc[missing_copy["ID"] == 1, "kosul2"] = np.nan
    missing_copy.loc[missing_copy["ID"] == 2, "kosul1"] = np.nan
    missing_copy["fark"] = missing_copy["kosul2"] - missing_copy["kosul1"]
    complete_difference = missing_copy["fark"].dropna().to_numpy(dtype=float)
    missing_result = one_sample(complete_difference)

    summary = {
        "bolum": "B18",
        "baslik": "IBM SPSS Uygulamaları",
        "kaynak": {
            "sleep_satir": int(len(sleep)),
            "sleep_ID": int(sleep["ID"].nunique()),
            "ToothGrowth_satir": int(len(teeth)),
            "doz_supp_hucre_n": int(teeth.groupby(["dose", "supp"]).size().iloc[0]),
            "normalize_sha256": hashes,
        },
        "uyku_esli": {
            "kosul1": summarize(wide["kosul1"]),
            "kosul2": summarize(wide["kosul2"]),
            "korelasyon": {"r": float(corr.statistic), "p": float(corr.pvalue)},
            "fark_kosul2_eksi_kosul1": paired_test,
        },
        "ToothGrowth_doz1": {
            "OJ": summarize(oj),
            "VC": summarize(vc),
            "Levene_ortalama_merkezli": {"F": float(levene.statistic), "p": float(levene.pvalue)},
            "Welch": independent(oj, vc, equal_var=False),
            "Student": independent(oj, vc, equal_var=True),
            "d_pooled": float((oj.mean() - vc.mean()) / pooled_sd),
            "filtre_kapatilinca_doz_frekanslari": {str(float(k)): int(v) for k, v in teeth.groupby("dose").size().items()},
        },
        "durum_deneyi": {
            "ID_1_5_filtresi": first5,
            "agirlik_2_mekanik_tekrar": repeated,
            "iki_hucre_gizleme": {
                "kosul1_gecerli": int(missing_copy["kosul1"].notna().sum()),
                "kosul2_gecerli": int(missing_copy["kosul2"].notna().sum()),
                "tam_cift": int(missing_copy[["kosul1", "kosul2"]].notna().all(axis=1).sum()),
                **missing_result,
            },
        },
        "yurutme": {
            "Python_referans": True,
            "SPSS_calistirildi": False,
            "R_calistirildi": False,
            "not": "SPSS/R komut dosyaları hazırlanmıştır; bu Python betiğinin çalışması onları yürütmez.",
        },
        "surumler": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__},
    }

    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "ozet.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("B18 Python referans doğrulaması tamamlandı; SPSS ve R çalıştırılmadı.")
    print(f"Uyku: n={paired_test['n']}, fark={paired_test['ortalama']:.3f}, t={paired_test['t']:.6f}")
    print(f"Doz 1 Welch: fark={oj.mean()-vc.mean():.2f}, t={summary['ToothGrowth_doz1']['Welch']['t']:.6f}")


if __name__ == "__main__":
    main()
