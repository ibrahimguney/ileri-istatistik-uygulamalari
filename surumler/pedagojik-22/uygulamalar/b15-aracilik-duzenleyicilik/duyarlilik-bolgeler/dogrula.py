import unittest
import numpy as np
from scipy import stats
from analiz import sensitivity,band,roots
class Tests(unittest.TestCase):
    def setUp(self):self.beta=np.array([.4,.56]);self.cov=np.array([[.006,-.0005],[-.0005,.005]]);self.t=stats.t.ppf(.975,156)
    def test_zero_rho(self):self.assertAlmostEqual(float(sensitivity(.6,.7,1.,0)),.42)
    def test_zero_crossing(self):
        rho=.7/np.sqrt(.7**2+1);self.assertAlmostEqual(float(sensitivity(.6,.7,1.,rho)),0)
    def test_invalid_rho(self):
        for rho in [-1,1,np.nan]:
            with self.assertRaises(ValueError):sensitivity(.6,.7,1.,rho)
    def test_roots_are_interval_boundaries(self):
        for root in roots(self.beta,self.cov,self.t):self.assertLess(min(abs(band(self.beta,self.cov,root,self.t))),1e-12)
    def test_simultaneous_contains_pointwise(self):
        w=np.linspace(-3,3,100);p=band(self.beta,self.cov,w,self.t);j=band(self.beta,self.cov,w,np.sqrt(2*stats.f.ppf(.95,2,156)))
        self.assertTrue(np.all(j[:,0]<p[:,0]));self.assertTrue(np.all(j[:,1]>p[:,1]))
    def test_recentering_invariance(self):
        shift=.8;T=np.array([[1,shift],[0,1.]])
        w=np.array([-2.,0,1.]);np.testing.assert_allclose(band(self.beta,self.cov,w,self.t),band(T@self.beta,T@self.cov@T.T,w-shift,self.t),atol=1e-12)
    def test_regions_agree_with_direct_t(self):
        w=np.linspace(-2,2,100);r=roots(self.beta,self.cov,self.t);ci=band(self.beta,self.cov,w,self.t)
        direct=(ci[:,0]>0)|(ci[:,1]<0);self.assertTrue(np.array_equal(direct,(w<r[0])|(w>r[1])))
if __name__=='__main__':unittest.main()
