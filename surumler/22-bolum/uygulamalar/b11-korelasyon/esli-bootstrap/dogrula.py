import unittest
import numpy as np
from scipy import stats
from analiz import coefficients,paired_bootstrap
class Tests(unittest.TestCase):
    def setUp(self):self.p=np.array([[1,2],[1,3],[2,1],[2,2],[3,4],[3,4],[4,3],[4,6],[5,5],[6,7]],float)
    def test_scipy_coefficients(self):np.testing.assert_allclose(coefficients(self.p)[:2],[stats.pearsonr(*self.p.T).statistic,stats.spearmanr(*self.p.T).statistic])
    def test_affine_and_sign(self):
        q=self.p*np.array([-2,3])+[10,20];np.testing.assert_allclose(coefficients(q),-coefficients(self.p))
    def test_monotone_ranks(self):
        q=self.p.copy();q[:,0]=q[:,0]**2;self.assertAlmostEqual(coefficients(q)[1],coefficients(self.p)[1]);self.assertNotAlmostEqual(coefficients(q)[0],coefficients(self.p)[0])
    def test_row_order_and_reproducibility(self):self.assertEqual(paired_bootstrap(self.p,1000),paired_bootstrap(self.p[::-1],1000))
    def test_same_coefficient_zero_difference(self):
        q=np.column_stack([np.arange(20),np.arange(20)])
        r=paired_bootstrap(q,1000);np.testing.assert_allclose(r['intervals'][2]['interval_percentile_95'],[0,0],atol=1e-14)
    def test_invalid_and_degenerate_rejected(self):
        with self.assertRaises(ValueError):coefficients([[1,1],[1,2],[1,3],[1,4]])
        q=self.p.copy();q[0,0]=np.nan
        with self.assertRaises(ValueError):paired_bootstrap(q,1000)
        with self.assertRaises(ValueError):paired_bootstrap([[0,0],[0,0],[0,0],[1,1]],1000)
    def test_correlation_not_agreement(self):
        x=np.arange(10);self.assertAlmostEqual(stats.pearsonr(x,x+5).statistic,1);self.assertEqual(np.mean((x+5)-x),5)
if __name__=='__main__':unittest.main()
