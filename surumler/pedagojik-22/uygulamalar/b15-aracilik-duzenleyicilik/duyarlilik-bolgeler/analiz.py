"""Bilinen simülasyonda varsayım duyarlılığı ve basit eğim bölgeleri."""
from pathlib import Path
import importlib.util,json,os,tempfile
if 'MPLCONFIGDIR' not in os.environ:os.environ['MPLCONFIGDIR']=tempfile.mkdtemp(prefix='b15-mpl-')
import numpy as np
import pandas as pd
import scipy
from scipy import stats,optimize
import statsmodels
import statsmodels.formula.api as smf
BASE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('b15_original_analysis',BASE/'analiz.py')
original=importlib.util.module_from_spec(spec);spec.loader.exec_module(original)

def sensitivity(a,b,residual_ratio,rho):
    rho=np.asarray(rho,float)
    if not np.isfinite(rho).all() or np.any(np.abs(rho)>=1) or not np.isfinite([a,b,residual_ratio]).all() or residual_ratio<=0:
        raise ValueError("Sonlu parametre, pozitif artık oranı ve -1<rho<1 gerekir")
    adjusted_b=b-rho*residual_ratio/np.sqrt(1-rho*rho)
    return a*adjusted_b

def band(beta,cov,w,critical):
    beta,cov=np.asarray(beta,float),np.asarray(cov,float);w=np.asarray(w,float)
    if beta.shape!=(2,) or cov.shape!=(2,2) or not np.isfinite(w).all() or not np.isfinite(beta).all() or not np.isfinite(cov).all() or critical<=0:
        raise ValueError("İki eğim parametresi ve geçerli kovaryans gerekir")
    slope=beta[0]+beta[1]*w;variance=cov[0,0]+2*w*cov[0,1]+w*w*cov[1,1]
    if np.any(variance<0):raise ValueError("Negatif varyans")
    half=critical*np.sqrt(variance)
    return np.stack([slope-half,slope+half],axis=-1)

def roots(beta,cov,critical):
    b=np.asarray(beta,float);v=np.asarray(cov,float)
    coeff=[b[1]**2-critical**2*v[1,1],2*(b[0]*b[1]-critical**2*v[0,1]),b[0]**2-critical**2*v[0,0]]
    answer=np.roots(np.trim_zeros(np.asarray(coeff),'f'))
    return sorted(float(z.real) for z in answer if abs(z.imag)<1e-10)

def main():
    here=Path(__file__).parent;data=original.uret();saved=pd.read_csv(BASE/'veri.csv')
    assert len(data)==len(saved)==160
    np.testing.assert_allclose(data.to_numpy(float),saved[data.columns].to_numpy(float),atol=5.1e-7,rtol=0)
    ma=smf.ols('araci~x',data=data).fit();my=smf.ols('y_aracilik~x+araci',data=data).fit();mt=smf.ols('y_aracilik~x',data=data).fit()
    a,b=float(ma.params['x']),float(my.params['araci']);ratio=float(np.sqrt(my.ssr/ma.ssr))
    ref=json.loads((BASE/'sonuclar/ozet.json').read_text());np.testing.assert_allclose(a*b,ref['aracilik']['ab'],rtol=1e-12)
    rho_zero=float(b/np.sqrt(b*b+ratio*ratio))
    np.testing.assert_allclose(rho_zero,stats.pearsonr(ma.resid,mt.resid).statistic,rtol=1e-12)
    np.testing.assert_allclose(rho_zero,optimize.brentq(lambda rho:float(sensitivity(a,b,ratio,rho)),-.99,.99),rtol=1e-12)
    rho_grid=[-.6,-.3,0,.3,.6,.8];sens=[dict(rho=rho,ab_assumption=float(sensitivity(a,b,ratio,rho))) for rho in rho_grid]
    data=data.assign(x_c=data.x-data.x.mean(),w_c=data.w-data.w.mean());data['etkilesim']=data.x_c*data.w_c
    mod=smf.ols('y_duzenleyicilik~x_c+w_c+etkilesim',data=data).fit()
    beta=mod.params[['x_c','etkilesim']].to_numpy();cov=mod.cov_params().loc[['x_c','etkilesim'],['x_c','etkilesim']].to_numpy()
    tcrit=float(stats.t.ppf(.975,mod.df_resid));jointcrit=float(np.sqrt(2*stats.f.ppf(.95,2,mod.df_resid)))
    point=roots(beta,cov,tcrit);simultaneous=roots(beta,cov,jointcrit)
    for critical,rr in [(tcrit,point),(jointcrit,simultaneous)]:
        for root in rr:
            lo,hi=band(beta,cov,root,critical);assert min(abs(lo),abs(hi))<1e-10
    wmin,wmax=float(data.w_c.min()),float(data.w_c.max());grid=np.linspace(wmin,wmax,201)
    ci=band(beta,cov,grid,tcrit);joint=band(beta,cov,grid,jointcrit)
    assert np.all(joint[:,0]<=ci[:,0]+1e-12) and np.all(joint[:,1]>=ci[:,1]-1e-12)
    output=here/'sonuclar';output.mkdir(exist_ok=True)
    result=dict(simulation=True,n=160,generation_seed=original.URETIM_TOHUMU,full_precision_generator=True,csv_rounded_6_checked=True,
        mediation=dict(a=a,b_OLS=b,residual_SD_ratio_same_n=ratio,rho_zero_point=rho_zero,grid=sens,
            true_generation_rho=0,sensitivity_CI_computed=False,interpretation='Hypothesized error correlation in linear normal equations, not estimated confounding or causal proof'),
        moderation=dict(beta=beta.tolist(),covariance=cov.tolist(),df=int(mod.df_resid),w_mean=float(data.w.mean()),w_centered_range=[wmin,wmax],
            pointwise_t_critical=tcrit,pointwise_roots_centered=point,simultaneous_critical=jointcrit,simultaneous_roots_centered=simultaneous,
            interpretation='Separate simulated moderation response; pointwise JN is not simultaneous; 2-parameter normal/homoskedastic F ellipse band'),
        limits='No real participants, no conditional mediation combining responses, no bootstrap sensitivity interval, no HC3/cluster JN or causal identification test.',
        versions=dict(numpy=np.__version__,pandas=pd.__version__,scipy=scipy.__version__,statsmodels=statsmodels.__version__))
    (output/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    pd.DataFrame(sens).to_csv(output/'rho-duyarlilik.csv',index=False)
    pd.DataFrame(dict(w_centered=grid,slope=beta[0]+beta[1]*grid,point_lower=ci[:,0],point_upper=ci[:,1],joint_lower=joint[:,0],joint_upper=joint[:,1])).to_csv(output/'egim-bantlari.csv',index=False)
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
