import unittest
import numpy as np
import pandas as pd
from analiz import BASE,fit_all,standardize,weights
class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=pd.read_csv(BASE.parent/'b06-parametrik-testler/kaynak/ToothGrowth.csv');cls.models=fit_all(cls.data)
    def test_balanced_raw_difference(self):
        m,c=self.models['cells'];r=standardize(m,m.cov_params(),[1/3]*3,'cells')
        self.assertAlmostEqual(r['difference'],self.data.loc[self.data.supp=='OJ','len'].mean()-self.data.loc[self.data.supp=='VC','len'].mean())
    def test_point_mass_matches_cell(self):
        m,c=self.models['cells'];r=standardize(m,m.cov_params(),[0,1,0],'cells')
        self.assertAlmostEqual(r['difference'],5.93);self.assertAlmostEqual(r['SE']**2,2*m.mse_resid/10)
    def test_invalid_weights(self):
        for w in [[1,1,1],[-.1,.5,.6],[np.nan,.5,.5],[.5,.5]]:
            with self.assertRaises(ValueError):weights(w)
    def test_row_order(self):
        reordered=fit_all(self.data.iloc[::-1]);w=[.1,.1,.8]
        for name,(m,c) in self.models.items():
            a=standardize(m,m.cov_params(),w,name);q,_=reordered[name];b=standardize(q,q.cov_params(),w,name)
            np.testing.assert_allclose([a['difference'],a['SE']],[b['difference'],b['SE']],atol=1e-12)
    def test_group_reverse(self):
        swapped=self.data.assign(supp=self.data.supp.map({'OJ':'VC','VC':'OJ'}));m,_=fit_all(swapped)['cells'];q,_=self.models['cells']
        a=standardize(m,m.cov_params(),[.6,.3,.1],'cells');b=standardize(q,q.cov_params(),[.6,.3,.1],'cells')
        np.testing.assert_allclose(a['bonferroni_family_CI_95'],-np.array(b['bonferroni_family_CI_95'])[::-1],atol=1e-12)
    def test_missing_support_rejected(self):
        with self.assertRaises(ValueError):fit_all(self.data.loc[~((self.data.supp=='OJ')&(self.data.dose==2))])
    def test_linear_average_equals_at_mean(self):
        w=np.array([.1,.1,.8]);dose=float(w@np.array([.5,1,2]));m,_=self.models['interaction'];r=standardize(m,m.cov_params(),w,'interaction')
        self.assertAlmostEqual(r['difference'],m.params[1]+m.params[3]*(dose-1))
        a,_=self.models['additive'];self.assertAlmostEqual(standardize(a,a.cov_params(),w,'additive')['difference'],3.7)
if __name__=='__main__':unittest.main()
