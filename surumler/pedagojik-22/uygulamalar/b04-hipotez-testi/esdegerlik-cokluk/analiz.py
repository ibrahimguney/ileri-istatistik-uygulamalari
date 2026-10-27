"""Eşdeğerlik ve çokluk; sleep sınırları ve p ailesi yalnız öğretim içindir."""
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.weightstats import ttost_paired


def tost(n, mean, sd, delta, alpha=.05):
    if (not isinstance(n, (int, np.integer)) or n < 2 or
        not np.isfinite([mean, sd, delta, alpha]).all() or sd <= 0 or delta <= 0 or not 0 < alpha < .5):
        raise ValueError('n>=2 tamsayı, sonlu ortalama, pozitif s/delta ve 0<alfa<.5 gerekir')
    se = sd/np.sqrt(n)
    df = n-1
    p_lower = float(stats.t.sf((mean+delta)/se,df))
    p_upper = float(stats.t.cdf((mean-delta)/se,df))
    p = max(p_lower,p_upper)
    margin = float(stats.t.ppf(1-alpha,df)*se)
    ci = [float(mean-margin),float(mean+margin)]
    equivalent = p < alpha
    assert equivalent == (ci[0] > -delta and ci[1] < delta)
    return {'n':int(n),'mean':float(mean),'sd':float(sd),'se':float(se),'df':int(df),
            'delta':float(delta),'alpha':alpha,'p_lower':p_lower,'p_upper':p_upper,
            'p_tost':p,'CI_1_minus_2alpha':ci,'equivalent_under_model':bool(equivalent),
            'p_difference_two_sided':float(2*stats.t.sf(abs(mean/se),df))}


def holm_adjust(values):
    p = np.asarray(values,dtype=float)
    if p.ndim != 1 or not len(p) or not np.isfinite(p).all() or ((p<0)|(p>1)).any():
        raise ValueError('Sonlu, boş olmayan bir boyutlu [0,1] p dizisi gerekir')
    order = np.argsort(p,kind='stable')
    adjusted_sorted = np.minimum(1,np.maximum.accumulate((len(p)-np.arange(len(p)))*p[order]))
    result = np.empty_like(p)
    result[order] = adjusted_sorted
    return result


def main():
    directory = Path(__file__).parent
    parent = directory.parent
    source = parent.parent/'b06-parametrik-testler/kaynak/sleep.csv'
    original = source.read_bytes()
    source_hash = 'adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e'
    assert hashlib.sha256(original.replace(b'\r\n',b'\n').rstrip(b'\n')+b'\n').hexdigest() == source_hash
    spec = importlib.util.spec_from_file_location('b04_original',parent/'analiz.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    paired = module.pair_data(pd.read_csv(source))
    d = paired.fark.to_numpy()
    # Sınırlar geriye dönük öğretim senaryolarıdır; klinik tolerans değildir.
    real = [{'label':'sleep_delta1_teaching',**tost(len(d),float(d.mean()),float(d.std(ddof=1)),1)},
            {'label':'sleep_delta3_teaching',**tost(len(d),float(d.mean()),float(d.std(ddof=1)),3)}]
    for row in real:
        independent = ttost_paired(d, np.zeros_like(d), -row['delta'], row['delta'])
        np.testing.assert_allclose([row['p_tost'],row['p_lower'],row['p_upper']], [independent[0],independent[1][1],independent[2][1]])
    toy = [{'label':'summary_n25_synthetic',**tost(25,0,10,5)},
           {'label':'summary_n4_synthetic',**tost(4,0,10,5)}]
    assert real[0]['equivalent_under_model'] is False
    assert real[1]['equivalent_under_model'] is True
    assert toy[0]['equivalent_under_model'] is True and toy[1]['equivalent_under_model'] is False
    p = np.array([.20,.004,.024,.012])
    adjusted = holm_adjust(p)
    np.testing.assert_allclose(adjusted,multipletests(p,method='holm')[1])
    bonferroni = np.minimum(1,4*p)
    family = [{'comparison':f'H{i+1}','p_raw':float(x),'p_holm':float(h),'p_bonferroni':float(b),
               'reject_holm_05':bool(h<.05),'reject_bonferroni_05':bool(b<.05)}
              for i,(x,h,b) in enumerate(zip(p,adjusted,bonferroni))]
    output = directory/'sonuclar'
    output.mkdir(exist_ok=True)
    pd.DataFrame(real+toy).to_csv(output/'esdegerlik.csv',index=False)
    pd.DataFrame(family).to_csv(output/'kurgu-holm-ailesi.csv',index=False)
    result = {'scope':'Yalnız model altında öğretim; klinik sınır veya gerçek çoklu test ailesi yok',
              'source_normalized_sha256':source_hash,'sleep_teaching_bounds':real,
              'synthetic_summaries_no_raw_data':toy,'synthetic_p_family':family,
              'holm_strong_FWER_assumes_valid_marginal_p':True,
              'versions':{'numpy':np.__version__,'pandas':pd.__version__}}
    (output/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    assert source.read_bytes() == original
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
