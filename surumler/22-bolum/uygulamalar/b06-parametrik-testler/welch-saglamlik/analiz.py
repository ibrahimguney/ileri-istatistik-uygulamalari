"""Welch/Student kalibrasyon kurgusu ve gerçek ToothGrowth'ta Yuen duyarlılığı."""
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

SEED = 20261025
REPETITIONS = 200000


def yuen(first,second,trim=.2):
    if not np.isfinite(trim) or not 0 <= trim < .5:
        raise ValueError('Kırpma oranı [0,.5) arasında olmalı')
    parts = []
    for values in [first,second]:
        y = np.sort(np.asarray(values,dtype=float))
        if y.ndim != 1 or len(y)<2 or not np.isfinite(y).all():
            raise ValueError('Sonlu bir boyutlu en az iki gözlem gerekir')
        g = int(np.floor(trim*len(y)))
        h = len(y)-2*g
        if h<2:
            raise ValueError('Kırpma sonrası en az iki değer gerekir')
        winsor = np.clip(y,y[g],y[len(y)-g-1])
        ss = float(np.sum((winsor-winsor.mean())**2))
        parts.append({'n':len(y),'g':g,'h':h,'trimmed_mean':float(y[g:len(y)-g].mean()),
                      'winsor_SS':ss,'q':ss/(h*(h-1))})
    a,b = parts
    variance = a['q']+b['q']
    if variance <= 0:
        raise ValueError('Pozitif winsorize varyans gerekir')
    se = np.sqrt(variance)
    df = variance**2/(a['q']**2/(a['h']-1)+b['q']**2/(b['h']-1))
    estimate = a['trimmed_mean']-b['trimmed_mean']
    t = estimate/se
    p = 2*stats.t.sf(abs(t),df)
    ci = estimate+np.array([-1,1])*stats.t.ppf(.975,df)*se
    tested = stats.ttest_ind(first,second,equal_var=False,trim=trim)
    np.testing.assert_allclose([t,p,df],[tested.statistic,tested.pvalue,tested.df])
    np.testing.assert_allclose(ci,tested.confidence_interval())
    return {'trim_each_tail':trim,'groups':parts,'estimate':estimate,'se':float(se),'df':float(df),
            't':float(t),'p':float(p),'CI95':ci.tolist()}


def simulations():
    rng = np.random.default_rng(SEED)
    rows = []
    for sigma1,sigma2 in [(3.,1.),(1.,3.),(1.,1.)]:
        n1,n2 = 10,30
        # Bağımsız normal ortalamalar ve bağımsız ki-kare örneklem varyansları.
        difference = rng.normal(0,sigma1/np.sqrt(n1),REPETITIONS)-rng.normal(0,sigma2/np.sqrt(n2),REPETITIONS)
        v1 = sigma1**2*rng.chisquare(n1-1,REPETITIONS)/(n1-1)
        v2 = sigma2**2*rng.chisquare(n2-1,REPETITIONS)/(n2-1)
        q1,q2 = v1/n1,v2/n2
        se_w = np.sqrt(q1+q2)
        df_w = (q1+q2)**2/(q1**2/(n1-1)+q2**2/(n2-1))
        pooled = ((n1-1)*v1+(n2-1)*v2)/(n1+n2-2)
        se_p = np.sqrt(pooled*(1/n1+1/n2))
        p_w = 2*stats.t.sf(abs(difference/se_w),df_w)
        p_p = 2*stats.t.sf(abs(difference/se_p),n1+n2-2)
        true_variance = sigma1**2/n1+sigma2**2/n2
        expected_pooled = ((n1-1)*sigma1**2+(n2-1)*sigma2**2)/(n1+n2-2)*(1/n1+1/n2)
        row = {'n1':n1,'n2':n2,'sigma1':sigma1,'sigma2':sigma2,'true_mean_difference':0.,
               'nominal_alpha':.05,'true_variance_difference':true_variance,
               'expected_pooled_SE_squared':expected_pooled,'variance_ratio':expected_pooled/true_variance}
        for name,p in [('Welch',p_w),('Student',p_p)]:
            rate = float(np.mean(p<.05))
            row[name+'_rejection_rate'] = rate
            row[name+'_MC_SE'] = float(np.sqrt(rate*(1-rate)/REPETITIONS))
        # Eş varyanslı normal durumda pooled Student tam null kalibrasyonuna sahiptir.
        if sigma1==sigma2:
            assert abs(row['Student_rejection_rate']-.05)<5*np.sqrt(.05*.95/REPETITIONS)
        rows.append(row)
    return rows


def main():
    directory = Path(__file__).parent
    parent = directory.parent
    source = parent/'kaynak/ToothGrowth.csv'
    original = source.read_bytes()
    assert hashlib.sha256(original.replace(b'\r\n',b'\n').rstrip(b'\n')+b'\n').hexdigest() == '654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3'
    data = pd.read_csv(source)
    assert len(data)==60 and not data.isna().any().any()
    selected = data.loc[data.dose.eq(1)]
    first = selected.loc[selected.supp.eq('OJ'),'len'].to_numpy()
    second = selected.loc[selected.supp.eq('VC'),'len'].to_numpy()
    assert len(first)==len(second)==10
    spec = importlib.util.spec_from_file_location('b06_original',parent/'analiz.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    welch = module.independent(first,second)
    robust = yuen(first,second)
    rows = simulations()
    result = {'scope':'Kalibrasyon yalnız normal bağımsız model kurgusu; Yuen farklı konum hedefidir',
              'source_normalized_sha256':'654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3',
              'ToothGrowth_dose1':{'direction':'OJ-VC','ordinary_mean_Welch':welch,'trimmed_mean_Yuen':robust},
              'synthetic_calibration':rows,'seed':SEED,'repetitions':REPETITIONS,
              'simulation_unit':'Normal ortalamalar ve ki-kare varyanslar; ham kişi/hayvan tablosu üretilmez',
              'versions':{'numpy':np.__version__,'pandas':pd.__version__}}
    output = directory/'sonuclar'
    output.mkdir(exist_ok=True)
    pd.DataFrame(rows).to_csv(output/'kalibrasyon.csv',index=False)
    (output/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    assert source.read_bytes()==original
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
