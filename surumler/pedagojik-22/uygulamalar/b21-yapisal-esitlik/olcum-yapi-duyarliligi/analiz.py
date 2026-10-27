"""MIMIC ölçüm duyarlılığı ve aynı kovaryansı veren artık-rho senaryoları.

Ana analiz/bootstrap korunur. Yeni senaryolar keşifsel nokta duyarlılığıdır.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import numpy as np
import pandas as pd


def residual_sensitivity(u,v,w,a,total,rho):
    if not np.isfinite([u,v,w,a,total,rho]).all() or u<=0 or v-w*w/u<=0 or abs(rho)>=1:
        raise ValueError('Pozitif koşullu kovaryans ve |rho|<1 gerekir.')
    psi=(v-w*w/u)/(1-rho*rho)
    b=w/u-rho*np.sqrt(psi/u)
    return dict(b=float(b),c_prime=float(total-a*b),psi_C=float(psi),
                residual_covariance=float(rho*np.sqrt(u*psi)),indirect=float(a*b),total=float(total))


def encode(model,rows):
    values={r['parameter']:r['value'] for r in rows}
    return np.array([np.log(values[label]) if transform=='log' else values[label]
                     for label,_,_,_,transform in model.parameters])


def main():
    directory=Path(__file__).resolve().parent;parent=directory.parent
    specmod=importlib.util.spec_from_file_location('sem_reference',parent/'analiz.py')
    module=importlib.util.module_from_spec(specmod);specmod.loader.exec_module(module)
    path=parent.parent/'b18-faktor-analizi/yarim_B.csv';raw=path.read_bytes()
    assert hashlib.sha256(raw.rstrip(b'\n')+b'\n').hexdigest()==module.SOURCE_HASH
    source=pd.read_csv(path);assert len(source)==1316 and source.kaynak_kayit.is_unique
    x=source[module.ITEMS].astype(float).copy()
    for name in ['A1','C4','C5']:x[name]=7-x[name]
    z=(x-x.mean())/x.std(ddof=1);K=(source.gender==2).astype(float)
    np.testing.assert_array_equal(K.value_counts().sort_index(),[425,891])
    sample=np.cov(np.column_stack([z,K]),rowvar=False,ddof=1)
    old=json.loads((parent/'sonuclar/ozet.json').read_text());ref=old['models']['mediation']
    base=module.build_models()['mediation'];t=encode(base,ref['parameters'])
    np.testing.assert_allclose(base.covariance(t),pd.read_csv(parent/'sonuclar/mediation_kovaryans.csv',index_col=0),atol=1e-12)
    np.testing.assert_allclose((len(x)-1)*module.objective(t,sample,base)[0],ref['chi2'],atol=1e-7)
    scenarios={}
    selected=['a_stdnox','b_std','c_prime_stdnox','indirect_stdnox','total_stdnox']
    scenarios['baseline']=dict(direct_indicator_paths=[],chi2=ref['chi2'],df=ref['df'],
        points={key:ref['quantities'][key]['estimate'] for key in selected})
    for items,label in [(('A1',),'direct_A1'),(('A1','A2'),'direct_A1_A2')]:
        parameters=base.parameters+[(name+'~K','A',name,'K','lin') for name in items]
        model=module.Model('mediation',base.observed,parameters,list(base.fixed))
        info,values,Sigma,_=module.fit(model,sample,len(x),start=np.r_[t,np.zeros(len(items))])
        rows={r['parameter']:r['value'] for r in info['parameters']}
        scenarios[label]=dict(direct_indicator_paths=list(items),chi2=info['chi2'],df=info['df'],
            jacobian_rank=info['jacobian_rank'],points={key:info['quantities'][key]['estimate'] for key in selected},
            direct_coefficients={item:rows[item+'~K'] for item in items})
        # İkili K için modelin ima ettiği grup farkı, Cov(z,K)/Var(K)'dır.
        paths,_,inverse,_=model.matrices(values)
        slopes=Sigma[:-1,-1]/Sigma[-1,-1]
        np.testing.assert_allclose(slopes,inverse[:10,model.index['K']],atol=1e-10)
    _,S,_,full=base.matrices(t);idx=base.index
    positions=[idx[k] for k in ['A','C','K']];latent=full[np.ix_(positions,positions)]
    varK=latent[2,2];conditional=latent[:2,:2]-np.outer(latent[:2,2],latent[2,:2])/varK
    u,v,w=conditional[0,0],conditional[1,1],conditional[0,1]
    a,total=latent[0,2]/varK,latent[1,2]/varK;sdC=np.sqrt(latent[1,1])
    rho_zero=float(w/np.sqrt(u*v));rho_rows=[]
    for rho in [-.3,0.,.3,rho_zero,.6]:
        point=residual_sensitivity(u,v,w,a,total,rho)
        changed=t.copy()
        for name,value in [('C~A',point['b']),('C~K',point['c_prime']),('C~~C',np.log(point['psi_C']))]:
            changed[base.labels().index(name)]=value
        fixed=list(base.fixed)+[('S','A','C',point['residual_covariance'])]
        working=module.Model('mediation',base.observed,list(base.parameters),fixed)
        Sigma=working.covariance(changed)
        np.testing.assert_allclose(Sigma,base.covariance(t),atol=1e-10)
        disturbance=working.matrices(changed)[1]
        assert np.linalg.eigvalsh(disturbance).min()>0
        fit_chi=(len(x)-1)*module.objective(changed,sample,working)[0]
        np.testing.assert_allclose(fit_chi,ref['chi2'],atol=1e-7)
        rho_rows.append(dict(rho=float(rho),**point,indirect_stdnox=float(point['indirect']/sdC),
            c_prime_stdnox=float(point['c_prime']/sdC),total_stdnox=float(total/sdC),chi2=float(fit_chi)))
    result=dict(n=1316,measurement_scenarios=scenarios,
        structural_sensitivity=dict(conditional_covariance=conditional.tolist(),rho_zero_point=rho_zero,rows=rho_rows),
        limits='Same inspected B half; MIMIC direct K-to-indicator paths are exploratory uniform-DIF sensitivity, not multi-group invariance or causal effects. Rho is assumed, not estimated; covariance/fit is identical across rho. No intervals/bootstrap for new scenarios, ordinal/robust analysis, selection adjustment or new validation. Original 2000-draw bootstrap applies only to original model.')
    out=directory/'sonuclar';out.mkdir(exist_ok=True)
    (out/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    pd.DataFrame(rho_rows).to_csv(out/'rho-senaryolari.csv',index=False)
    pd.DataFrame([dict(model=k,**v['points'],chi2=v['chi2'],df=v['df']) for k,v in scenarios.items()]).to_csv(out/'mimic-senaryolari.csv',index=False)
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
