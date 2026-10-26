"""Sabit çıpa kümelerinde gizil fark aralıkları ve ortalama ayrıştırması.

Ana veri/model araması korunur. Yeni aralıklar seçim sonrası koşulludur.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import numpy as np
import pandas as pd
from scipy.stats import norm


def moment_derivatives(values,spec,fixed,g,module):
    mats,Sigma,mu=module.matrices(values,spec,fixed,g)
    q=len(values);dS=np.zeros((q,10,10));dm=np.zeros((q,10))
    L,P,a=mats['L'],mats['Phi'],mats['alpha'].ravel()
    for group,name,i,j,k in spec.cells:
        if group!=g:continue
        if name=='L':
            unit=np.zeros_like(L);unit[i,j]=1
            dS[k]+=unit@P@L.T+L@P@unit.T;dm[k]+=unit@a
        elif name=='nu':dm[k,i]+=1
        elif name=='Theta':
            dS[k,i,j]+=1
            if i!=j:dS[k,j,i]+=1
        elif name=='Phi':
            unit=np.zeros_like(P);unit[i,j]=1
            if i!=j:unit[j,i]=1
            dS[k]+=L@unit@L.T
        else:dm[k]+=L[:,i]
    return mats,Sigma,mu,dS,dm


def expected_covariance(groups):
    information=None
    for n,Sigma,dS,dm in groups:
        if n<=1 or not np.isfinite(Sigma).all() or np.linalg.eigvalsh(Sigma).min()<=0:
            raise ValueError('Pozitif tanımlı model kovaryansı ve n>1 gerekir.')
        inverse=np.linalg.inv(Sigma);W=np.einsum('ij,kjl->kil',inverse,dS)
        block=n*(dm@inverse@dm.T+.5*np.einsum('aij,bji->ab',W,W))
        information=block if information is None else information+block
    if information is None or np.linalg.eigvalsh(information).min()<=1e-9:
        raise ValueError('Tanımlanmış, pozitif bilgi matrisi gerekir.')
    return np.linalg.inv(information)


def pooled_effect(delta,v0,v1,n0,n1):
    if min(v0,v1,n0,n1)<=0:raise ValueError('Pozitif varyans ve grup büyüklükleri gerekir.')
    return delta/np.sqrt((n0*v0+n1*v1)/(n0+n1))


def reverse_reference(mats,center,scale):
    center=np.asarray(center,float);scale=np.asarray(scale,float)
    if np.any(scale<=0):raise ValueError('Pozitif yeniden ölçekleme gerekir.')
    D=np.diag(scale);inverse=np.diag(1/scale)
    return dict(L=mats['L']@inverse,nu=mats['nu']+mats['L']@center[:,None],
                alpha=D@(mats['alpha']-center[:,None]),Phi=D@mats['Phi']@D,Theta=mats['Theta'].copy())


def mean_parts(left,right):
    if not np.allclose(left['L'],right['L']):
        raise ValueError('Bu ayrıştırma ortak yükler gerektirir.')
    intercept=(right['nu']-left['nu']).ravel()
    factor=(left['L']@(right['alpha']-left['alpha'])).ravel()
    return intercept,factor,intercept+factor


def main():
    directory=Path(__file__).resolve().parent;parent=directory.parent
    specmod=importlib.util.spec_from_file_location('invariance_reference',parent/'analiz.py')
    module=importlib.util.module_from_spec(specmod);specmod.loader.exec_module(module)
    path=parent.parent/'b18-faktor-analizi/yarim_B.csv';raw=path.read_bytes()
    assert hashlib.sha256(raw.rstrip(b'\n')+b'\n').hexdigest()==module.SOURCE_HASH
    source=pd.read_csv(path);keyed=source[module.ITEMS].copy()
    for name in ['A1','C4','C5']:keyed[name]=7-keyed[name]
    data=[]
    for group,n in [(1,425),(2,891)]:
        x=keyed.loc[source.gender==group].to_numpy(float);assert len(x)==n
        data.append((n,np.cov(x,rowvar=False,ddof=0),x.mean(axis=0)))
    old=json.loads((parent/'sonuclar/ozet.json').read_text())
    cases={'scalar':((),old['models']['scalar']),
           'free_A1':(('A1',),old['partial_scalar'])}
    start=dict(old['partial_scalar']['estimates'])
    for g in [1,2]:start[f'nu.A2.g{g}']=start['nu.A2']
    extra,_,_,_=module.fit('scalar',data,free_intercepts=('A1','A2'),start=start)
    cases['free_A1_A2']=(('A1','A2'),extra)
    out=directory/'sonuclar';out.mkdir(exist_ok=True);results={};rows=[]
    for label,(freed,ref) in cases.items():
        spec,fixed=module.build('scalar',freed)
        t=np.array([ref['estimates'][name] for name in spec.labels])
        np.testing.assert_allclose(module.objective(t,spec,fixed,data)[0],ref['chi2'],atol=1e-7)
        moments=[moment_derivatives(t,spec,fixed,g,module) for g in [0,1]]
        for mats,Sigma,mu,_,_ in moments:
            assert np.linalg.eigvalsh(mats['Phi']).min()>0 and np.linalg.eigvalsh(mats['Theta']).min()>0
        vcov=expected_covariance([(data[g][0],m[1],m[3],m[4]) for g,m in enumerate(moments)])
        gradmax=float(np.max(np.abs(module.objective(t,spec,fixed,data)[1])))
        assert gradmax<1e-3
        print(f'{label}: max|gradient|={gradmax:.8g}; required <1e-3')
        estimates=[];G=[]
        for factor in ['A','C']:
            ia=spec.labels.index(f'alpha.{factor}.g2');iv=spec.labels.index(f'phi.{factor}{factor}.g2')
            delta,var=t[ia],t[iv];weight=891/1316;W=(425+891*var)/1316
            a=np.zeros(len(t));a[ia]=1
            d=np.zeros(len(t));d[ia]=1/np.sqrt(W);d[iv]=-.5*delta*weight/W**1.5
            estimates.extend([delta,pooled_effect(delta,1,var,425,891)]);G.extend([a,d])
        G=np.array(G);metric_covariance=G@vcov@G.T;SE=np.sqrt(np.diag(metric_covariance));ci={}
        for i,name in enumerate(['A_male_SD','A_pooled_SD','C_male_SD','C_pooled_SD']):
            ci[name]=dict(estimate=float(estimates[i]),se=float(SE[i]),
                conditional_ci95=(estimates[i]+np.array([-1,1])*norm.ppf(.975)*SE[i]).tolist())
            if i in [0,2]:ci[name]['bonferroni_A_C_ci95']=(estimates[i]+np.array([-1,1])*norm.ppf(1-.05/4)*SE[i]).tolist()
        left,right=moments[0][0],moments[1][0]
        intercept,factor,total=mean_parts(left,right)
        np.testing.assert_allclose(total,moments[1][2]-moments[0][2],atol=1e-12)
        decomposition={}
        for name,indices in [('A',slice(0,5)),('C',slice(5,10))]:
            observed=float((data[1][2]-data[0][2])[indices].mean())
            decomposition[name]=dict(intercept_component=float(intercept[indices].mean()),
                latent_component=float(factor[indices].mean()),model_mean_gap=float(total[indices].mean()),
                observed_mean_gap=observed,observed_minus_model=float(observed-total[indices].mean()))
        center=right['alpha'].ravel();scale=1/np.sqrt(np.diag(right['Phi']))
        transformed=[reverse_reference(m,center,scale) for m in [left,right]]
        for g,m in enumerate(transformed):
            np.testing.assert_allclose(m['L']@m['Phi']@m['L'].T+m['Theta'],moments[g][1],atol=1e-10)
            np.testing.assert_allclose((m['nu']+m['L']@m['alpha']).ravel(),moments[g][2],atol=1e-10)
        results[label]=dict(free_intercepts=list(freed),chi2=float(ref['chi2']),df=int(ref['df']),
            gradient_check_passed=True,gradient_limit=1e-3,intervals=ci,mean_decomposition=decomposition,
            male_minus_female_in_female_SD=transformed[0]['alpha'].ravel().tolist(),
            variance_g2=np.diag(right['Phi']).tolist(),full_metric_covariance=metric_covariance.tolist())
        rows.extend([dict(model=label,quantity=name,**val) for name,val in ci.items()])
    result=dict(n=[425,891],method='Fixed anchor sets; expected normal-theory information with mean and covariance derivatives; delta method; intervals conditional on model selection',
        models=results,limits='Same previously inspected B half; A1 was selected by a data-based search. Nominal search p-values and conditional intervals do not account for selection; A1+A2 is sensitivity, not a new accepted model or equivalence proof. No ordinal/robust inference, new validation, or causal group effect.')
    (out/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    pd.DataFrame(rows).to_csv(out/'gizil-fark-araliklari.csv',index=False)
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
