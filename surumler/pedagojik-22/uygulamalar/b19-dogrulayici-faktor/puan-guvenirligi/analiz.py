"""Sabit M1/M2 yapılarında puan hedefi ve normal kuramlı delta belirsizliği.

Ana model yeniden seçilmez; beklenen bilgi ve tam parametre kovaryansı kullanılır.
"""
from pathlib import Path
import importlib.util
import hashlib
import json
import numpy as np
import pandas as pd
from scipy.stats import norm


def score_share(loadings, errors, weights=None, factor_variance=1.):
    lam=np.asarray(loadings,float);theta=np.asarray(errors,float)
    w=np.ones(len(lam)) if weights is None else np.asarray(weights,float)
    if lam.ndim!=1 or theta.shape!=(len(lam),len(lam)) or w.shape!=lam.shape:
        raise ValueError('Uyumlu yük, hata matrisi ve puan ağırlıkları gerekir.')
    if not all(np.isfinite(a).all() for a in [lam,theta,w]) or not np.isfinite(factor_variance) or factor_variance<=0:
        raise ValueError('Sonlu katsayılar ve pozitif faktör varyansı gerekir.')
    if not np.allclose(theta,theta.T) or np.linalg.eigvalsh(theta).min()<=0 or not np.any(w):
        raise ValueError('Pozitif tanımlı artık matrisi ve sıfır olmayan ağırlık gerekir.')
    signal=float((w@lam)**2*factor_variance);error=float(w@theta@w)
    return signal/(signal+error)


def expected_covariance(covariance,derivatives,n):
    if n<=1:raise ValueError('n>1 gerekir.')
    inverse=np.linalg.inv(covariance)
    weighted=np.einsum('ij,kjl->kil',inverse,derivatives)
    information=(n-1)/2*np.einsum('aij,bji->ab',weighted,weighted)
    if np.linalg.eigvalsh(information).min()<=0:
        raise ValueError('Bilgi matrisi pozitif tanımlı değil.')
    return np.linalg.inv(information)


def quantities(parameters,model,raw_sd):
    """Karmaşık adım türevini de koruyan model fonksiyonu; çıktı sırası LABELS."""
    t=np.asarray(parameters);lam=t[:10];theta=np.diag(np.exp(t[10:20]))
    if model=='resid_cov':
        for value,(i,j) in zip(t[21:],[(0,1),(5,6),(8,9)]):theta[i,j]=theta[j,i]=value
    sd=np.sqrt(lam**2+np.diag(theta));phi=np.tanh(t[20])
    output=[];aves=[]
    for positions in [np.arange(5),np.arange(5,10)]:
        l=lam[positions];E=theta[np.ix_(positions,positions)]
        for w in [np.asarray(raw_sd)[positions],1/sd[positions]]:
            signal=(w@l)**2
            output.append(signal/(signal+w@E@w))
        ave=np.mean((l/sd[positions])**2);output.append(ave);aves.append(ave)
    output.extend([a-phi**2 for a in aves])
    return np.asarray(output)


LABELS=['CR_raw_A','CR_standardized_A','AVE_A','CR_raw_C','CR_standardized_C','AVE_C','AVE_A_minus_phi2','AVE_C_minus_phi2']


def complex_jacobian(function,point):
    columns=[]
    for j in range(len(point)):
        p=np.asarray(point,complex).copy();p[j]+=1e-20j
        columns.append(np.imag(function(p))/1e-20)
    return np.stack(columns,axis=-1)


def main():
    directory=Path(__file__).resolve().parent;parent=directory.parent
    spec=importlib.util.spec_from_file_location('cfa_reference',parent/'analiz.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    data=pd.read_csv(parent/'puanlanmis.csv')
    names=module.NAMES;assert len(data)==1316 and data.kaynak_kayit.is_unique
    values=data[names].to_numpy(float);raw_sd=values.std(axis=0,ddof=1)
    source_path=parent.parent/'b18-faktor-analizi/yarim_B.csv'
    source_bytes=source_path.read_bytes()
    assert hashlib.sha256(source_bytes.rstrip(b'\n')+b'\n').hexdigest()==module.SOURCE_HASH
    source=pd.read_csv(source_path)
    np.testing.assert_array_equal(data.kaynak_kayit,source.kaynak_kayit)
    keyed=source[names].copy()
    for name in ['A1','C4','C5']:keyed[name]=7-keyed[name]
    np.testing.assert_array_equal(values,keyed.to_numpy())
    reference=json.loads((parent/'sonuclar/ozet.json').read_text())
    results={}
    for model in ['correlated','resid_cov']:
        ref=reference['models'][model]
        t=np.r_[[a['loading'] for a in ref['items']],np.log([a['theta'] for a in ref['items']]),np.arctanh(ref['phi'])]
        if model=='resid_cov':t=np.r_[t,[ref['residual_covariances'][names[i]+'~~'+names[j]]['theta'] for i,j in module.RESIDUAL_PAIRS]]
        L,_,P,Sigma=module.decode(t,model)
        np.testing.assert_allclose(Sigma,pd.read_csv(parent/'sonuclar'/f'{model}_model.csv',index_col=0),atol=1e-12)
        theta=Sigma-L@P@L.T
        assert np.linalg.eigvalsh(theta).min()>0
        vcov=expected_covariance(Sigma,module.derivatives(t,model),len(data))
        estimates=quantities(t,model,raw_sd)
        jac=complex_jacobian(lambda p:quantities(p,model,raw_sd),t)
        numeric=module.numeric_jacobian(lambda p:quantities(p,model,raw_sd),t)
        np.testing.assert_allclose(jac,numeric,atol=1e-8)
        metric_covariance=jac@vcov@jac.T
        se=np.sqrt(np.diag(metric_covariance))
        rows={}
        for j,name in enumerate(LABELS):
            rows[name]=dict(estimate=float(estimates[j]),se=float(se[j]),
                pointwise_ci95=(estimates[j]+np.array([-1,1])*norm.ppf(.975)*se[j]).tolist())
            if j>=6:
                rows[name]['bonferroni_two_contrasts_ci95']=(estimates[j]+np.array([-1,1])*norm.ppf(1-.05/4)*se[j]).tolist()
        for scale,j in [('A',0),('C',3)]:
            np.testing.assert_allclose(estimates[j+1],ref['AVE_CR'][scale]['CR_standardized_sum'],atol=1e-12)
            np.testing.assert_allclose(estimates[j+2],ref['AVE_CR'][scale]['AVE'],atol=1e-12)
        # Eski yük standart hatalarını aynı beklenen bilgiyle bağımsız yeniden kurar.
        loadfun=lambda p:p[:10]/np.sqrt(p[:10]**2+np.exp(p[10:20]))
        G=complex_jacobian(loadfun,t)
        np.testing.assert_allclose(np.sqrt(np.diag(G@vcov@G.T)),[a['loading_std_se'] for a in ref['items']],rtol=1e-6,atol=1e-9)
        results[model]=dict(quantities=rows,
            full_metric_covariance=metric_covariance.tolist(),
            diagonal_only_se_counterexample=np.sqrt(np.sum(jac**2*np.diag(vcov),axis=1)).tolist())
    result=dict(n=1316,information='Expected normal-theory information, Wishart n-1; full covariance; complex-step delta derivative',
        interval='Untransformed asymptotic Wald intervals; no clipping; pointwise except separately labeled Bonferroni family of two AVE-minus-phi-squared contrasts within each fixed model',
        models=results,limits='Same previously examined half B; no fresh validation, ordinal/robust analysis, model-selection uncertainty, or M1-M2 difference interval. Focal-factor share treats residual components as error relative to that target; not universal temporal reliability or validity proof.')
    out=directory/'sonuclar';out.mkdir(exist_ok=True)
    (out/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    pd.DataFrame([dict(model=m,quantity=q,**r) for m,a in results.items() for q,r in a['quantities'].items()]).to_csv(out/'araliklar.csv',index=False)
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
