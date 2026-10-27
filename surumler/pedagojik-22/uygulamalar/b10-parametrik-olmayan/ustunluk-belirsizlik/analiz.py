"""Bağımsız iki örneklemde A belirsizliği; eşli farkta işaret/medyan ayrımı."""
from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
import scipy
from scipy import stats
SEED=20261025
B=20000

def vector(x):
    x=np.asarray(x,float)
    if x.ndim!=1 or len(x)<2 or not np.isfinite(x).all():
        raise ValueError("En az iki sonlu gözlem gerekir")
    return np.sort(x)

def kernel(x,y):
    return (x[..., :,None]>y[...,None,:]).astype(float)+.5*(x[..., :,None]==y[...,None,:])

def superiority(x,y):
    x,y=vector(x),vector(y);h=kernel(x,y)
    return float(h.mean())

def brunner_munzel(x,y):
    x,y=vector(x),vector(y);h=kernel(x,y);a=float(h.mean())
    v1=h.mean(1).var(ddof=1)/len(x);v2=h.mean(0).var(ddof=1)/len(y);v=v1+v2
    if v<=0:raise ValueError("Sıfır yerleşim varyansı: BM yaklaşımı tanımsız")
    se=float(np.sqrt(v));df=float(v*v/(v1*v1/(len(x)-1)+v2*v2/(len(y)-1)))
    t=float((a-.5)/se);p=float(2*stats.t.sf(abs(t),df))
    reference=stats.brunnermunzel(x,y,distribution='t',alternative='two-sided')
    np.testing.assert_allclose([-t,p],[reference.statistic,reference.pvalue],rtol=1e-11,atol=1e-13)
    return dict(A=a,SE=se,t_positive_for_x_superiority=t,df=df,p_two_sided=p,method='Brunner-Munzel t approximation; not exhaustive')

def bootstrap(x,y,repetitions=B,seed=SEED):
    x,y=vector(x),vector(y)
    if repetitions<100:raise ValueError("En az100 tekrar")
    rng=np.random.default_rng(seed)
    xb=x[rng.integers(0,len(x),size=(repetitions,len(x)))];yb=y[rng.integers(0,len(y),size=(repetitions,len(y)))]
    estimates=kernel(xb,yb).mean(axis=(1,2))
    return dict(A=float(kernel(x,y).mean()),interval_percentile_95=np.quantile(estimates,[.025,.975],method='linear').tolist(),
        repetitions=repetitions,seed=seed,quantile_method='linear',n_at_zero=int(np.sum(estimates==0)),n_at_one=int(np.sum(estimates==1)),
        unit='Independent animal rows within each group; not n*m independent pairs',exact_coverage=False)

def sign_and_median(d,alpha=.05):
    d=vector(d);n=len(d);nonzero=d[d!=0];m=len(nonzero)
    if m==0:raise ValueError("İşaret testi için sıfır olmayan fark gerekir")
    positive=int(np.sum(nonzero>0));tested=stats.binomtest(positive,m,.5,alternative='two-sided')
    # [D_(k),D_(n-k+1)] için sürekli medyanda 1-2*BinomCDF(k-1;n,.5).
    candidates=[(k,float(1-2*stats.binom.cdf(k-1,n,.5))) for k in range(1,n//2+1)]
    acceptable=[(k,c) for k,c in candidates if c>=1-alpha]
    if not acceptable:raise ValueError("Bu n ile istenen düzeyde sonlu sıra aralığı yok")
    k,coverage=max(acceptable)
    return dict(n_pairs=n,n_zero=int(n-m),n_signs=m,n_positive=positive,sign_p=float(tested.pvalue),
        sign_target='P(D>0 | D!=0)=.5; zero differences omitted only in this conditional test',
        median=float(np.median(d)),median_interval=[float(d[k-1]),float(d[n-k])],order_k=k,
        continuous_model_coverage=coverage,requested_coverage=1-alpha,
        median_interval_target='Population median of paired difference D; all pairs including zeros; iid continuous model for stated exact coverage')

def main():
    here=Path(__file__).parent;shared=here.parent.parent/'b06-parametrik-testler/kaynak'
    expected={'sleep.csv':'adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e','ToothGrowth.csv':'654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3'}
    for name,digest in expected.items():assert hashlib.sha256((shared/name).read_bytes().rstrip(b"\n")+b"\n").hexdigest()==digest
    teeth=pd.read_csv(shared/'ToothGrowth.csv');sleep=pd.read_csv(shared/'sleep.csv')
    x=teeth.loc[(teeth.supp=='OJ')&(teeth.dose==1),'len'].to_numpy();y=teeth.loc[(teeth.supp=='VC')&(teeth.dose==1),'len'].to_numpy()
    assert len(x)==len(y)==10
    paired=sleep.pivot(index='ID',columns='group',values='extra').sort_index();assert paired.shape==(10,2) and not paired.isna().any().any()
    d=np.round((paired[2]-paired[1]).to_numpy(),1)
    result=dict(source_hashes=expected,n_OJ=len(x),n_VC=len(y),brunner_munzel=brunner_munzel(x,y),bootstrap=bootstrap(x,y),sign_median=sign_and_median(d),
        weak_null='A=P(X>Y)+.5P(X=Y)=.5; unlike equality of entire distributions',
        limits='Small n=10/group; approximate BM and percentile bootstrap, no calibrated coverage claim; no animal independence of all100 comparisons',
        median_continuity_limit='Rounded data contain ties and a zero: continuous-model coverage is a benchmark, not measured coverage of these data',
        versions=dict(numpy=np.__version__,pandas=pd.__version__,scipy=scipy.__version__))
    out=here/'sonuclar';out.mkdir(exist_ok=True);(out/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    pd.DataFrame([dict(target='A_OJ_VC',estimate=result['bootstrap']['A'],lower=result['bootstrap']['interval_percentile_95'][0],upper=result['bootstrap']['interval_percentile_95'][1],method='Within-group animal bootstrap percentile approximate'),dict(target='median_D_drug2_minus_drug1',estimate=result['sign_median']['median'],lower=result['sign_median']['median_interval'][0],upper=result['sign_median']['median_interval'][1],method='Order statistics; continuous-model benchmark')]).to_csv(out/'araliklar.csv',index=False)
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
