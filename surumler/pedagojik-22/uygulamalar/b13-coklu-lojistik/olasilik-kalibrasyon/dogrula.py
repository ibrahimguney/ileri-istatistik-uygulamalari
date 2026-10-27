import unittest
import numpy as np
from scipy.special import expit
from analiz import metrics,profile,difference
class Tests(unittest.TestCase):
    def setUp(self):
        self.beta=np.array([-2.,.3,.1]);self.cov=np.array([[.4,-.01,0],[-.01,.02,.001],[0,.001,.03]])
    def test_monotone_auc_same_calibration_changes(self):
        y=np.array([0,0,1,0,1,1]);eta=np.array([-2,-1,-.5,.2,1,2]);a=metrics(y,eta);b=metrics(y,2*eta)
        self.assertEqual(a['AUC'],b['AUC']);self.assertEqual(a['accuracy_at_half'],b['accuracy_at_half']);self.assertNotAlmostEqual(a['Brier'],b['Brier'])
    def test_stable_logloss(self):
        r=metrics([0,1],[-1000,1000]);self.assertTrue(np.isfinite(r['log_loss']));self.assertLess(r['log_loss'],1e-10)
    def test_profile_covariance(self):
        x=np.array([1,12,0]);r=profile(self.beta,self.cov,x);self.assertAlmostEqual(r['eta_SE']**2,x@self.cov@x);self.assertLess(r['probability_CI_95'][0],r['p']);self.assertGreater(r['probability_CI_95'][1],r['p'])
    def test_delta_gradient_numeric(self):
        a=np.array([1,12,0]);b=np.array([1,13,0]);r=difference(self.beta,self.cov,a,b);grad=[]
        for j in range(3):
            e=np.eye(3)[j]*1e-5
            grad.append(((expit(b@(self.beta+e))-expit(a@(self.beta+e)))-(expit(b@(self.beta-e))-expit(a@(self.beta-e))))/(2e-5))
        np.testing.assert_allclose(r['gradient'],grad,rtol=1e-7,atol=1e-8)
    def test_difference_reversal(self):
        a=[1,12,0];b=[1,13,0];r=difference(self.beta,self.cov,a,b);q=difference(self.beta,self.cov,b,a)
        self.assertAlmostEqual(r['probability_difference'],-q['probability_difference']);np.testing.assert_allclose(r['delta_Wald_CI_95'],-np.array(q['delta_Wald_CI_95'])[::-1])
    def test_shared_profile_zero_difference(self):
        r=difference(self.beta,self.cov,[1,12,0],[1,12,0]);self.assertEqual(r['delta_SE'],0);self.assertEqual(r['probability_difference'],0)
    def test_invalid_metrics(self):
        with self.assertRaises(ValueError):metrics([1,1],[0,1])
        with self.assertRaises(ValueError):metrics([0,1],[0,np.nan])
if __name__=='__main__':unittest.main()
