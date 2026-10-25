"""Ortak kayıtlarda alfa farkı ve bilinen kovaryansla öğretim örnekleri.

IPIP verisine faktör modeli uydurulmaz; model örnekleri anakütle cebiridir.
"""
from pathlib import Path
import hashlib
import json
import numpy as np
import pandas as pd


def alpha_cov(S):
    S=np.asarray(S,dtype=float)
    if S.ndim!=2 or S.shape[0]!=S.shape[1] or len(S)<2 or not np.isfinite(S).all():
        raise ValueError('Sonlu kare kovaryans matrisi gerekir.')
    if not np.allclose(S,S.T) or np.linalg.eigvalsh(S).min() < -1e-10 or S.sum()<=0:
        raise ValueError('Geçerli pozitif toplam varyanslı kovaryans gerekir.')
    k=len(S)
    return float(k/(k-1)*(1-np.trace(S)/S.sum()))


def batch_alpha(x):
    x=np.asarray(x,dtype=float)
    if x.ndim!=3 or x.shape[1]<2 or x.shape[2]<2 or not np.isfinite(x).all():
        raise ValueError('Tekrar, kişi, madde boyutlarında tam veri gerekir.')
    total=x.sum(axis=2).var(axis=1,ddof=1)
    if np.any(total<=0):
        raise ValueError('Sıfır toplam varyanslı örnek sessizce atlanmaz.')
    return x.shape[2]/(x.shape[2]-1)*(1-x.var(axis=1,ddof=1).sum(axis=1)/total)


def paired_draws(A,C,seed=202617,repeats=20000):
    A,C=np.asarray(A,float),np.asarray(C,float)
    if A.ndim!=2 or C.ndim!=2 or len(A)!=len(C) or len(A)<2 or repeats<1:
        raise ValueError('Eşleşmiş en az iki kişi ve pozitif tekrar sayısı gerekir.')
    rng=np.random.default_rng(seed);draws=[]
    for start in range(0,repeats,500):
        idx=rng.integers(0,len(A),size=(min(500,repeats-start),len(A)))
        draws.extend((batch_alpha(C[idx])-batch_alpha(A[idx])).tolist())
    return np.array(draws)


def score_model(loadings,errors,weights=None):
    lam=np.asarray(loadings,float);theta=np.asarray(errors,float)
    if lam.ndim!=1 or len(lam)<2 or theta.shape!=(len(lam),len(lam)) or not np.isfinite(lam).all():
        raise ValueError('Yük ve artık kovaryans boyutları uyumlu olmalı.')
    if not np.isfinite(theta).all() or not np.allclose(theta,theta.T) or np.linalg.eigvalsh(theta).min()<=0:
        raise ValueError('Pozitif tanımlı artık kovaryansı gerekir.')
    w=np.ones(len(lam)) if weights is None else np.asarray(weights,float)
    if w.shape!=lam.shape or not np.isfinite(w).all() or not np.any(w):
        raise ValueError('Sonlu, sıfır olmayan puan ağırlıkları gerekir.')
    S=np.outer(lam,lam)+theta
    signal=float((w@lam)**2);error=float(w@theta@w);total=signal+error
    reliability=signal/total
    return dict(alpha=alpha_cov(S),score_reliability=reliability,total_variance=total,
                error_variance=error,sem=float(np.sqrt(error)),
                illustrative_independent_change_threshold=float(1.959963984540054*np.sqrt(2*error)))


def examples():
    equal=np.full(5,.7);unequal=np.array([.8,.7,.6,.5,.4]);theta=np.diag(1-unequal**2)
    correlated=theta.copy();correlated[0,1]=correlated[1,0]=.2
    return {'tau_equivalent':score_model(equal,np.diag(1-equal**2)),
            'congeneric':score_model(unequal,theta),
            'correlated_errors':score_model(unequal,correlated)}


def main():
    directory=Path(__file__).resolve().parent
    path=directory.parent/'kaynak/bfi-ilk100-AC.csv';raw=path.read_bytes()
    assert hashlib.sha256(raw.rstrip(b'\n')+b'\n').hexdigest()=='8726fd25dbfc685be2d3d726e5511bbb31ba9c7b367b6864eb06e0d8669e6557'
    source=pd.read_csv(path);names=[f'{s}{j}' for s in ['A','C'] for j in range(1,6)]
    common=source.dropna(subset=names).sort_values('kaynak_satir').copy()
    assert len(common)==97 and common.kaynak_kayit.is_unique
    for name in ['A1','C4','C5']:common[name]=7-common[name]
    A=common[[f'A{j}' for j in range(1,6)]].to_numpy();C=common[[f'C{j}' for j in range(1,6)]].to_numpy()
    a,c=[alpha_cov(np.cov(x,rowvar=False,ddof=1)) for x in [A,C]]
    draws=paired_draws(A,C)
    result=dict(common_records=dict(n=97,alpha_A=a,alpha_C=c,difference_C_minus_A=c-a,
        seed=202617,resamples=20000,method='paired participant-row percentile, linear quantiles',
        ci95=np.quantile(draws,[.025,.975],method='linear').tolist(),bootstrap_sd=float(draws.std(ddof=1)),invalid_draws=0),
        population_examples=examples(),
        limits='First 100 source records, complete common cases; paired bootstrap preserves A-C dependence. Difference of observed alpha functionals, not proof of better construct validity or population reliability. Model examples are stipulated covariance calculations, not fitted IPIP omega; no clinical or longitudinal threshold validation.')
    out=directory/'sonuclar';out.mkdir(exist_ok=True)
    common[['kaynak_satir','kaynak_kayit']].to_csv(out/'ortak-kayitlar.csv',index=False)
    (out/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
