"""Gerçek kaynaktan öğretim alt kümesi: hücre ağırlığı ve HC3 kontrastları."""
from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
from scipy.stats import t
import statsmodels.api as sm

CELLS=[(s,d) for s in ['OJ','VC'] for d in [.5,1.,2.]]
KEEP=[5,10,8,10,6,9]


def fit_cells(data):
    if data[['len','supp','dose']].isna().any().any() or not np.isfinite(data.len).all():raise ValueError('Tam sonlu veri gerekir.')
    X=np.column_stack([((data.supp==s)&(data.dose==d)).to_numpy(float) for s,d in CELLS])
    if not np.all(X.sum(1)==1) or np.any(X.sum(0)<2):raise ValueError('Altı dolu hücrede en az ikişer bağımsız kayıt gerekir.')
    inverse=np.linalg.inv(X.T@X);b=inverse@X.T@data.len.to_numpy()
    residual=data.len.to_numpy()-X@b;h=np.einsum('ij,jk,ik->i',X,inverse,X)
    covariance=inverse@(X.T@(((residual/(1-h))**2)[:,None]*X))@inverse
    return b,covariance,X,len(data)-6


def contrast(b,V,c,df,family=1):
    c=np.asarray(c,float)
    if c.shape!=(6,) or not np.isfinite(c).all() or df<=0 or family<1:raise ValueError('Geçerli kontrast ve aile gerekir.')
    estimate=float(c@b);se=float(np.sqrt(c@V@c));critical=t.ppf(1-.05/(2*family),df)
    return dict(estimate=estimate,se=se,df=df,nominal_p=float(2*t.sf(abs(estimate/se),df)),
                ci_family95=(estimate+np.array([-1,1])*critical*se).tolist())


def main():
    directory=Path(__file__).resolve().parent
    path=directory.parents[1]/'b06-parametrik-testler/kaynak/ToothGrowth.csv'
    raw=path.read_bytes();assert hashlib.sha256(raw.rstrip(b'\n')+b'\n').hexdigest()=='654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3'
    full=pd.read_csv(path);parts=[full.loc[(full.supp==s)&(full.dose==d)].sort_values('kaynak_satir').head(k) for (s,d),k in zip(CELLS,KEEP)]
    data=pd.concat(parts,ignore_index=True);b,V,X,df=fit_cells(data)
    reference=sm.OLS(data.len.to_numpy(),X).fit().get_robustcov_results(cov_type='HC3',use_t=True)
    np.testing.assert_allclose(b,reference.params,atol=1e-12);np.testing.assert_allclose(V,reference.cov_params(),atol=1e-12)
    counts=X.sum(0);equal=np.ones(3)/3;pooled=(counts[:3]+counts[3:])/len(data)
    weights={'equal_dose':np.r_[equal,-equal],'common_observed_dose':np.r_[pooled,-pooled],
             'different_group_composition':np.r_[counts[:3]/counts[:3].sum(),-counts[3:]/counts[3:].sum()]}
    estimates={k:contrast(b,V,c,df) for k,c in weights.items()}
    rawgap=data.loc[data.supp=='OJ','len'].mean()-data.loc[data.supp=='VC','len'].mean()
    np.testing.assert_allclose(estimates['different_group_composition']['estimate'],rawgap)
    interaction=[np.array([-1,1,0,1,-1,0.]),np.array([-1,0,1,1,0,-1.])]
    pairs=[contrast(b,V,c,df,family=2) for c in interaction]
    result=dict(n=len(data),cell_counts=counts.astype(int).tolist(),cell_order=CELLS,kept_source_rows=data.kaynak_satir.tolist(),
        cell_means=b.tolist(),marginal_targets=estimates,interaction_differences=pairs,
        conditions='Teaching subset selected by source order, not new/missing-at-random data. Independent records; saturated cell means; HC3 with residual-df t approximation. Marginal targets are pointwise; only the two specified interaction contrasts form a Bonferroni family. No causal or population inference.')
    out=directory/'sonuclar';out.mkdir(exist_ok=True);data.to_csv(out/'ogretim-alt-kumesi.csv',index=False)
    (out/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
