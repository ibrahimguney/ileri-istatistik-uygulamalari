import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

SOURCE_HASH = "51dcab9aeaa121123dd28a00156d4dfa398c38eecad69bd5699ae4cea03e5ee9"
SEED = 20260906
BANDS = ["0-9", "10-14", "15-20"]


def main():
    directory = Path(__file__).parent
    source = directory.parent / "b12-regresyon/kaynak/uci-portekizce-ilk80-notlar.csv"
    original = source.read_bytes()
    assert hashlib.sha256(original.rstrip(b"\n") + b"\n").hexdigest() == SOURCE_HASH
    data = pd.read_csv(source)
    assert list(data.columns) == ["kaynak_satir", "school", "G1", "G3"]
    assert len(data) == 80 and not data.isna().any().any()
    np.testing.assert_array_equal(data.kaynak_satir, np.arange(1, 81))
    assert data.school.eq("GP").all()
    assert data[["G1", "G3"]].apply(lambda column: column.between(0, 20).all()).all()
    assert data[["G1", "G3"]].eq(data[["G1", "G3"]].round()).all().all()
    output = directory / "sonuclar"
    output.mkdir(exist_ok=True)
    data["G3_bant"] = pd.cut(data.G3, [-.5, 9.5, 14.5, 20.5], labels=BANDS)
    data.to_csv(directory / "notlar.csv", index=False)
    frequency = data.G3.value_counts().reindex(range(21), fill_value=0).sort_index()
    bands = data.G3_bant.value_counts(sort=False).reindex(BANDS)
    assert int(frequency.sum()) == int(bands.sum()) == len(data)
    np.testing.assert_array_equal(bands, [frequency.loc[:9].sum(), frequency.loc[10:14].sum(), frequency.loc[15:].sum()])
    pd.DataFrame({"G3": frequency.index, "frekans": frequency.values,
                  "yuzde": 100 * frequency.values / len(data)}).to_csv(output / "not_frekanslari.csv", index=False)
    pd.DataFrame({"bant": BANDS, "frekans": bands.values,
                  "yuzde": 100 * bands.values / len(data)}).to_csv(output / "bant_frekanslari.csv", index=False)
    population_mean = float(data.G3.sum() / len(data))
    assert population_mean == float(data.G3.mean())
    generator = np.random.default_rng(SEED)
    random_ids = np.sort(generator.choice(data.kaynak_satir.to_numpy(), size=10, replace=False))
    selected = {"basit_rastgele": random_ids.tolist(), "sistematik_r3": list(range(3, 81, 8)),
                "ilk10": list(range(1, 11))}
    sampling = []
    for method, identifiers in selected.items():
        subset = data.loc[data.kaynak_satir.isin(identifiers)]
        assert len(subset) == 10 and subset.kaynak_satir.is_unique
        subset.to_csv(output / f"ornek_{method}.csv", index=False)
        sampling.append({"yontem": method, "satirlar": identifiers, "n": len(subset),
                         "ortalama": float(subset.G3.mean()), "cerceve_ortalamasindan_fark": float(subset.G3.mean() - population_mean)})
    systematic = []
    included = np.zeros(80, dtype=int)
    for start in range(1, 9):
        positions = np.arange(start - 1, 80, 8)
        included[positions] += 1
        systematic.append({"baslangic": start, "n": len(positions), "ortalama": float(data.iloc[positions].G3.mean())})
    np.testing.assert_array_equal(included, np.ones(80, dtype=int))
    np.testing.assert_allclose(np.mean([row["ortalama"] for row in systematic]), population_mean)
    pd.DataFrame(systematic).to_csv(output / "sekiz_baslangic.csv", index=False)
    periodic = np.tile([1, 0, 0, 0, 0, 0, 0, 0], 10)
    periodic_means = [float(periodic[start::8].mean()) for start in range(8)]
    assert np.mean(periodic_means) == periodic.mean() == .125
    pd.DataFrame({"kurgusal_sira": np.arange(1, 81), "kurgusal_gosterge": periodic}).to_csv(
        directory / "dongusellik_kurgu.csv", index=False)
    missing_demo = data.copy()
    missing_demo["G3"] = missing_demo.G3.astype(float)
    missing_demo.loc[missing_demo.kaynak_satir.isin([1, 2, 3, 4]), "G3"] = np.nan
    missing_demo["G3_bant"] = pd.cut(missing_demo.G3, [-.5, 9.5, 14.5, 20.5], labels=BANDS)
    missing_demo.to_csv(directory / "eksik_veri_ogretim.csv", index=False)
    valid = int(missing_demo.G3.notna().sum())
    high = int(missing_demo.G3.ge(15).sum())
    assert valid == 76 and high == 15 and missing_demo.G3.isna().sum() == 4
    long_data = data.melt(id_vars=["kaynak_satir", "school"], value_vars=["G1", "G3"],
                          var_name="donem", value_name="not")
    assert len(long_data) == 160 and long_data.kaynak_satir.nunique() == 80
    restored = long_data.pivot(index="kaynak_satir", columns="donem", values="not")
    np.testing.assert_array_equal(restored[["G1", "G3"]], data[["G1", "G3"]])
    long_data.to_csv(directory / "notlar_uzun.csv", index=False)
    stem_source = [21, 24, 24, 26, 27, 27, 30, 32, 38, 41]
    stem_leaves = {str(stem): [value % 10 for value in stem_source if value // 10 == stem] for stem in [2, 3, 4]}
    assert [int(stem) * 10 + leaf for stem, leaves in stem_leaves.items() for leaf in leaves] == stem_source
    results = {"source_normalized_sha256": SOURCE_HASH, "source_raw_sha256": hashlib.sha256(original).hexdigest(),
               "remote_cells_verified": False, "seed": SEED, "n": len(data), "school_counts": data.school.value_counts().to_dict(),
               "grade_sum": int(data.G3.sum()), "grade_mean": population_mean,
               "grade_range": [int(data.G3.min()), int(data.G3.max())], "G1_zero_count": int(data.G1.eq(0).sum()),
               "band_counts": {str(key): int(value) for key, value in bands.items()},
               "band_percent": {str(key): float(100 * value / len(data)) for key, value in bands.items()},
               "samples": sampling, "systematic_starts": systematic,
               "periodic_example_is_synthetic": True, "periodic_means": periodic_means,
               "missing_example_is_modified_copy": True, "masked_rows": [1, 2, 3, 4],
               "missing_example": {"valid_n": valid, "high_count": high, "percent_all": 100 * high / len(data),
                                   "percent_valid": 100 * high / valid},
               "long_rows": len(long_data), "independent_students_not_increased": True,
               "synthetic_stem_leaves": stem_leaves,
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "matplotlib": matplotlib.__version__}}
    (output / "ozet.json").write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.1), constrained_layout=True)
    axes[0].bar(BANDS, bands.values, color="#781e2d")
    for position, count in enumerate(bands.values):
        axes[0].text(position, count + 1, str(count), ha="center")
    axes[0].set(xlabel="Öğretim amaçlı G3 bandı", ylabel="Kayıt sayısı", title="(a) Sıralı kategoriler", ylim=(0, 72))
    counts, _, _ = axes[1].hist(data.G3, bins=np.arange(-.5, 21.5, 1), color="#55555c", edgecolor="white")
    np.testing.assert_array_equal(counts, frequency.values)
    axes[1].set(xlabel="G3 (0–20 puan)", ylabel="Kayıt sayısı", title="(b) Bir puanlık sınıflar", xlim=(-.5, 20.5), xticks=[0, 5, 10, 15, 20])
    figures = directory.parent.parent / "assets_figures"
    figures.mkdir(exist_ok=True)
    figure.savefig(figures / "b01-veri-grafikleri.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert source.read_bytes() == original
    print(json.dumps(results, indent=2, ensure_ascii=False))
    print("B01 kontrolleri geçti: frekans, payda, seçim, sekiz başlangıç, uzun/geniş dönüşüm ve kurgu ayrımı.")


if __name__ == "__main__":
    main()