"""Gerçek sleepstudy üzerinde ayrı eksik-izlem kopyası; aynı eğim modeli."""
import hashlib
import json
from pathlib import Path
import warnings
import numpy as np
import pandas as pd
from scipy import stats
from scipy.special import expit
import statsmodels.formula.api as smf
from statsmodels.stats.multitest import multipletests

SEED = 20261025


def validate_panel(frame):
    required = {'Subject','Days','DaysB','Reaction'}
    if not required <= set(frame) or frame[['Subject','Days','DaysB']].isna().any().any():
        raise ValueError('Panel anahtarı/sütunları eksik')
    if frame.duplicated(['Subject','Days']).any():
        raise ValueError('Kişi-gün anahtarı tekrarlı')
    if not np.isfinite(frame['Reaction'].dropna()).all():
        raise ValueError('Gözlenen tepkiler sonlu olmalı')


def mask_followup(frame):
    validate_panel(frame)
    ordered = frame.sort_values(['Subject','Days']).copy()
    rng = np.random.default_rng(SEED)
    rows = []
    for subject,g in ordered.groupby('Subject',sort=True):
        baseline = g.loc[g.DaysB.eq(0),'Reaction']
        if len(baseline)!=1 or pd.isna(baseline.iloc[0]):
            raise ValueError('Her kişinin gözlenen temeli olmalı')
        hazard = float(expit(-2+.025*(baseline.iloc[0]-265)))
        dropped = False
        for idx,row in g.iterrows():
            if row.DaysB>=2:
                if not dropped:
                    dropped = bool(rng.random()<hazard)
                if dropped:
                    ordered.loc[idx,'Reaction'] = np.nan
            rows.append({'Subject':subject,'Days':row.Days,'masked':dropped,'hazard_given_baseline':hazard})
    validate_panel(ordered)
    return ordered,pd.DataFrame(rows)


def fit_same_model(frame):
    validate_panel(frame)
    observed = frame.dropna(subset=['Reaction']).copy()
    if (observed.groupby('Subject').size()<2).any():
        raise ValueError('Bu öğretim örneği her kişide en az iki ölçüm ister')
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        fit = smf.mixedlm('Reaction~DaysB',observed,groups=observed.Subject,re_formula='~DaysB').fit(reml=True,method=['lbfgs'])
    covariance = np.asarray(fit.cov_re)
    assert fit.converged and np.isfinite(fit.fe_params).all() and np.isfinite(fit.bse_fe).all()
    assert np.linalg.eigvalsh(covariance).min()>0 and fit.scale>0
    slope,se = float(fit.fe_params['DaysB']),float(fit.bse_fe['DaysB'])
    return {'rows':len(observed),'subjects':observed.Subject.nunique(),'converged':bool(fit.converged),
            'slope':slope,'slope_SE':se,'slope_z':slope/se,
            'normal_Wald_CI95':[slope-stats.norm.ppf(.975)*se,slope+stats.norm.ppf(.975)*se],
            'random_covariance_eigenvalues':np.linalg.eigvalsh(covariance).tolist(),
            'residual_SD':float(np.sqrt(fit.scale)),
            'warnings':[str(w.message) for w in caught],
            'inference':'Normal Wald yaklaşımı; Satterthwaite/Kenward-Roger sd hesaplanmadı'}


def main():
    directory = Path(__file__).parent
    source = directory.parent/'kaynak/sleepstudy.csv'
    original = source.read_bytes()
    normalized = original.replace(b'\r\n',b'\n').rstrip(b'\n')+b'\n'
    assert hashlib.sha256(normalized).hexdigest() == 'e4783c6b6ac6dcbfdf0e6731e4f0024166ca7416243873a480a64c40839a0af6'
    raw = pd.read_csv(source)
    full = raw.loc[raw.Days.ge(2)].copy()
    full['DaysB'] = full.Days-2
    assert len(full)==144 and full.Subject.nunique()==18 and not full.isna().any().any()
    masked,mask = mask_followup(full)
    counts = masked.groupby('Subject').Reaction.count()
    complete_ids = counts[counts.eq(8)].index
    complete = masked.loc[masked.Subject.isin(complete_ids)].copy()
    assert masked.Reaction.isna().sum()==40 and masked.Reaction.count()==104 and len(complete_ids)==7
    assert (counts>=2).all()
    pd.testing.assert_frame_equal(masked[['Subject','Days','DaysB']],full.sort_values(['Subject','Days'])[['Subject','Days','DaysB']])
    compare = {'full_reference':fit_same_model(full),'masked_available':fit_same_model(masked),'masked_complete_subjects':fit_same_model(complete)}
    # Dört yaşa özgü ayrı Welch sorusu; öğretim ailesi baştan dört olarak tanımlı.
    ortho_source = directory.parent/'kaynak/Orthodont.csv'
    ortho_original = ortho_source.read_bytes()
    assert hashlib.sha256(ortho_original.replace(b'\r\n',b'\n').rstrip(b'\n')+b'\n').hexdigest()=='2eacb310cb54353189058bd1acdfec400009bb9bd28d1afbdb012c90265284a0'
    ortho = pd.read_csv(ortho_source)
    effects = []
    for age in [8,10,12,14]:
        male = ortho.loc[ortho.age.eq(age)&ortho.Sex.eq('Male'),'distance']
        female = ortho.loc[ortho.age.eq(age)&ortho.Sex.eq('Female'),'distance']
        tested = stats.ttest_ind(male,female,equal_var=False)
        effects.append({'age':age,'male_n':len(male),'female_n':len(female),
                        'mean_male_minus_female':float(male.mean()-female.mean()),'p_raw':float(tested.pvalue)})
    p = np.array([e['p_raw'] for e in effects])
    holm = multipletests(p,method='holm')[1]
    for e,h,b in zip(effects,holm,np.minimum(1,4*p)):
        e.update(p_Holm=float(h),p_Bonferroni=float(b))
    output = directory/'sonuclar'
    output.mkdir(exist_ok=True)
    masked.to_csv(output/'eksik-izlem-ogretim.csv',index=False)
    mask.to_csv(output/'maske-kaydi.csv',index=False)
    pd.DataFrame(compare).T.to_csv(output/'ayni-model-karsilastirma.csv')
    pd.DataFrame(effects).to_csv(output/'yas-ailesi.csv',index=False)
    result = {'scope':'Özgün veride eksik yok; sonradan maskelenmiş öğretim kopyası',
              'seed':SEED,'hazard':'expit(-2 + .025*(observed baseline Reaction - 265)); first two days retained',
              'masked_measurements':40,'observed_measurements':104,'retained_subjects':18,'complete_subjects':7,
              'same_linear_REML_model':compare,'age_specific_teaching_family':effects,
              'MNAR_sensitivity_performed':False,'small_sample_df_correction':False,
              'versions':{'numpy':np.__version__,'pandas':pd.__version__}}
    (output/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    assert source.read_bytes()==original and ortho_source.read_bytes()==ortho_original
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
