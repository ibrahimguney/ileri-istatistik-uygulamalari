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

SOURCE_HASH = "adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e"
SEED = 20260906
REPEATS = 20000


def mean_test(count, mean, deviation, reference=0, alpha=.05):
    if count < 2 or deviation <= 0 or not np.isfinite([mean, deviation, reference]).all():
        raise ValueError("Sonlu ortalama, pozitif s ve en az iki kayıt gerekli.")
    degrees = count - 1
    error = deviation / np.sqrt(count)
    statistic = (mean - reference) / error
    critical = stats.t.ppf(1-alpha/2, degrees)
    return {"n": int(count), "ortalama": float(mean), "s": float(deviation), "referans": reference,
            "SH": float(error), "t": float(statistic), "sd": int(degrees),
            "p_iki": float(2*stats.t.sf(abs(statistic), degrees)),
            "p_sag": float(stats.t.sf(statistic, degrees)), "p_sol": float(stats.t.cdf(statistic, degrees)),
            "kritik_iki": float(critical), "GA95": [float(mean-critical*error), float(mean+critical*error)],
            "fark_GA95": [float(mean-reference-critical*error), float(mean-reference+critical*error)],
            "alt_sinir95_tek": float(mean-stats.t.ppf(1-alpha, degrees)*error),
            "d": float((mean-reference)/deviation)}


def pair_data(frame):
    if list(frame.columns) != ["kaynak_satir", "extra", "group", "ID"]:
        raise ValueError("Beklenmeyen sütunlar.")
    if frame.isna().any().any() or frame.duplicated(["ID", "group"]).any():
        raise ValueError("Eksik veya yinelenen kişi-koşul kaydı.")
    if len(frame) != 20 or set(frame.ID) != set(range(1,11)) or set(frame.group) != {1,2}:
        raise ValueError("Beklenen 10 tam çift bulunamadı.")
    wide = frame.pivot(index="ID", columns="group", values="extra").sort_index()
    if wide.isna().any().any():
        raise ValueError("Eşleştirmede eksik koşul.")
    return wide.rename(columns={1: "kosul1", 2: "kosul2"}).assign(fark=lambda data: data.kosul2-data.kosul1)


def simulate():
    generator = np.random.default_rng(SEED)
    size = 25
    critical = stats.t.ppf(.975, size-1)
    rows = []
    for effect in (0., .5):
        samples = generator.normal(loc=effect, scale=1, size=(REPEATS,size))
        averages = samples.mean(axis=1)
        errors = samples.std(axis=1, ddof=1)/np.sqrt(size)
        statistics = averages/errors
        rejected = np.abs(statistics) > critical
        covered_null = (averages-critical*errors <= 0) & (averages+critical*errors >= 0)
        assert np.array_equal(rejected, ~covered_null)
        covered_true = (averages-critical*errors <= effect) & (averages+critical*errors >= effect)
        selected_direction = stats.t.sf(np.abs(statistics), size-1) < .05
        theoretical = stats.nct.sf(critical,size-1,effect*np.sqrt(size))+stats.nct.cdf(-critical,size-1,effect*np.sqrt(size))
        rate = rejected.mean()
        mc_error = np.sqrt(rate*(1-rate)/REPEATS)
        assert abs(rate-theoretical) < 5*np.sqrt(theoretical*(1-theoretical)/REPEATS)
        rows.append({"d": effect, "n": size, "tekrar": REPEATS, "red_sayisi": int(rejected.sum()),
                     "red_orani": float(rate), "kuramsal_red": float(theoretical), "MC_SH": float(mc_error),
                     "gercek_ortalama_kapsama": float(covered_true.mean()),
                     "veriden_yon_secip_tek_p_red": float(selected_direction.mean())})
    return rows


def main():
    base = Path(__file__).resolve().parent
    source = base / "veri.csv"
    original = source.read_bytes()
    normalized = original.replace(b"\r\n",b"\n").rstrip(b"\n")+b"\n"
    assert hashlib.sha256(normalized).hexdigest() == SOURCE_HASH
    frame = pd.read_csv(source)
    wide = pair_data(frame)
    pd.testing.assert_frame_equal(wide, pair_data(frame.sample(frac=1,random_state=17)))
    for bad in (frame.iloc[:-1], pd.concat([frame,frame.iloc[[0]]],ignore_index=True)):
        try:
            pair_data(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("Bozuk eşleştirme kabul edildi.")
    differences = wide.fark.to_numpy()
    result = mean_test(len(wide), differences.mean(), differences.std(ddof=1))
    independent_check = stats.ttest_rel(wide.kosul2,wide.kosul1)
    np.testing.assert_allclose([result['t'],result['p_iki']], [independent_check.statistic,independent_check.pvalue])
    interval = independent_check.confidence_interval(.95)
    np.testing.assert_allclose(result['GA95'], [interval.low,interval.high])
    np.testing.assert_allclose(result['d']*np.sqrt(10), result['t'])
    reversed_result = mean_test(10,-differences.mean(),differences.std(ddof=1))
    np.testing.assert_allclose(reversed_result['p_iki'], result['p_iki'])
    np.testing.assert_allclose(reversed_result['GA95'], -np.asarray(result['GA95'])[::-1])
    np.testing.assert_allclose(stats.ttest_1samp(differences,0).statistic,result['t'])
    covariance = np.cov(wide.kosul1,wide.kosul2,ddof=1)[0,1]
    np.testing.assert_allclose(differences.var(ddof=1),wide.kosul1.var()+wide.kosul2.var()-2*covariance)
    toy_table = np.array([[20,30],[30,20]])
    chi = stats.chi2_contingency(toy_table,correction=False)
    np.testing.assert_allclose(chi.statistic, np.sum((toy_table-chi.expected_freq)**2/chi.expected_freq))
    toys = {"ders_ornegi": mean_test(16,74.5,8,70), "O1_dolum": mean_test(25,496,10,500),
            "I1": mean_test(36,52,12,50)}
    simulations = simulate()
    output = base/'sonuclar'; output.mkdir(parents=True,exist_ok=True)
    wide.to_csv(base/'esli_veri.csv')
    pd.DataFrame(simulations).to_csv(output/'simulasyon.csv',index=False)
    pd.DataFrame([{"senaryo":"sleep_esli",**result}]+[{"senaryo":key,**value} for key,value in toys.items()]).to_csv(output/'testler.csv',index=False)
    pd.DataFrame(toy_table,index=['A','B'],columns=['tercih1','tercih2']).to_csv(output/'kurgu_capraz.csv')
    summary = {"kaynak_hash":SOURCE_HASH,"fark_yonu":"kosul2-kosul1","sleep":result,
               "farklar":differences.tolist(),"fark_kareli_sapmalar_toplami":float(((differences-differences.mean())**2).sum()),
               "kosul_ortalamalari": [float(wide.kosul1.mean()),float(wide.kosul2.mean())],
               "kovaryans":float(covariance),"kurgu_ozetler":toys,
               "kurgu_ki_kare":{"tablo":toy_table.tolist(),"beklenen":chi.expected_freq.tolist(),
                 "ki_kare":float(chi.statistic),"sd":int(chi.dof),"p":float(chi.pvalue),"V":float(np.sqrt(chi.statistic/100))},
               "simulasyon":simulations,"tohum":SEED,"bagimsiz20_test_aile_hatasi":1-.95**20,
               "surum":{"numpy":np.__version__,"scipy":scipy.__version__,"pandas":pd.__version__},
               "R_SPSS_calistirildi":False}
    (output/'ozet.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n', encoding='utf-8')
    fig,axes=plt.subplots(1,2,figsize=(8.2,3.3))
    axes[0].scatter(wide.index,differences,color='#8f1d35')
    axes[0].axhline(0,color='gray',linewidth=.8)
    axes[0].axhline(result['ortalama'],color='#365876',linestyle='--',label='Ortalama = 1.58')
    axes[0].set(xlabel='Kaynak ID',ylabel='Koşul 2 − koşul 1 (saat)',xticks=[1,3,5,7,9,10])
    axes[0].legend(fontsize=8)
    grid=np.linspace(-7,7,2001); density=stats.t.pdf(grid,9)
    axes[1].plot(grid,density,color='#555566')
    axes[1].fill_between(grid,0,density,where=np.abs(grid)>=abs(result['t']),color='#8f1d35',alpha=.8,label='İki yönlü p alanı')
    for direction in (-1,1):
        axes[1].axvline(direction*result['kritik_iki'],color='#365876',linestyle='--',linewidth=.9)
        axes[1].axvline(direction*abs(result['t']),color='#8f1d35',linewidth=.8)
    axes[1].set(xlabel='t istatistiği',ylabel='H0 altında yoğunluk',title='sd=9; kesikli çizgi ±2.262')
    axes[1].legend(fontsize=8)
    fig.tight_layout()
    figures = base / 'grafikler'
    figures.mkdir(exist_ok=True)
    fig.savefig(figures/'b04-test-mantigi.pdf',metadata={'CreationDate':None,'ModDate':None})
    plt.close(fig)
    assert source.read_bytes()==original
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()