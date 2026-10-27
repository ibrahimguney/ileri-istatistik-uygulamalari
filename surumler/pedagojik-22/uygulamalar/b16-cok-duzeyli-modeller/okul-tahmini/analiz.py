"""HSB boş modeli: hedef ortalama, dengesiz kümeler, koşullu tahmin.

Varyans bileşenleri toplulaştırılmış REML ile bağımsız hesaplanır.
Tahmin aralıkları parametreler sabit kabul edilen normal model içindir.
"""
from pathlib import Path
import hashlib
import json
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar


def summaries(data):
    if data[['School', 'MathAch']].isna().any().any():
        raise ValueError('Okul kimliği ve puan eksik olamaz.')
    if not np.isfinite(data.MathAch).all() or data.School.astype(str).str.strip().eq('').any():
        raise ValueError('Sonlu puan ve geçerli okul kimliği gerekir.')
    g = data.groupby('School', sort=True).MathAch
    table = g.agg(n='size', mean='mean')
    table['within_ss'] = g.apply(lambda x: float(np.sum((x-x.mean())**2)))
    if len(table) < 2 or table.n.sum() <= len(table):
        raise ValueError('En az iki okul ve okul içi bilgi gerekir.')
    return table


def reml(table):
    n, y = table.n.to_numpy(), table['mean'].to_numpy()
    N = int(n.sum())
    def profile(r):
        weights = n / (1+n*r)
        mean = float(weights @ y / weights.sum())
        q = float(table.within_ss.sum() + np.sum(weights*(y-mean)**2))
        sigma = q/(N-1)
        if sigma <= 0:
            raise ValueError('Pozitif artık varyansı gerekir.')
        objective = .5*((N-1)*np.log(sigma) + np.log1p(n*r).sum() + np.log(weights.sum()))
        return float(objective), mean, sigma
    result = minimize_scalar(lambda x: profile(np.exp(x))[0], bounds=(-20, 8),
                             method='bounded', options={'xatol': 1e-10})
    if not result.success:
        raise RuntimeError('REML profili yakınsamadı.')
    ratio = float(np.exp(result.x))
    if profile(0)[0] <= profile(ratio)[0]:
        ratio = 0.
    _, mean, sigma = profile(ratio)
    tau = ratio*sigma
    se = float(1/np.sqrt(np.sum(n/(sigma+n*tau))))
    return dict(intercept=mean, school_variance=tau, residual_variance=sigma, intercept_se=se)


def design_effect(n, tau, sigma):
    n = np.asarray(n, dtype=float)
    if n.ndim != 1 or len(n) == 0 or not np.isfinite(n).all() or np.any(n <= 0):
        raise ValueError('Pozitif sonlu küme büyüklükleri gerekir.')
    if not np.isfinite([tau, sigma]).all() or tau < 0 or sigma <= 0:
        raise ValueError('Geçersiz varyans.')
    icc = tau/(tau+sigma)
    N = float(n.sum())
    return dict(icc=icc, equal_size_approx=1+(n.mean()-1)*icc,
                unequal_size=1+(np.sum(n*n)/N-1)*icc,
                mean_variance=sigma/N+tau*np.sum(n*n)/N**2)


def predict(table, model):
    t = table.copy()
    tau, sigma, mean = (model[k] for k in ['school_variance','residual_variance','intercept'])
    t['reliability'] = tau/(tau+sigma/t.n)
    t['school_mean_prediction'] = mean+t.reliability*(t['mean']-mean)
    t['conditional_mean_variance'] = tau*(1-t.reliability)
    t['known_school_pupil_variance'] = sigma+t.conditional_mean_variance
    t['mean_halfwidth_95'] = 1.959963984540054*np.sqrt(t.conditional_mean_variance)
    t['pupil_halfwidth_95'] = 1.959963984540054*np.sqrt(t.known_school_pupil_variance)
    return t


def main():
    directory = Path(__file__).resolve().parent
    path = directory.parent/'kaynak/MathAchieve.csv'
    raw = path.read_bytes()
    assert hashlib.sha256(raw.rstrip(b'\n')+b'\n').hexdigest() == '087beeed36585553ec1b69dd5b29266a99e8189c565d51a301b99e53a2a0be72'
    table = summaries(pd.read_csv(path, dtype={'School':str}))
    model = reml(table)
    old = json.loads((directory.parent/'sonuclar/ozet.json').read_text())['null_model']
    reference = [old['fixed']['Intercept']['estimate'], old['random_effects']['variances']['Group'], old['random_effects']['residual_variance']]
    actual = [model[k] for k in ['intercept','school_variance','residual_variance']]
    np.testing.assert_allclose(actual, reference, rtol=2e-5, atol=2e-5)
    de = design_effect(table.n, model['school_variance'], model['residual_variance'])
    de['effective_n_for_student_mean'] = float(table.n.sum()/de['unequal_size'])
    predictions = predict(table, model)
    selected = table.reset_index().sort_values(['n','School']).iloc[[0,-1]].School.tolist()
    result = dict(students=int(table.n.sum()), schools=len(table), model=model,
        empirical_student_mean=float(np.average(table['mean'],weights=table.n)),
        empirical_equal_school_mean=float(table['mean'].mean()), design_effect=de,
        new_school=dict(center=model['intercept'], pupil_variance=model['school_variance']+model['residual_variance'],
                        mean_of_30_variance=model['school_variance']+model['residual_variance']/30),
        selected_schools=[dict(School=str(j),**predictions.loc[j].to_dict()) for j in selected],
        conditions='Normal random-intercept model; independent schools, noninformative cluster size; plug-in conditional intervals omit parameter-estimation uncertainty. No causal or national inference.')
    out = directory/'sonuclar'; out.mkdir(exist_ok=True)
    predictions.to_csv(out/'okul-tahminleri.csv',float_format='%.10g')
    (out/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
