import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import pandas as pd

ITEMS = [f"{prefix}{number}" for prefix in ("A", "C") for number in range(1, 6)]
REVERSE = ["A1", "C4", "C5"]
SOURCE_HASH = "8726fd25dbfc685be2d3d726e5511bbb31ba9c7b367b6864eb06e0d8669e6557"


def validate(frame):
    required = ["kaynak_satir", "kaynak_kayit"] + ITEMS
    if list(frame.columns) != required:
        raise ValueError("Beklenen sütunlar ve sıraları korunmalı.")
    for identifier in required[:2]:
        if frame[identifier].isna().any() or frame[identifier].duplicated().any():
            raise ValueError("Kaynak anahtarı eksik veya yinelenmiş.")
    values = frame[ITEMS]
    if not all(pd.api.types.is_numeric_dtype(values[item]) for item in ITEMS):
        raise ValueError("Sayısal olmayan madde: otomatik eksik kodlamayın.")
    if (values.notna() & ~values.isin(range(1, 7))).any().any():
        raise ValueError("Madde yanıtı 1--6 tamsayı veya eksik olmalı.")


def score(values, minimum):
    if not 1 <= minimum <= values.shape[1]:
        raise ValueError("Geçerli madde eşiği hatalı.")
    return values.mean(axis=1).where(values.count(axis=1) >= minimum)


def expected_failure(operation):
    try:
        operation()
    except (ValueError, pd.errors.MergeError):
        return True
    raise AssertionError("Hatalı örnek sessizce kabul edildi.")


def main():
    base = Path(__file__).resolve().parent
    source = base / "veri.csv"
    original = source.read_bytes()
    normalized = original.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    assert hashlib.sha256(normalized).hexdigest() == SOURCE_HASH
    frame = pd.read_csv(source)
    validate(frame)
    assert len(frame) == 100
    assert frame.kaynak_satir.tolist() == list(range(1, 101))
    output = base / "sonuclar"
    output.mkdir(parents=True, exist_ok=True)
    missing = frame[ITEMS].isna()
    assert int(missing.sum().sum()) == 3
    assert frame.loc[missing.any(axis=1), "kaynak_satir"].tolist() == [63, 66, 90]
    missing_summary = pd.DataFrame({"madde": ITEMS, "eksik": missing.sum().to_numpy(),
                                   "gecerli": frame[ITEMS].count().to_numpy()})
    missing_summary["eksik_yuzde_payda100"] = missing_summary.eksik
    missing_summary.to_csv(output / "eksik_ozeti.csv", index=False)
    patterns = missing.astype(int).astype(str).agg("".join, axis=1).value_counts().sort_index()
    patterns.rename_axis("A1_A5_C1_C5_sirasinda_1_eksik").rename("kayit").to_csv(output / "desenler.csv")
    scored = frame.copy()
    for item in REVERSE:
        scored[item + "_t"] = 7 - frame[item]
    summaries = []
    for prefix in ("A", "C"):
        items = [f"{prefix}{number}" for number in range(1, 6)]
        values = frame[items].copy()
        for item in set(items) & set(REVERSE):
            values[item] = scored[item + "_t"]
        scored[prefix + "_n"] = values.count(axis=1)
        for minimum in (5, 4):
            column = prefix + f"_ort{minimum}"
            scored[column] = score(values, minimum)
            summaries.append({"puan": column, "gecerli": int(scored[column].count()),
                              "ortalama": float(scored[column].mean())})
        scored[prefix + "_top5"] = values.sum(axis=1, min_count=5)
        np.testing.assert_allclose(scored[prefix + "_top5"], 5 * scored[prefix + "_ort5"], equal_nan=True)
    pd.DataFrame(summaries).to_csv(output / "puan_ozeti.csv", index=False)
    scored.to_csv(base / "puanlar.csv", index=False)
    long = frame.melt(id_vars=["kaynak_satir", "kaynak_kayit"], value_vars=ITEMS,
                      var_name="madde", value_name="yanit")
    assert len(long) == 1000 and long.yanit.count() == 997
    assert not long.duplicated(["kaynak_satir", "madde"]).any()
    restored = long.pivot(index="kaynak_satir", columns="madde", values="yanit")[ITEMS]
    np.testing.assert_allclose(restored, frame[ITEMS], equal_nan=True)
    long.to_csv(base / "uzun.csv", index=False)
    pairs = frame[ITEMS].notna().astype(int).T.dot(frame[ITEMS].notna().astype(int))
    pairs.to_csv(output / "cift_paydalari.csv")
    zscore = (scored.A_ort5 - scored.A_ort5.mean()) / scored.A_ort5.std(ddof=1)
    np.testing.assert_allclose([zscore.mean(), zscore.std(ddof=1)], [0, 1], atol=1e-12)
    scored.loc[:, ["kaynak_satir"]].assign(A_z99=zscore).to_csv(output / "standartlastirma.csv", index=False)
    observed = frame.C1.dropna()
    filled = frame.C1.fillna(observed.mean())
    np.testing.assert_allclose(filled.mean(), observed.mean())
    np.testing.assert_allclose(filled.var(ddof=1), observed.var(ddof=1) * 98 / 99)
    synthetic = pd.DataFrame([[np.nan] * 5, [6, np.nan, np.nan, np.nan, np.nan], [6, 4, 5, 3, np.nan]])
    assert synthetic.sum(axis=1).iloc[0] == 0
    assert synthetic.mean(axis=1).iloc[1] == 6
    assert score(synthetic, 4).isna().tolist() == [True, True, False]
    np.testing.assert_allclose(score(synthetic, 4).iloc[2], 4.5)
    invalid = frame.copy(); invalid.loc[0, "A1"] = 99
    fractional = frame.copy(); fractional.loc[0, "A2"] = 2.5
    text = frame.copy(); text["A1"] = text.A1.astype(object); text.loc[0, "A1"] = "yanlis"
    duplicate = pd.concat([frame, frame.iloc[[0]]], ignore_index=True)
    checks = {"99_reddedildi": expected_failure(lambda: validate(invalid)),
              "kesir_reddedildi": expected_failure(lambda: validate(fractional)),
              "metin_reddedildi": expected_failure(lambda: validate(text)),
              "anahtar_tekrari_reddedildi": expected_failure(lambda: validate(duplicate)),
              "bos_ve_tek_maddeli_puan_engellendi": True}
    left = pd.DataFrame({"id": [1, 2], "deger": [10, 20]})
    right = pd.DataFrame({"id": [1, 1, 2], "etiket": ["a", "b", "c"]})
    checks["coklayan_birlestirme_reddedildi"] = expected_failure(
        lambda: left.merge(right, on="id", validate="one_to_one"))
    checks["sessiz_pivot_ozetlemesi_engellendi"] = expected_failure(
        lambda: pd.concat([long, long.iloc[[0]]]).pivot(index="kaynak_satir", columns="madde", values="yanit"))
    dictionary = [{"alan": item, "tur": "ordinal tamsayi", "gecerli": "1,2,3,4,5,6",
                   "eksik": "bos hucre", "ters": item in REVERSE, "kaynak": "psych/bfi anahtari"} for item in ITEMS]
    pd.DataFrame(dictionary).to_csv(output / "veri_sozlugu.csv", index=False)
    log = [{"adim": "aktarim", "giren": 100, "cikan": 100, "karar": "Ham arşiv değişmedi; hash denetlendi."},
           {"adim": "aralik_anahtar", "giren": 100, "cikan": 100, "karar": "Geçersiz değer veya anahtar tekrarı yok."},
           {"adim": "eksik", "giren": 100, "cikan": 100, "karar": "3 boş madde korundu; atama yapılmadı."},
           {"adim": "ters", "giren": 100, "cikan": 100, "karar": "A1/C4/C5 yeni sütunlarda 7-x; ham sütunlar korundu."},
           {"adim": "puan", "giren": 100, "cikan": 100, "karar": "A5tam n99, C5tam n98, ortak n97; 4/5 duyarlılık n100."}]
    pd.DataFrame(log).to_csv(output / "karar_gunlugu.csv", index=False)
    result = {"kaynak_hash_normalize": SOURCE_HASH, "kayit": 100, "madde_hucresi": 1000,
              "eksik_hucre": 3, "eksik_hucre_yuzde": 0.3, "eksikli_kayit": 3,
              "ortak_tam": int((~missing.any(axis=1)).sum()), "puanlar": summaries,
              "eksikli_kayit_puanlari": scored.loc[missing.any(axis=1),
                  ["kaynak_satir", "A_n", "A_ort4", "C_n", "C_ort4"]].to_dict("records"),
              "ortalama_atama_karsi_ornegi_C1": {"gozlenen_n": 99, "ortalama": float(observed.mean()),
                  "gozlenen_varyans": float(observed.var(ddof=1)), "doldurulmus_varyans": float(filled.var(ddof=1))},
              "kurgu_denetimleri": checks, "kurgu_kontrolsuz_join_satir": len(left.merge(right, on="id")),
              "surum": {"numpy": np.__version__, "pandas": pd.__version__, "matplotlib": matplotlib.__version__},
              "R_SPSS_calistirildi": False}
    (output / "ozet.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.5), gridspec_kw={"width_ratios": [1.2, 1]})
    axes[0].imshow(missing.to_numpy(), aspect="auto", interpolation="nearest", cmap=ListedColormap(["#eeeeee", "#8f1d35"]), vmin=0, vmax=1)
    axes[0].set_xticks(range(10), ITEMS, rotation=45)
    axes[0].set_yticks([0, 24, 49, 74, 99], [1, 25, 50, 75, 100])
    axes[0].set_ylabel("Kaynak sırası"); axes[0].set_title("100 kayıt × 10 madde; kırmızı = eksik")
    axes[1].bar(["A: 5/5", "C: 5/5", "A ve C\nortak", "A/C: 4/5"], [99, 98, 97, 100], color="#555566")
    axes[1].set_ylim(0, 108); axes[1].set_ylabel("Puan üretilebilen kayıt")
    for index, count in enumerate([99, 98, 97, 100]): axes[1].text(index, count+1, str(count), ha="center")
    fig.tight_layout()
    figure = base / "grafikler/b03-eksik-puan-paydalari.pdf"
    figure.parent.mkdir(exist_ok=True)
    fig.savefig(figure, metadata={"CreationDate": None, "ModDate": None})
    plt.close(fig)
    assert source.read_bytes() == original
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()