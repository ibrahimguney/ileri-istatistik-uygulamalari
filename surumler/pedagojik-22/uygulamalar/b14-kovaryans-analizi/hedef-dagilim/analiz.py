"""Aynı ANCOVA/hücre modellerinde sabit hedef doz dağılımı öğretimi."""
from pathlib import Path
import importlib.util,hashlib,json,os,tempfile
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR']=tempfile.mkdtemp(prefix='b14-mpl-')
import numpy as np
import pandas as pd
import scipy
from scipy import stats
import statsmodels
BASE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('b14_original_analysis',BASE/'analiz.py')
original=importlib.util.module_from_spec(spec);spec.loader.exec_module(original)
DOSES=np.array([.5,1.,2.])
TARGETS={'equal':[1/3,1/3,1/3],'low_dose':[.6,.3,.1],'high_dose':[.1,.1,.8]}

def weights(w):
    w=np.asarray(w,float)
    if w.shape!=(3,) or not np.isfinite(w).all() or np.any(w<0) or not np.isclose(w.sum(),1,rtol=0,atol=1e-12):
        raise ValueError("Üç doz için sonlu, negatif olmayan ve toplamı1 ağırlık gerekir")
    return w

def check_support(data):
    if not {'supp','dose','len'}<=set(data) or data[['supp','dose','len']].isna().any().any():raise ValueError("Tam grup/doz/yanıt gerekir")
    if not np.isfinite(data[['dose','len']].to_numpy(float)).all() or not data.supp.isin(['VC','OJ']).all() or not data.dose.isin(DOSES).all():raise ValueError("Bilinmeyen/sonlu olmayan veri")
    counts=data.groupby(['supp','dose']).size()
    if len(counts)!=6 or counts.min()<2:raise ValueError("Her iki grupta üç dozun her birinde en az2 kayıt gerekir; destek uydurulmaz")

def fit_all(data):
    check_support(data)
    return {name:original.fit(data.len.to_numpy(float),original.design(data,name)) for name in ['additive','interaction','cells']}

def standardize(model,cov,w,model_name,family=3):
    w=weights(w)
    if family<1 or int(family)!=family:raise ValueError("Pozitif tam aile büyüklüğü gerekir")
    v=original.design(pd.DataFrame(dict(supp=['VC']*3,dose=DOSES)),model_name)
    o=original.design(pd.DataFrame(dict(supp=['OJ']*3,dose=DOSES)),model_name)
    lv=w@v;lo=w@o;l=lo-lv
    estimate=float(l@model.params);se=float(np.sqrt(l@cov@l));crit=stats.t.ppf(1-.05/(2*family),model.df_resid)
    return dict(weights=w.tolist(),mean_dose=float(w@DOSES),VC_mean=float(lv@model.params),OJ_mean=float(lo@model.params),difference=estimate,SE=se,
        family_size=family,df=int(model.df_resid),bonferroni_family_CI_95=(estimate+np.array([-1,1])*crit*se).tolist(),contrast=l.tolist())

def main():
    here=Path(__file__).parent;source=BASE.parent/'b06-parametrik-testler/kaynak/ToothGrowth.csv';raw=source.read_bytes()
    assert hashlib.sha256(raw.replace(b"\r\n",b"\n").rstrip(b"\n")+b"\n").hexdigest()==original.SOURCE_HASH
    data=pd.read_csv(source);assert len(data)==60
    fits=fit_all(data);ref=json.loads((BASE/'sonuclar/ozet.json').read_text());rows=[]
    for name,(model,hc3) in fits.items():
        np.testing.assert_allclose(model.params,ref['models'][name]['parameters'],rtol=1e-12,atol=1e-12)
        for target,w in TARGETS.items():
            for cov_name,cov in [('OLS',model.cov_params()),('HC3_t_approx',hc3)]:
                r=standardize(model,cov,w,name,family=1 if name=='additive' else 3);rows.append(dict(model=name,target=target,covariance=cov_name,**r))
    cell=fits['cells'][0];means=np.array([data.loc[(data.supp=='OJ')&(data.dose==d),'len'].mean()-data.loc[(data.supp=='VC')&(data.dose==d),'len'].mean() for d in DOSES])
    for row in rows:
        if row['model']=='cells':np.testing.assert_allclose(row['difference'],np.dot(row['weights'],means),rtol=1e-12,atol=1e-12)
    result=dict(source_normalized_sha256=original.SOURCE_HASH,n=60,per_cell=10,cell_differences=means.tolist(),comparisons=rows,
        target_definition='Three fixed teaching dose distributions, not external population estimates or new animals; same weights applied to both groups',
        limits='Weights treated as known; OLS Bonferroni family3 within each interaction/cells model/covariance; additive is one identical contrast, family1. HC3 t approximate. Different targets, not same-parameter sensitivity; no protection over model search or all book tests, no causal transport or weight uncertainty.',
        versions=dict(numpy=np.__version__,pandas=pd.__version__,scipy=scipy.__version__,statsmodels=statsmodels.__version__))
    out=here/'sonuclar';out.mkdir(exist_ok=True);(out/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    pd.DataFrame([{k:v for k,v in r.items() if k not in ['weights','contrast','bonferroni_family_CI_95']}|dict(lower=r['bonferroni_family_CI_95'][0],upper=r['bonferroni_family_CI_95'][1]) for r in rows]).to_csv(out/'hedef-karsilastirmalari.csv',index=False)
    assert source.read_bytes()==raw
    print(json.dumps([r for r in rows if r['model']=='cells'],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
