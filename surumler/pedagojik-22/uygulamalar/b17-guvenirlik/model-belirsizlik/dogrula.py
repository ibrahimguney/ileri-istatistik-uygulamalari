import unittest
import numpy as np
from analiz import alpha_cov,batch_alpha,paired_draws,score_model,examples


class Checks(unittest.TestCase):
    def test_covariance_alpha_reference(self):
        x=np.array([[1,2,4],[2,4,3],[5,6,5],[3,2,2]],float)
        expected=3/2*(1-x.var(axis=0,ddof=1).sum()/x.sum(axis=1).var(ddof=1))
        self.assertAlmostEqual(alpha_cov(np.cov(x,rowvar=False)),expected)
        self.assertAlmostEqual(batch_alpha(x[None])[0],expected)

    def test_paired_bootstrap_manual(self):
        rng=np.random.default_rng(81);A=rng.normal(size=(30,5));C=.6*A+rng.normal(size=(30,5))
        actual=paired_draws(A,C,seed=19,repeats=9)
        idx=np.random.default_rng(19).integers(0,30,size=(9,30))
        expected=[alpha_cov(np.cov(C[i],rowvar=False))-alpha_cov(np.cov(A[i],rowvar=False)) for i in idx]
        np.testing.assert_allclose(actual,expected,atol=1e-14)

    def test_identical_scales_zero_difference(self):
        A=np.random.default_rng(9).normal(size=(30,5))
        np.testing.assert_array_equal(paired_draws(A,A,repeats=501),np.zeros(501))

    def test_tau_equivalent_equality(self):
        d=examples()['tau_equivalent']
        self.assertAlmostEqual(d['alpha'],d['score_reliability'])
        self.assertAlmostEqual(d['score_reliability'],(5*.7)**2/((5*.7)**2+5*.51))

    def test_correlated_residual_counterexample(self):
        d=examples();self.assertLess(d['congeneric']['alpha'],d['congeneric']['score_reliability'])
        self.assertGreater(d['correlated_errors']['alpha'],d['correlated_errors']['score_reliability'])
        self.assertGreater(d['correlated_errors']['alpha'],d['congeneric']['alpha'])
        self.assertLess(d['correlated_errors']['score_reliability'],d['congeneric']['score_reliability'])

    def test_score_units_and_error_identity(self):
        lam=np.array([.8,.7,.6,.5,.4]);theta=np.diag(1-lam**2)
        original=score_model(lam,theta);scaled=score_model(lam,theta,np.full(5,10.))
        self.assertAlmostEqual(original['score_reliability'],scaled['score_reliability'])
        self.assertAlmostEqual(scaled['sem'],10*original['sem'])
        self.assertAlmostEqual(original['sem']**2,original['total_variance']*(1-original['score_reliability']))

    def test_invalid_inputs_and_negative_alpha(self):
        self.assertLess(alpha_cov(np.array([[1.,-.2],[-.2,1.]])),0)
        with self.assertRaises(ValueError):alpha_cov([[1,2],[2,1]])
        with self.assertRaises(ValueError):score_model([.5,.5],[[1,2],[2,1]])
        with self.assertRaises(ValueError):batch_alpha(np.ones((2,10,5)))
        with self.assertRaises(ValueError):paired_draws(np.ones((3,5)),np.ones((4,5)))


if __name__=='__main__':unittest.main(verbosity=2)
