"""İki grup: hedef, affine değişmezlik ve eşzamanlı aralık öğretimi."""
from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
import scipy
from scipy import stats
SOURCE_HASH="1eebcf05961dd2f569b545e5456c0fd2e5c8b5a79cd82770f3b0a06c31230fce"

def compare_groups(a,b,alpha=.05):
    a,b=np.asarray(a,float),np.asarray(b,float)
    if a.ndim!=2 or b.ndim!=2 or a.shape[1]!=b.shape[1]:
        raise ValueError("Aynı p sütunlu iki matris gerekir")
    n1,p=a.shape;n2=len(b);df=n1+n2-2
    if min(n1,n2)<2 or p<1 or df<p or not 0<alpha<1:
        raise ValueError("Örneklem/boyut/alpha uygun değil")
    if not np.isfinite(a).all() or not np.isfinite(b).all():
        raise ValueError("Tam ve sonlu gözlemler gerekir")
    s1=np.atleast_2d(np.cov(a,rowvar=False,ddof=1));s2=np.atleast_2d(np.cov(b,rowvar=False,ddof=1))
    sp=((n1-1)*s1+(n2-1)*s2)/df
    v=s1/n1+s2/n2
    for covariance in [sp,v]:
        if np.linalg.matrix_rank(covariance)<p:
            raise ValueError("Tekil kovaryans: boyutu/ölçümü inceleyin")
        np.linalg.cholesky(covariance)
    d=a.mean(0)-b.mean(0);vp=sp*(1/n1+1/n2)
    t2=float(d@np.linalg.solve(vp,d));df2=n1+n2-p-1
    f=t2*df2/(p*df)
    w=float(d@np.linalg.solve(v,d))
    se=np.sqrt(np.diag(vp));tcrit=stats.t.ppf(1-alpha/2,df)
    bonf=stats.t.ppf(1-alpha/(2*p),df)
    # Hotelling elipsoidinin her doğrultudaki izdüşümü aynı kritik çarpanı kullanır.
    hot=np.sqrt(p*df/df2*stats.f.ppf(1-alpha,p,df2))
    intervals=[]
    for j in range(p):
        intervals.append(dict(position=j,difference=float(d[j]),pooled_SE=float(se[j]),
            marginal=[float(d[j]-tcrit*se[j]),float(d[j]+tcrit*se[j])],
            bonferroni_family=[float(d[j]-bonf*se[j]),float(d[j]+bonf*se[j])],
            hotelling_all_directions=[float(d[j]-hot*se[j]),float(d[j]+hot*se[j])]))
    return dict(n1=n1,n2=n2,p=p,alpha=alpha,difference=d.tolist(),
        pooled_T2=t2,pooled_F=float(f),pooled_df=[p,df2],pooled_p=float(stats.f.sf(f,p,df2)),
        unpooled_Wald_chi2=w,unpooled_asymptotic_p=float(stats.chi2.sf(w,p)),
        intervals=intervals)

def main():
    here=Path(__file__).parent;path=here.parent/'kaynak/sat_act.csv'
    assert hashlib.sha256(path.read_bytes().rstrip(b"\n")+b"\n").hexdigest()==SOURCE_HASH
    raw=pd.read_csv(path);data=raw.dropna(subset=['ACT','SATV','SATQ'])
    assert len(raw)==700 and len(data)==687
    a=data.loc[data.gender==1,['SATV','SATQ']].to_numpy(float)
    b=data.loc[data.gender==2,['SATV','SATQ']].to_numpy(float)
    original=compare_groups(a,b)
    # Ortak, tersinir dönüşüm: SATV/100 ve (SATQ-SATV)/100; aynı vektör hipotezi.
    transform=np.array([[.01,0],[-.01,.01]]);shift=np.array([2.,-3.])
    transformed=compare_groups(a@transform.T+shift,b@transform.T+shift)
    for k in ['pooled_T2','pooled_F','pooled_p','unpooled_Wald_chi2','unpooled_asymptotic_p']:
        np.testing.assert_allclose(original[k],transformed[k],rtol=1e-10,atol=1e-12)
    reference=json.loads((here.parent/'sonuclar/ozet.json').read_text())['two_group_gender']
    np.testing.assert_allclose(original['pooled_T2'],reference['T2'],rtol=1e-12)
    rows=[]
    for name,row in zip(['SATV','SATQ'],original['intervals']):
        rows.append(dict(outcome=name,**row))
    output=here/'sonuclar';output.mkdir(exist_ok=True)
    pd.DataFrame([{k:v for k,v in row.items() if not isinstance(v,list)} | {
        f'{k}_{side}':row[k][i] for k in ['marginal','bonferroni_family','hotelling_all_directions'] for i,side in enumerate(['lower','upper'])} for row in rows]).to_csv(output/'araliklar.csv',index=False)
    result=dict(source_sha256=SOURCE_HASH,complete_case_policy='All three original outcomes: 687; SATV/SATQ analysis uses same people',
        original=original,affine_transformed=transformed,transformation=transform.tolist(),shift=shift.tolist(),
        asymptotic_Wald_small_sample_calibration=False,permutation_performed=False,
        interval_assumptions='Independent multivariate normal observations; common positive-definite covariance for pooled intervals',
        interpretation='Observational self-report sample; no causal or national population claim',
        versions=dict(numpy=np.__version__,pandas=pd.__version__,scipy=scipy.__version__))
    (output/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(original,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
