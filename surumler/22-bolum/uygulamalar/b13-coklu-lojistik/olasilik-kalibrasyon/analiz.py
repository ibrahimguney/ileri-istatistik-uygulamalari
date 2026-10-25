"""Sabit lojistik modelde olasılık belirsizliği ve sıralama/kalibrasyon ayrımı."""
from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
import scipy
from scipy import stats
from scipy.special import expit
import statsmodels.api as sm

def metrics(y,eta):
    y=np.asarray(y,float);eta=np.asarray(eta,float)
    if y.ndim!=1 or eta.shape!=y.shape or not np.isfinite(eta).all() or not np.isin(y,[0,1]).all() or len(np.unique(y))!=2:
        raise ValueError("İki sınıf, sonlu logit ve eşit boyut gerekir")
    p=expit(eta);positive=eta[y==1];negative=eta[y==0]
    auc=float(np.mean((positive[:,None]>negative)+.5*(positive[:,None]==negative)))
    ranks=stats.rankdata(eta);n1=len(positive);n0=len(negative)
    np.testing.assert_allclose(auc,(ranks[y==1].sum()-n1*(n1+1)/2)/(n1*n0))
    return dict(AUC=auc,Brier=float(np.mean((y-p)**2)),log_loss=float(np.mean(np.logaddexp(0,eta)-y*eta)),
        mean_predicted=float(p.mean()),observed_fraction=float(y.mean()),observed_minus_predicted=float(np.mean(y-p)),
        accuracy_at_half=float(np.mean((eta>=0)==y)))

def profile(beta,cov,x):
    beta,cov,x=np.asarray(beta,float),np.asarray(cov,float),np.asarray(x,float)
    if beta.ndim!=1 or x.shape!=beta.shape or cov.shape!=(len(beta),len(beta)) or not all(np.isfinite(v).all() for v in [beta,cov,x]):raise ValueError("Geçerli katsayı/kovaryans/profil gerekir")
    v=float(x@cov@x)
    if v<0:raise ValueError("Negatif varyans")
    eta=float(x@beta);se=float(np.sqrt(v));z=stats.norm.ppf(.975)
    return dict(eta=eta,eta_SE=se,p=float(expit(eta)),probability_CI_95=expit(eta+np.array([-1,1])*z*se).tolist())

def difference(beta,cov,x0,x1):
    beta,cov,x0,x1=map(lambda a:np.asarray(a,float),[beta,cov,x0,x1])
    p0=profile(beta,cov,x0)['p'];p1=profile(beta,cov,x1)['p']
    gradient=p1*(1-p1)*x1-p0*(1-p0)*x0
    se=float(np.sqrt(gradient@cov@gradient));delta=p1-p0
    return dict(p0=p0,p1=p1,probability_difference=float(delta),delta_SE=se,
        delta_Wald_CI_95=(delta+np.array([-1,1])*stats.norm.ppf(.975)*se).tolist(),gradient=gradient.tolist())

def main():
    here=Path(__file__).parent;source=here.parent/'kaynak/uci-portekizce-ilk80-yas-notlar.csv'
    raw=source.read_bytes();data=pd.read_csv(source)
    expected='3ad427ac4ce8da8f4fc8d12fcb271d6f0a2699a0e086dc18d9ae4400636462b5'
    assert hashlib.sha256(raw.rstrip(b"\r\n")+b"\n").hexdigest()==expected
    assert len(data)==80 and data.school.eq('GP').all() and data.kaynak_satir.tolist()==list(range(1,81))
    x=np.column_stack([np.ones(80),data.G1,data.age-16]);y=(data.G3>=14).astype(int).to_numpy()
    fitted=sm.Logit(y[:60],x[:60]).fit(disp=False);assert fitted.mle_retvals['converged'];beta=np.asarray(fitted.params);cov=np.asarray(fitted.cov_params())
    ref=json.loads((here.parent/'sonuclar/ozet.json').read_text())
    np.testing.assert_allclose(beta,[ref['logistic']['coefficients'][n]['estimate'] for n in ['const','G1','age_c']],rtol=1e-10,atol=1e-10)
    points=np.array([[1,10,0],[1,12,0],[1,13,0],[1,14,0]],float)
    profiles=[dict(age=16,G1=int(v[1]),**profile(beta,cov,v)) for v in points]
    glm=sm.GLM(y[:60],x[:60],family=sm.families.Binomial()).fit(tol=1e-12,maxiter=200)
    check=glm.get_prediction(points).summary_frame(alpha=.05)
    np.testing.assert_allclose([r['probability_CI_95'] for r in profiles],check[['mean_ci_lower','mean_ci_upper']].to_numpy(),rtol=1e-6,atol=1e-7)
    delta=difference(beta,cov,[1,12,0],[1,13,0])
    eta=x[60:]@beta;rows=[dict(multiplier=c,**metrics(y[60:],c*eta)) for c in [.5,1.,2.]]
    np.testing.assert_allclose([r['AUC'] for r in rows],ref['transfer']['AUC'])
    np.testing.assert_allclose(rows[1]['Brier'],ref['transfer']['Brier'])
    result=dict(source_sha256=hashlib.sha256(raw).hexdigest(),training_n=60,training_events=int(y[:60].sum()),audit_n=20,audit_events=int(y[60:].sum()),
        profiles=profiles,age16_G1_12_to_13=delta,conditional_G1_OR=float(np.exp(beta[1])),audit_fixed_logit_transforms=rows,
        limits='Pointwise model-based normal/delta intervals, not Bernoulli future-observation prediction intervals or causal effects. Transform grid is algebra teaching, no selection/recalibration fitted on audit20. No calibration slope/curve, uncertainty for metrics, penalty or external validation.',
        versions=dict(numpy=np.__version__,pandas=pd.__version__,scipy=scipy.__version__,statsmodels=sm.__version__))
    out=here/'sonuclar';out.mkdir(exist_ok=True);(out/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    pd.DataFrame(rows).to_csv(out/'sirala-ve-kalibre-et.csv',index=False)
    pd.DataFrame([dict(age=r['age'],G1=r['G1'],p=r['p'],lower=r['probability_CI_95'][0],upper=r['probability_CI_95'][1]) for r in profiles]).to_csv(out/'profil-araliklari.csv',index=False)
    assert source.read_bytes()==raw
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
