from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

HERE = Path(__file__).resolve().parent
OUT = HERE / "sonuclar"
OUT.mkdir(exist_ok=True)


def paired_summary(path: Path) -> dict:
    df = pd.read_csv(path)
    wide = df.pivot(index="ID", columns="group", values="extra")
    valid = wide[[1, 2]].dropna()
    diff = valid[2] - valid[1]
    test = stats.ttest_rel(valid[2], valid[1])
    ci = stats.t.interval(
        0.95,
        df=len(diff) - 1,
        loc=float(diff.mean()),
        scale=float(stats.sem(diff)),
    )
    corr = stats.pearsonr(valid[1], valid[2]) if len(valid) >= 3 else None
    return {
        "satir_sayisi": int(len(df)),
        "benzersiz_id": int(df["ID"].nunique()),
        "gecerli_cift": int(len(valid)),
        "group1_ortalama": float(valid[1].mean()),
        "group1_ss": float(valid[1].std(ddof=1)),
        "group2_ortalama": float(valid[2].mean()),
        "group2_ss": float(valid[2].std(ddof=1)),
        "esler_arasi_korelasyon": float(corr.statistic) if corr else None,
        "esler_arasi_korelasyon_p": float(corr.pvalue) if corr else None,
        "fark_yonu": "group2-group1",
        "ortalama_fark": float(diff.mean()),
        "fark_ss": float(diff.std(ddof=1)),
        "t": float(test.statistic),
        "df": int(test.df),
        "p_iki_yonlu": float(test.pvalue),
        "ga95_alt": float(ci[0]),
        "ga95_ust": float(ci[1]),
    }


def independent_summary(path: Path) -> dict:
    df = pd.read_csv(path)
    dose1 = df.loc[df["dose"].eq(1.0)].copy()
    oj = dose1.loc[dose1["supp"].eq("OJ"), "len"]
    vc = dose1.loc[dose1["supp"].eq("VC"), "len"]

    levene = stats.levene(oj, vc, center="mean")
    equal = stats.ttest_ind(oj, vc, equal_var=True)
    welch = stats.ttest_ind(oj, vc, equal_var=False)

    diff = float(oj.mean() - vc.mean())
    se = float(np.sqrt(oj.var(ddof=1) / len(oj) + vc.var(ddof=1) / len(vc)))
    a = oj.var(ddof=1) / len(oj)
    b = vc.var(ddof=1) / len(vc)
    welch_df = float((a + b) ** 2 / (a**2 / (len(oj) - 1) + b**2 / (len(vc) - 1)))
    ci = stats.t.interval(0.95, df=welch_df, loc=diff, scale=se)

    return {
        "tam_veri_n": int(len(df)),
        "dose1_n": int(len(dose1)),
        "oj_n": int(len(oj)),
        "vc_n": int(len(vc)),
        "oj_ortalama": float(oj.mean()),
        "oj_ss": float(oj.std(ddof=1)),
        "vc_ortalama": float(vc.mean()),
        "vc_ss": float(vc.std(ddof=1)),
        "fark_yonu": "OJ-VC",
        "ortalama_fark": diff,
        "levene_f": float(levene.statistic),
        "levene_p": float(levene.pvalue),
        "esit_varyans_t": float(equal.statistic),
        "esit_varyans_df": float(equal.df),
        "esit_varyans_p": float(equal.pvalue),
        "welch_t": float(welch.statistic),
        "welch_df": float(welch.df),
        "welch_p": float(welch.pvalue),
        "welch_ga95_alt": float(ci[0]),
        "welch_ga95_ust": float(ci[1]),
    }


sleep = paired_summary(HERE / "sleep.csv")
sleep_eksik = paired_summary(HERE / "sleep_eksik.csv")
toothgrowth = independent_summary(HERE / "ToothGrowth.csv")

summary = {
    "bolum": "B18",
    "baslik": "IBM SPSS Uygulamaları",
    "sleep_esli_test": sleep,
    "toothgrowth_dose1_bagimsiz_test": toothgrowth,
    "sleep_eksik_esli_test": sleep_eksik,
    "durum_deneyi": {
        "sleep_uzun_satir": sleep["satir_sayisi"],
        "sleep_gecerli_cift": sleep["gecerli_cift"],
        "toothgrowth_tam_n": toothgrowth["tam_veri_n"],
        "toothgrowth_dose1_n": toothgrowth["dose1_n"],
        "sleep_eksik_gecerli_cift": sleep_eksik["gecerli_cift"],
        "yorum": "Dosya satır sayısı, aktif filtre ve geçerli analiz birimi aynı kavram değildir; ağırlık yeni bağımsız birim yaratmaz.",
    },
    "dogrulama_notu": "Bu Python analizi SPSS yazılımının çalıştırıldığı anlamına gelmez; SPSS çıktıları analiz.sps ile ayrıca kontrol edilmelidir.",
}

(OUT / "ozet.json").write_text(
    json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)

print(json.dumps(summary, ensure_ascii=False, indent=2))
