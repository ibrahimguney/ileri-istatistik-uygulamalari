"""Aynı öğrenci satırını koruyan Pearson/Spearman bootstrap öğretimi."""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
import scipy
from scipy import stats
SEED=20261025
B=20000

def validate(pairs):
    p=np.asarray(pairs,float)
    if p.ndim!=2 or p.shape[1]!=2 or len(p)<4 or not np.isfinite(p).all():
        raise ValueError("En az4 tam ve sonlu (X,Y) satırı gerekir")
    if np.any(np.ptp(p,axis=0)==0):raise ValueError("Sabit sütunda korelasyon tanımsız")
    return p[np.lexsort((p[:,1],p[:,0]))]

def row_correlation(x,y):
    x=x-x.mean(axis=-1,keepdims=True);y=y-y.mean(axis=-1,keepdims=True)
    denominator=np.sqrt(np.sum(x*x,axis=-1)*np.sum(y*y,axis=-1))
    return np.divide(np.sum(x*y,axis=-1),denominator,out=np.full_like(denominator,np.nan,dtype=float),where=denominator>0)

def coefficients(pairs):
    p=validate(pairs);r=float(row_correlation(p[:,0],p[:,1]));rs=float(row_correlation(stats.rankdata(p[:,0]),stats.rankdata(p[:,1])))
    return np.array([r,rs,rs-r])

def paired_bootstrap(pairs,repetitions=B,seed=SEED,marker_pair=None):
    p=validate(pairs)
    if repetitions<100:raise ValueError("En az100 tekrar")
    rng=np.random.default_rng(seed);idx=rng.integers(0,len(p),size=(repetitions,len(p)))
    drawn=p[idx];x,y=drawn[:,:,0],drawn[:,:,1]
    r=row_correlation(x,y)
    # Eski sıralar çekilmez: her bootstrap örnekleminde bağlar yeniden sıralanır.
    rs=row_correlation(stats.rankdata(x,axis=1,method='average'),stats.rankdata(y,axis=1,method='average'))
    valid=np.isfinite(r)&np.isfinite(rs);est=np.column_stack([r,rs,rs-r])
    if not valid.all():raise ValueError(f"{int((~valid).sum())} dejenere tekrar; aralık sessizce hesaplanmaz")
    for i in range(5):
        np.testing.assert_allclose([r[i],rs[i]],[stats.pearsonr(x[i],y[i]).statistic,stats.spearmanr(x[i],y[i]).statistic],rtol=1e-12,atol=1e-13)
    rows=[]
    for j,name in enumerate(['Pearson_r','Spearman_rs','rs_minus_r']):
        rows.append(dict(target=name,estimate=float(coefficients(p)[j]),interval_percentile_95=np.quantile(est[:,j],[.025,.975],method='linear').tolist()))
    result=dict(n=len(p),repetitions=repetitions,seed=seed,degenerate_replicates=0,intervals=rows,
        unit='Whole student (G1,G3) row; same resample for both coefficients',ranks_recomputed=True,
        interval_type='Approximate percentile, linear quantiles; no calibrated coverage claim')
    if marker_pair is not None:
        positions=np.flatnonzero(np.all(p==marker_pair,axis=1))
        if len(positions)!=1:raise ValueError("İşaretlenen çift benzersiz olmalı")
        count=(idx==positions[0]).sum(axis=1)
        result['marker_diagnostic']=[dict(source_row_1_drawn=bool(flag),replicates=int(mask.sum()),
            pearson_median=float(np.median(r[mask])),pearson_percentiles_025_975=np.quantile(r[mask],[.025,.975],method='linear').tolist())
            for flag,mask in [(False,count==0),(True,count>0)]]
        result['marker_expected_absence_probability']=float((1-1/len(p))**len(p))
    return result

def main():
    here=Path(__file__).parent;source=here.parent.parent/'b12-regresyon/kaynak/uci-portekizce-ilk80-notlar.csv';raw=source.read_bytes();frame=pd.read_csv(source)
    reference=json.loads((here.parent/'sonuclar/ozet.json').read_text());assert hashlib.sha256(raw).hexdigest()==reference['local_projection_sha256']
    assert len(frame)==80 and frame.school.eq('GP').all() and frame.kaynak_satir.tolist()==list(range(1,81))
    pairs=frame.iloc[:60][['G1','G3']].to_numpy(float);coef=coefficients(pairs)
    np.testing.assert_allclose(coef[:2],[reference['main']['pearson_r'],reference['main']['spearman_r']],rtol=1e-12)
    result=dict(source_sha256=hashlib.sha256(raw).hexdigest(),selection='First60 source-ordered GP records; not a random sample',
        bootstrap=paired_bootstrap(pairs,marker_pair=[0,11]),
        transformed_G1_squared=dict(pearson=float(stats.pearsonr(pairs[:,0]**2,pairs[:,1]).statistic),spearman=float(stats.spearmanr(pairs[:,0]**2,pairs[:,1]).statistic)),
        agreement_teaching=dict(description='Constructed Ydagger=X+5 from G1, not new observed grades; only algebra illustration',
            r=float(stats.pearsonr(pairs[:,0],pairs[:,0]+5).statistic),mean_difference=float(np.mean((pairs[:,0]+5)-pairs[:,0]))),
        limits='iid row resampling is a model assumption, not established by source order; no cluster bootstrap, BCa, coverage simulation, agreement analysis or dependent Pearson-equality test',
        versions=dict(numpy=np.__version__,pandas=pd.__version__,scipy=scipy.__version__))
    np.testing.assert_allclose(result['transformed_G1_squared']['spearman'],coef[1])
    out=here/'sonuclar';out.mkdir(exist_ok=True);(out/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    pd.DataFrame([dict(target=row['target'],estimate=row['estimate'],lower=row['interval_percentile_95'][0],upper=row['interval_percentile_95'][1]) for row in result['bootstrap']['intervals']]).to_csv(out/'araliklar.csv',index=False)
    assert source.read_bytes()==raw
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
