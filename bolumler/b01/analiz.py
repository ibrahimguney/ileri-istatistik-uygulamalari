from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE / "veri.csv"
RESULTS = HERE / "sonuclar"
FIGURES = HERE / "grafikler"


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)

    df = pd.read_csv(DATA)

    # Temel bütünlük ve veri tanıma kontrolleri
    n = int(len(df))
    missing_total = int(df.isna().sum().sum())
    school_levels = sorted(df["school"].astype(str).unique().tolist())

    # Frekans ve yüzde tablosu
    freq = df["G3"].value_counts().sort_index()
    pct = (freq / n * 100).round(8)
    freq_table = [
        {"G3": int(score), "frekans": int(freq.loc[score]), "yuzde": float(pct.loc[score])}
        for score in freq.index
    ]

    # Kitaptaki öğretim örneği: N=80, n=10, başlangıç=3, aralık=8.
    # Başlangıç 3 gösterim için sabittir; rastgele çekildiği iddia edilmez.
    systematic_rows = list(range(3, n + 1, 8))
    systematic = df[df["kaynak_satir"].isin(systematic_rows)].copy()

    summary = {
        "bolum": "B01",
        "baslik": "İstatistiksel Düşünme: Sorudan Kanıta",
        "veri": {
            "n": n,
            "eksik_hucre": missing_total,
            "school_duzeyleri": school_levels,
            "kaynak_satir_benzersiz": bool(df["kaynak_satir"].is_unique),
        },
        "G1": {
            "min": int(df["G1"].min()),
            "max": int(df["G1"].max()),
            "ortalama": float(df["G1"].mean()),
        },
        "G3": {
            "min": int(df["G3"].min()),
            "max": int(df["G3"].max()),
            "toplam": int(df["G3"].sum()),
            "ortalama": float(df["G3"].mean()),
            "medyan": float(df["G3"].median()),
            "frekans_yuzde": freq_table,
        },
        "sistematik_secim": {
            "N": 80,
            "hedef_n": 10,
            "baslangic": 3,
            "aralik": 8,
            "kaynak_satirlar": [int(x) for x in systematic["kaynak_satir"].tolist()],
            "n": int(len(systematic)),
            "G1_ortalama": float(systematic["G1"].mean()),
            "G3_ortalama": float(systematic["G3"].mean()),
            "not": "Kitaptaki öğretim örneğidir; başlangıç 3 gösterim için sabitlenmiştir ve ilk 80 kaydı temsili örnekleme dönüştürmez.",
        },
    }

    (RESULTS / "ozet.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    freq_df = pd.DataFrame(freq_table)
    freq_df.to_csv(RESULTS / "g3_frekans_yuzde.csv", index=False)
    systematic.to_csv(RESULTS / "sistematik_ornek.csv", index=False)

    # Nicel dağılım için basit histogram
    fig, ax = plt.subplots(figsize=(7, 4.5))
    bins = range(int(df["G3"].min()), int(df["G3"].max()) + 2)
    ax.hist(df["G3"], bins=bins, align="left", edgecolor="black")
    ax.set_xlabel("G3 yıl sonu notu")
    ax.set_ylabel("Frekans")
    ax.set_title("B01 — G3 dağılımı")
    fig.tight_layout()
    fig.savefig(FIGURES / "g3_dagilimi.png", dpi=150)
    plt.close(fig)

    print("B01 analizi tamamlandı.")
    print(f"n={n}, eksik hücre={missing_total}, G1 ortalama={df['G1'].mean():.4f}, G3 ortalama={df['G3'].mean():.4f}")
    print(f"Sistematik seçim n={len(systematic)}, G3 ortalama={systematic['G3'].mean():.4f}")


if __name__ == "__main__":
    main()
