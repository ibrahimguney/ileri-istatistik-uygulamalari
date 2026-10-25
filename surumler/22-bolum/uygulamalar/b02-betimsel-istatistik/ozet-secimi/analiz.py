"""Betimsel hedefler, ampirik dağılım ve eşleşmiş değişim; çıkarım yapılmaz."""
import hashlib
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import trim_mean

SOURCE_HASH = '51dcab9aeaa121123dd28a00156d4dfa398c38eecad69bd5699ae4cea03e5ee9'


def trimmed_mean(values, proportion=.2):
    y = np.sort(np.asarray(values, dtype=float))
    if not len(y) or not np.isfinite(y).all() or not 0 <= proportion < .5:
        raise ValueError('Sonlu, boş olmayan veri ve 0 <= oran < .5 gerekir')
    g = int(np.floor(len(y) * proportion))
    return float(y[g:len(y)-g].mean())


def ecdf(values, at):
    y = np.asarray(values, dtype=float)
    if not len(y) or not np.isfinite(y).all():
        raise ValueError('Sonlu, boş olmayan veri gerekir')
    return float(np.mean(y <= at))


def main():
    directory = Path(__file__).parent
    source = directory.parents[1] / 'b12-regresyon/kaynak/uci-portekizce-ilk80-notlar.csv'
    original = source.read_bytes()
    assert hashlib.sha256(original.rstrip(b'\n') + b'\n').hexdigest() == SOURCE_HASH
    data = pd.read_csv(source)
    assert len(data) == 80 and not data[['G1', 'G3']].isna().any().any()
    rows = []
    for name in ['G1', 'G3']:
        y = data[name].to_numpy(dtype=float)
        ordered = np.sort(y)
        mean, median, trimmed = float(y.mean()), float(np.median(y)), trimmed_mean(y)
        np.testing.assert_allclose(trimmed, trim_mean(y, .2))
        # Ortalama kare kaybını; medyan mutlak kaybı en aza indirir.
        candidates = np.r_[np.linspace(y.min(), y.max(), 401), mean, median, trimmed]
        square_loss = np.array([np.sum((y-a)**2) for a in candidates])
        absolute_loss = np.array([np.sum(abs(y-a)) for a in candidates])
        assert np.sum((y-mean)**2) <= square_loss.min() + 1e-9
        assert np.sum(abs(y-median)) <= absolute_loss.min() + 1e-9
        rows.append({'variable': name, 'n': len(y), 'mean': mean, 'median': median,
                     'trimmed_mean_20_percent_each_tail': trimmed,
                     'trimmed_each_tail': 16, 'trimmed_retained': 48,
                     'Q3_type7': float(np.quantile(y, .75, method='linear')),
                     'Q3_inverse_ecdf': float(ordered[int(np.ceil(.75*len(y)))-1])})
    g3 = data.G3.to_numpy()
    at15 = int(np.sum(g3 == 15))
    above15 = int(np.sum(g3 > 15))
    atleast15 = int(np.sum(g3 >= 15))
    assert (at15, above15, atleast15) == (6, 9, 15)
    np.testing.assert_allclose(1-ecdf(g3, 15), above15/80)
    np.testing.assert_allclose(1-float(np.mean(g3 < 15)), atleast15/80)
    diff = data.G3.to_numpy() - data.G1.to_numpy()
    np.testing.assert_allclose(diff.mean(), data.G3.mean()-data.G1.mean())
    values, counts = np.unique(diff, return_counts=True)
    # Gerçek çeyrek farkı ortalama/medyan sırasını değiştirebilir; kurgu ayrıdır.
    toy_first = np.array([1, 2, 100])
    toy_last = np.array([2, 100, 101])
    toy = {'first': toy_first.tolist(), 'last': toy_last.tolist(),
           'median_of_paired_differences': float(np.median(toy_last-toy_first)),
           'difference_of_medians': float(np.median(toy_last)-np.median(toy_first)),
           'synthetic_not_grades': True}
    assert toy['median_of_paired_differences'] == 1 and toy['difference_of_medians'] == 98
    output = directory/'sonuclar'
    output.mkdir(exist_ok=True)
    pd.DataFrame(rows).to_csv(output/'konum-hedefleri.csv', index=False)
    pd.DataFrame({'difference_G3_G1': values, 'count': counts, 'percent': 100*counts/80}).to_csv(output/'eslesmis-farklar.csv', index=False)
    pd.DataFrame({'grade': np.arange(21), 'F_G3': [ecdf(g3, x) for x in range(21)]}).to_csv(output/'ampirik-dagilim.csv', index=False)
    results = {'scope': 'İlk 80 GP kaydının betimi; güven aralığı, test veya nedensel etki değil',
               'source_normalized_sha256': SOURCE_HASH, 'location_targets': rows,
               'threshold15': {'equal': at15, 'greater': above15, 'at_least': atleast15,
                               'F15': ecdf(g3, 15), 'F15_left': float(np.mean(g3 < 15)),
                               'percent_greater': 100*above15/80, 'percent_at_least': 100*atleast15/80},
               'paired': {'n': 80, 'mean_difference': float(diff.mean()), 'median_difference': float(np.median(diff)),
                          'increased': int(np.sum(diff>0)), 'unchanged': int(np.sum(diff==0)), 'decreased': int(np.sum(diff<0))},
               'synthetic_median_counterexample': toy,
               'versions': {'numpy': np.__version__, 'pandas': pd.__version__}}
    (output/'ozet.json').write_text(json.dumps(results, ensure_ascii=False, indent=2)+'\n')
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9})
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3), constrained_layout=True)
    for name,color in [('G1','#55555c'),('G3','#781e2d')]:
        y = np.sort(data[name].to_numpy())
        axes[0].step(np.r_[-.5,y,20.5], np.r_[0,np.arange(1,81)/80,1], where='post', label=name,color=color)
    axes[0].set(xlabel='Not (0–20)',ylabel='Ampirik birikimli oran',xlim=(-.5,20.5),ylim=(0,1.02))
    axes[0].legend()
    axes[1].bar(values,counts,color=['#55555c' if v<0 else '#999999' if v==0 else '#781e2d' for v in values])
    axes[1].set(xlabel='Eşleşmiş fark: G3 − G1 (puan)',ylabel='Kayıt sayısı',xticks=values)
    figures = directory.parents[2]/'assets_figures'
    fig.savefig(figures/'b02-ampirik-eslesmis.pdf',metadata={'CreationDate':None,'ModDate':None})
    plt.close(fig)
    assert source.read_bytes() == original
    print(json.dumps(results,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
