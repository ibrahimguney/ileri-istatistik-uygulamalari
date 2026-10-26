"""SPSS yürütme yerine geçmeyen, dışa aktarılmış tablo sözleşmesi."""
from pathlib import Path
import argparse,csv,json,math
import numpy as np
import pandas as pd
from scipy import stats

FIELDS=['model','n1','n2','df','difference','se','t','p','ci_low','ci_high']


def expected(parent):
    sleep=pd.read_csv(parent/'uyku_esli.csv');d=sleep.kosul2-sleep.kosul1;n=len(d)
    mean=d.mean();se=d.std(ddof=1)/np.sqrt(n);test=stats.ttest_1samp(d,0);ci=test.confidence_interval()
    rows=[dict(model='paired_2_minus_1',n1=n,n2=0,df=n-1,difference=mean,se=se,t=test.statistic,p=test.pvalue,ci_low=ci.low,ci_high=ci.high)]
    teeth=pd.read_csv(parent/'dis_veri.csv');teeth=teeth[teeth.dose==1]
    a=teeth[teeth.supp==1].len.to_numpy();b=teeth[teeth.supp==2].len.to_numpy();test=stats.ttest_ind(a,b,equal_var=False);ci=test.confidence_interval()
    rows.append(dict(model='welch_OJ_minus_VC_dose1',n1=len(a),n2=len(b),df=test.df,difference=a.mean()-b.mean(),
        se=np.sqrt(a.var(ddof=1)/len(a)+b.var(ddof=1)/len(b)),t=test.statistic,p=test.pvalue,ci_low=ci.low,ci_high=ci.high))
    return rows


def compare(reference,observed,tolerance=.00051):
    keys=[r['model'] for r in observed]
    if len(keys)!=len(set(keys)) or set(keys)!={r['model'] for r in reference}:raise ValueError('Model satırları eksik, fazla veya yinelenmiş.')
    failures=[];index={r['model']:r for r in observed}
    for ref in reference:
        row=index[ref['model']]
        if set(row)!=set(FIELDS):raise ValueError('Sütun sözleşmesi uyuşmuyor.')
        for key in FIELDS[1:]:
            text=str(row[key]).strip()
            if key=='p' and text.startswith('<'):
                bound=float(text[1:])
                if not 0<bound<=1 or not ref[key]<bound:failures.append(ref['model']+': p üst sınırı yanlış')
                continue
            value=float(text)
            if not math.isfinite(value):raise ValueError('Sonlu sayısal çıktı gerekir.')
            if key=='p' and value==0:failures.append(ref['model']+': p=0 yazılamaz; üst sınır veya daha fazla basamak kullanın')
            tol=0 if key in ['n1','n2'] else tolerance
            if abs(value-ref[key])>tol:failures.append(ref['model']+': '+key+' uyuşmuyor')
    return failures


def main(observed=None):
    directory=Path(__file__).resolve().parent;rows=expected(directory.parent)
    out=directory/'sonuclar';out.mkdir(exist_ok=True)
    with (out/'beklenen-kontrol.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)
    status=dict(reference_generated_with='Python/SciPy',SPSS_executed=False,observed_output_supplied=observed is not None,
        rounding_absolute_tolerance=.00051,conditions='Two exact model rows, directions and sample sizes. Decimal-point comma-delimited CSV. Matching numbers do not prove software execution, assumptions, data provenance or independent review.')
    if observed:
        with Path(observed).open(newline='') as f:actual=list(csv.DictReader(f))
        status['differences']=compare(rows,actual)
        print(json.dumps(status,ensure_ascii=False,indent=2))
        if status['differences']:raise SystemExit(1)
        return
    (out/'ozet.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(status,ensure_ascii=False,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--observed');a=p.parse_args();main(a.observed)
