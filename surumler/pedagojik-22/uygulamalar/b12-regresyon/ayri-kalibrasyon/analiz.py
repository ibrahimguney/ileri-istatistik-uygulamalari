"""Sabit eğitim/kalibrasyon/kontrol rolleriyle split conformal öğretimi."""
from pathlib import Path
import hashlib,json,math
import numpy as np
import pandas as pd
import scipy
from scipy import stats
import statsmodels.api as sm
ALPHA=.05

def check_frame(frame):
    required=['kaynak_satir','G1','G3']
    if not set(required)<=set(frame) or frame[required].isna().any().any() or frame.kaynak_satir.duplicated().any():
        raise ValueError("Tam ve benzersiz kaynak satırları gerekir")
    if not np.isfinite(frame[['G1','G3']].to_numpy(float)).all():raise ValueError("Sonlu değer gerekir")

def roles(train,calibration,audit):
    for frame in [train,calibration,audit]:check_frame(frame)
    ids=[set(f.kaynak_satir) for f in [train,calibration,audit]]
    if any(ids[i]&ids[j] for i,j in [(0,1),(0,2),(1,2)]):raise ValueError("Eğitim/kalibrasyon/kontrol rolleri kesişemez")

def fit(train):
    check_frame(train);x=train.G1.to_numpy(float);y=train.G3.to_numpy(float)
    if len(x)<3 or np.ptp(x)==0:raise ValueError("Tam sıralı tasarım ve en az3 eğitim kaydı gerekir")
    design=np.column_stack([np.ones(len(x)),x]);beta=np.linalg.lstsq(design,y,rcond=None)[0]
    sxx=float(np.sum((x-x.mean())**2));s=float(np.sqrt(np.sum((y-design@beta)**2)/(len(x)-2)))
    return dict(beta=beta.tolist(),n=len(x),x_mean=float(x.mean()),Sxx=sxx,residual_sd=s)

def predict(model,x):
    x=np.asarray(x,float)
    if not np.isfinite(x).all():raise ValueError("Sonlu açıklayıcı gerekir")
    return model['beta'][0]+model['beta'][1]*x

def corrected_quantile(scores,alpha=ALPHA):
    scores=np.asarray(scores,float)
    if scores.ndim!=1 or len(scores)<1 or not np.isfinite(scores).all() or np.any(scores<0) or not 0<alpha<1:
        raise ValueError("Sonlu, negatif olmayan kalibrasyon skorları ve uygun alpha gerekir")
    k=math.ceil((len(scores)+1)*(1-alpha))
    return (float(np.sort(scores)[k-1]) if k<=len(scores) else float('inf')),k

def calibrate(model,calibration,alpha=ALPHA):
    check_frame(calibration);scores=np.abs(calibration.G3.to_numpy(float)-predict(model,calibration.G1))
    q,k=corrected_quantile(scores,alpha)
    return dict(q=q,k=k,m=len(scores),scores=scores.tolist(),alpha=alpha)

def intervals(model,calibration,x):
    point=predict(model,x);q=calibration['q']
    return np.column_stack([point-q,point+q])

def classical_individual(model,x,alpha=ALPHA):
    x=np.asarray(x,float);point=predict(model,x)
    half=stats.t.ppf(1-alpha/2,model['n']-2)*model['residual_sd']*np.sqrt(1+1/model['n']+(x-model['x_mean'])**2/model['Sxx'])
    return np.column_stack([point-half,point+half])

def main():
    here=Path(__file__).parent;source=here.parent/'kaynak/uci-portekizce-ilk80-notlar.csv';raw=source.read_bytes();frame=pd.read_csv(source)
    reference=json.loads((here.parent/'sonuclar/ozet.json').read_text());assert hashlib.sha256(raw).hexdigest()==reference['local_projection_sha256']
    assert len(frame)==80 and frame.school.eq('GP').all() and frame.kaynak_satir.tolist()==list(range(1,81))
    train=frame.iloc[:40].copy();cal=frame.iloc[40:60].copy();audit=frame.iloc[60:80].copy();roles(train,cal,audit)
    model=fit(train);calibrated=calibrate(model,cal)
    assert np.isfinite(calibrated['q'])
    regression=stats.linregress(train.G1,train.G3);np.testing.assert_allclose(model['beta'],[regression.intercept,regression.slope],rtol=1e-12)
    x0=[12.];point12=float(predict(model,x0)[0]);conf12=intervals(model,calibrated,x0)[0];classic12=classical_individual(model,x0)[0]
    point=predict(model,audit.G1);conf=intervals(model,calibrated,audit.G1);classic=classical_individual(model,audit.G1);y=audit.G3.to_numpy(float)
    check=sm.OLS(train.G3,sm.add_constant(train.G1,has_constant='add')).fit()
    frame_check=check.get_prediction(sm.add_constant(audit.G1,has_constant='add')).summary_frame(alpha=ALPHA)
    np.testing.assert_allclose(classic,frame_check[['obs_ci_lower','obs_ci_upper']].to_numpy(),rtol=1e-12)
    inside=(y>=conf[:,0])&(y<=conf[:,1]);classic_inside=(y>=classic[:,0])&(y<=classic[:,1])
    result=dict(source_sha256=hashlib.sha256(raw).hexdigest(),roles=dict(train=[1,40],calibration=[41,60],audit=[61,80]),
        model_40=model,calibration={k:v for k,v in calibrated.items() if k!='scores'},
        at_G1_12=dict(point=point12,split_conformal=conf12.tolist(),classical_individual=classic12.tolist()),
        audit_20=dict(n=len(audit),split_conformal_covered=int(inside.sum()),split_conformal_fraction=float(inside.mean()),
            constant_width=float(2*calibrated['q']),classical_covered=int(classic_inside.sum()),classical_fraction=float(classic_inside.mean()),
            classical_average_width=float(np.mean(classic[:,1]-classic[:,0])),RMSE=float(np.sqrt(np.mean((y-point)**2)))),
        ideal_marginal_coverage_without_ties=calibrated['k']/(calibrated['m']+1),
        limits='Source-ordered single-school data do not establish exchangeability; observed20 coverage is descriptive, not guaranteed future/conditional/simultaneous coverage. Model frozen after train40, no refit after calibration; no clipping, tuning or normalized-score conformal.',
        versions=dict(numpy=np.__version__,pandas=pd.__version__,scipy=scipy.__version__))
    out=here/'sonuclar';out.mkdir(exist_ok=True);(out/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    cal.assign(tahmin=predict(model,cal.G1),mutlak_skor=calibrated['scores']).to_csv(out/'kalibrasyon.csv',index=False)
    audit.assign(tahmin=point,alt=conf[:,0],ust=conf[:,1],kapsandi=inside,klasik_alt=classic[:,0],klasik_ust=classic[:,1]).to_csv(out/'kontrol.csv',index=False)
    assert source.read_bytes()==raw
    print(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False))
if __name__=='__main__':main()
