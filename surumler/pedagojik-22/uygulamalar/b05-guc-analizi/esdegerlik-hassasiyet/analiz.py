"""Normal/eşit varyanslı iki bağımsız grup: TOST gücü ve aralık genişliği."""
import importlib.util
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import integrate, stats

SEED = 20261025
REPETITIONS = 100000


def validate(n, sigma, alpha):
    if (not isinstance(n, (int,np.integer)) or n < 2 or
        not np.isfinite([sigma,alpha]).all() or sigma <= 0 or not 0 < alpha < .5):
        raise ValueError('n>=2 tamsayı, pozitif sigma ve 0<alfa<.5 gerekir')


def tost_power(n, delta=5., sigma=10., effect=0., alpha=.05):
    validate(n,sigma,alpha)
    if not np.isfinite([delta,effect]).all() or delta <= 0:
        raise ValueError('Pozitif sınır ve sonlu gerçek fark gerekir')
    df = 2*n-2
    se = sigma*np.sqrt(2/n)
    critical = stats.t.ppf(1-alpha,df)
    cap = stats.chi2.cdf(df*(delta/(critical*se))**2,df)

    def conditional(u):
        h = critical*se*np.sqrt(stats.chi2.ppf(u,df)/df)
        if h >= delta:
            return 0.
        return max(0.,float(stats.norm.cdf((delta-h-effect)/se)-stats.norm.cdf((-delta+h-effect)/se)))

    value,error = integrate.quad(conditional,0,float(cap),epsabs=1e-9,epsrel=1e-8,limit=200)
    assert error < 1e-7 and -.0000001 <= value <= 1.0000001
    return float(value)


def width_probability(n, half_width=2., sigma=10., alpha=.05):
    validate(n,sigma,alpha)
    if not np.isfinite(half_width) or half_width <= 0:
        raise ValueError('Pozitif sonlu yarı genişlik gerekir')
    df = 2*n-2
    threshold = df*(half_width/(stats.t.ppf(1-alpha/2,df)*sigma*np.sqrt(2/n)))**2
    return float(stats.chi2.cdf(threshold,df))


def minimum_count(function,target=.8,maximum=10000):
    if not np.isfinite(target) or not 0 < target < 1:
        raise ValueError('Hedef (0,1) arasında olmalı')
    high = 2
    while function(high) < target and high < maximum:
        high = min(2*high,maximum)
    if function(high) < target:
        raise ValueError('Belirlenen üst sınırda hedefe ulaşılamadı')
    low = 2
    while low < high:
        mid = (low+high)//2
        if function(mid) >= target:
            high = mid
        else:
            low = mid+1
    assert function(low) >= target
    assert low == 2 or function(low-1) < target
    return low


def main():
    directory = Path(__file__).parent
    spec = importlib.util.spec_from_file_location('b05_original',directory.parent/'analiz.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    equivalence = []
    for effect in [0.,2.5]:
        function = lambda n: tost_power(n,effect=effect)
        n = minimum_count(function)
        equivalence.append({'true_difference':effect,'delta':5.,'sigma':10.,'alpha':.05,'target_power':.8,
                            'n_per_group':n,'total':2*n,'previous_power':function(n-1),'power':function(n)})
    n_width = minimum_count(width_probability,target=.9)
    width = {'half_width_target':2.,'sigma':10.,'CI_level':.95,'target_probability':.9,
             'n_per_group':n_width,'total':2*n_width,'previous_probability':width_probability(n_width-1),
             'probability':width_probability(n_width),'probability_at_plugin_n194':width_probability(194)}
    rng = np.random.default_rng(SEED)
    checks = []
    for effect in [0.,2.5]:
        n = 64
        df = 2*n-2
        se = 10*np.sqrt(2/n)
        means = rng.normal(effect,se,REPETITIONS)
        scale = np.sqrt(rng.chisquare(df,REPETITIONS)/df)
        h = stats.t.ppf(.95,df)*se*scale
        rate = float(np.mean((means-h>-5)&(means+h<5)))
        exact = tost_power(n,effect=effect)
        mcse = float(np.sqrt(exact*(1-exact)/REPETITIONS))
        assert abs(rate-exact)<5*mcse
        checks.append({'n_per_group':n,'true_difference':effect,'integral_power':exact,
                       'MC_power':rate,'MC_SE':mcse})
    df = 2*n_width-2
    random_h = stats.t.ppf(.975,df)*10*np.sqrt(2/n_width)*np.sqrt(rng.chisquare(df,REPETITIONS)/df)
    rate = float(np.mean(random_h<=2))
    assert abs(rate-width['probability'])<5*np.sqrt(width['probability']*(1-width['probability'])/REPETITIONS)
    width['MC_probability'] = rate
    result = {'scope':'Varsayımsal bağımsız normal eşit varyanslı gruplar; klinik/pilot veri yok',
              'equivalence_plans':equivalence,'width_plan':width,
              'comparison_n64':{'difference_power_true_delta5':float(module.power_t(64,effect=.5)),
                                'TOST_power_true_delta0':tost_power(64,effect=0),
                                'TOST_power_true_delta2_5':tost_power(64,effect=2.5)},
              'simulation_checks':checks,'seed':SEED,'repetitions':REPETITIONS,
              'simulation_unit':'Normal ortalama farkı ve bağımsız ki-kare pooled varyans; yeni kişi verisi üretilmez',
              'uncertain_sigma_integrated':False,'loss_model_integrated':False,
              'versions':{'numpy':np.__version__,'pandas':pd.__version__}}
    output = directory/'sonuclar'
    output.mkdir(exist_ok=True)
    pd.DataFrame(equivalence).to_csv(output/'esdegerlik-planlari.csv',index=False)
    pd.DataFrame([width]).to_csv(output/'genislik-plani.csv',index=False)
    pd.DataFrame(checks).to_csv(output/'MC-denetimi.csv',index=False)
    (output/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
