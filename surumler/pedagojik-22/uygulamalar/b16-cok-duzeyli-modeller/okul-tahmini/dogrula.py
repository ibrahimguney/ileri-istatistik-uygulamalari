"""Yedi bağımsız sayısal/cebirsel denetim; Python unittest."""
import unittest
import numpy as np
import pandas as pd
from scipy.linalg import block_diag
from scipy.optimize import minimize
from analiz import summaries, reml, design_effect, predict


class Checks(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({'School':['a']*3+['b']*4+['c']*2,
                                  'MathAch':[0.,1.,2.,7.,8.,9.,10.,3.,5.]})
        self.table = summaries(self.data)
        self.model = reml(self.table)

    def test_dense_reml_reference(self):
        y = self.data.MathAch.to_numpy(); n = len(y); one = np.ones(n)
        def objective(logvars):
            tau, sigma = np.exp(logvars)
            V = block_diag(*[sigma*np.eye(k)+tau*np.ones((k,k)) for k in [3,4,2]])
            vi = np.linalg.solve(V,one); mean = vi@y/vi.sum()
            e = y-mean
            return .5*(np.linalg.slogdet(V)[1]+np.log(vi.sum())+e@np.linalg.solve(V,e))
        result = minimize(objective,np.log([10.,2.]),method='Nelder-Mead',
                          options={'xatol':1e-10,'fatol':1e-10})
        self.assertTrue(result.success)
        np.testing.assert_allclose(np.exp(result.x),[self.model['school_variance'],self.model['residual_variance']],rtol=2e-6)

    def test_equal_cluster_reduction(self):
        d = design_effect([20]*8,2.,8.)
        self.assertAlmostEqual(d['unequal_size'],d['equal_size_approx'])

    def test_block_covariance_mean(self):
        n = [2,4,9]; tau,sigma = 3.,7.
        V = block_diag(*[sigma*np.eye(k)+tau*np.ones((k,k)) for k in n])
        d = design_effect(n,tau,sigma)
        self.assertAlmostEqual(V.sum()/sum(n)**2,d['mean_variance'])
        self.assertGreater(d['unequal_size'],d['equal_size_approx'])

    def test_normal_conditioning_reference(self):
        t = predict(self.table,self.model); tau=self.model['school_variance']; sigma=self.model['residual_variance']
        for school,row in t.iterrows():
            y = self.data.loc[self.data.School==school,'MathAch'].to_numpy()
            V = sigma*np.eye(len(y))+tau*np.ones((len(y),len(y)))
            cross = np.full(len(y),tau)
            expected = self.model['intercept']+cross@np.linalg.solve(V,y-self.model['intercept'])
            var = tau-cross@np.linalg.solve(V,cross)
            self.assertAlmostEqual(expected,row.school_mean_prediction)
            self.assertAlmostEqual(var,row.conditional_mean_variance)

    def test_prediction_targets(self):
        t = predict(self.table,self.model).sort_values('n')
        self.assertTrue(np.all(np.diff(t.reliability)>0))
        self.assertTrue(np.all(t.known_school_pupil_variance>t.conditional_mean_variance))
        self.assertTrue(np.all(t.known_school_pupil_variance<self.model['school_variance']+self.model['residual_variance']))

    def test_permutation_invariance(self):
        other = reml(summaries(self.data.sample(frac=1,random_state=42)))
        np.testing.assert_allclose(list(other.values()),list(self.model.values()),rtol=1e-7)

    def test_boundary_and_invalid_data(self):
        model=dict(intercept=4.,school_variance=0.,residual_variance=2.)
        t=predict(self.table,model)
        np.testing.assert_allclose(t.school_mean_prediction,4.)
        np.testing.assert_allclose(t.conditional_mean_variance,0.)
        self.assertEqual(design_effect([2,9],0.,2.)['unequal_size'],1.)
        bad=self.data.copy();bad.loc[0,'School']=None
        with self.assertRaises(ValueError):summaries(bad)
        with self.assertRaises(ValueError):design_effect([0,2],1.,2.)
        with self.assertRaises(ValueError):design_effect([2,2],-1.,2.)


if __name__=='__main__':
    unittest.main(verbosity=2)
