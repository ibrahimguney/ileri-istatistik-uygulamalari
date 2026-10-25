"""Yalnız keşif yarısı: dört faktör denetimi ve regresyon faktör puanları.

Koşullu hesaplar sabit model parametreleriyle normal çalışma modeli içindir.
Yarım B okunmaz; puanlar klinik/bireysel karar için doğrulanmış değildir.
"""
from pathlib import Path
import importlib.util
import json
import numpy as np
import pandas as pd


def score_kernel(pattern, phi, uniqueness):
    L,P,psi=map(lambda a:np.asarray(a,float),(pattern,phi,uniqueness))
    if L.ndim!=2 or P.shape!=(L.shape[1],L.shape[1]) or psi.shape!=(L.shape[0],):
        raise ValueError('Matris boyutları uyumlu olmalı.')
    if not all(np.isfinite(a).all() for a in [L,P,psi]) or np.any(psi<=0):
        raise ValueError('Sonlu katsayılar ve pozitif özgüllük gerekir.')
    if not np.allclose(P,P.T) or np.linalg.eigvalsh(P).min()<=0:
        raise ValueError('Pozitif tanımlı faktör kovaryansı gerekir.')
    R=L@P@L.T+np.diag(psi)
    B=np.linalg.solve(R,L@P)
    C=P-P@L.T@B
    V=P-C
    if np.linalg.eigvalsh(C).min() < -1e-10:
        raise ValueError('Koşullu kovaryans uygun değil.')
    return R,B,C,V


def correlation(covariance):
    covariance=np.asarray(covariance,float)
    sd=np.sqrt(np.diag(covariance))
    if np.any(sd<=0):raise ValueError('Pozitif varyans gerekir.')
    return covariance/np.outer(sd,sd)


def bartlett_kernel(pattern,uniqueness):
    L,psi=np.asarray(pattern,float),np.asarray(uniqueness,float)
    if L.ndim!=2 or psi.shape!=(len(L),) or not np.isfinite(L).all() or not np.isfinite(psi).all() or np.any(psi<=0):
        raise ValueError('Uygun yük ve pozitif özgüllük gerekir.')
    precision_L=L/psi[:,None]
    information=L.T@precision_L
    if np.linalg.matrix_rank(information)<L.shape[1]:
        raise ValueError('Bartlett puanı için tam sütun rankı gerekir.')
    covariance=np.linalg.inv(information)
    return precision_L@covariance,covariance


def main():
    directory=Path(__file__).resolve().parent;parent=directory.parent
    names=[f'{s}{j}' for s in ['A','C'] for j in range(1,6)]
    data=pd.read_csv(parent/'puanlanmis.csv').sort_values('kaynak_satir')
    split=pd.read_csv(parent/'bolme.csv')
    assert len(data)==1316 and data.kaynak_kayit.is_unique
    assert set(data.kaynak_kayit)==set(split.loc[split.yarim=='A','kaynak_kayit'])
    assert not set(data.kaynak_kayit)&set(split.loc[split.yarim=='B','kaynak_kayit'])
    values=data[names].to_numpy(float)
    assert np.isfinite(values).all() and np.isin(values,np.arange(1,7)).all()
    R=np.corrcoef(values,rowvar=False)
    reference=json.loads((parent/'sonuclar/ozet.json').read_text())
    L=np.array(reference['rotation']['pattern']);P=np.array(reference['rotation']['phi'])
    psi=1-np.diag(L@P@L.T)
    np.testing.assert_allclose(R,pd.read_csv(parent/'sonuclar/korelasyon.csv',index_col=0).to_numpy(),atol=1e-12)
    model,B,C,V=score_kernel(L,P,psi)
    np.testing.assert_allclose(model,pd.read_csv(parent/'sonuclar/yeniden_uretilen.csv',index_col=0).to_numpy(),atol=1e-12)
    means=values.mean(axis=0);sds=values.std(axis=0,ddof=1)
    standardized=(values-means)/sds
    scores=standardized@B
    BB,bartlett_error=bartlett_kernel(L,psi)
    bartlett_scores=standardized@BB
    # Önceki PAF yordamı ayrı modül adıyla yüklenir; ana analizi çalıştırmaz.
    spec=importlib.util.spec_from_file_location('efa_reference',parent/'analiz.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    loadings,four=module.principal_axes(R,4)
    # Uygunsuz/yakınsamayan çözümden yorum tablosu veya faktör puanı üretilmez.
    four['accepted_for_interpretation']=False
    result=dict(n_half_A=len(data),half_B_responses_read=False,four_factor_PAF=four,
        regression_scores=dict(factor_correlation=P.tolist(),conditional_covariance=C.tolist(),
        model_score_covariance=V.tolist(),model_score_correlation=correlation(V).tolist(),
        empirical_score_correlation=np.corrcoef(scores,rowvar=False).tolist(),
        determinacy_under_model=np.sqrt(np.diag(V)/np.diag(P)).tolist(),
        conditional_sd=np.sqrt(np.diag(C)).tolist(),
        conditional_normal_halfwidth95=(1.959963984540054*np.sqrt(np.diag(C))).tolist()),
        bartlett_scores=dict(model_score_correlation=correlation(P+bartlett_error).tolist(),
        empirical_score_correlation=np.corrcoef(bartlett_scores,rowvar=False).tolist(),
        model_mean_square_error=bartlett_error.tolist()),
        limits='Fixed estimated two-factor model, normal working-model conditional moments; excludes loading/rotation/factor-number uncertainty. No bootstrap stability, ordinal model, new-population validation or individual diagnosis. Four-factor attempt is a numerical diagnostic, not factor-count proof.')
    out=directory/'sonuclar';out.mkdir(exist_ok=True)
    pd.DataFrame(B,index=names,columns=['A','C']).to_csv(out/'puan-katsayilari.csv')
    pd.DataFrame(BB,index=names,columns=['A','C']).to_csv(out/'bartlett-katsayilari.csv')
    pd.DataFrame({'mean_A':means,'sd_A_ddof1':sds},index=names).to_csv(out/'egitim-standartlastirma.csv')
    (out/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
