import unittest
import numpy as np
from scipy import stats
from analiz import compare_groups
class Tests(unittest.TestCase):
    def setUp(self):
        rng=np.random.default_rng(20261025)
        self.a=rng.normal(size=(19,2))@np.array([[1.,.4],[0.,1.3]])+[.4,-.2]
        self.b=rng.normal(size=(31,2))@np.array([[1.4,-.2],[0.,.8]])
    def test_univariate_student_reduction(self):
        r=compare_groups(self.a[:,:1],self.b[:,:1]);t=stats.ttest_ind(self.a[:,0],self.b[:,0],equal_var=True)
        np.testing.assert_allclose(r['pooled_T2'],t.statistic**2)
        np.testing.assert_allclose(r['pooled_p'],t.pvalue)
    def test_affine_invariance(self):
        r=compare_groups(self.a,self.b);m=np.array([[2.,-.3],[1.,4.]])
        q=compare_groups(self.a@m+17,self.b@m+17)
        for k in ['pooled_T2','pooled_p','unpooled_Wald_chi2']:np.testing.assert_allclose(r[k],q[k],rtol=1e-10)
    def test_swap_sign_intervals(self):
        r=compare_groups(self.a,self.b);q=compare_groups(self.b,self.a)
        np.testing.assert_allclose(r['pooled_T2'],q['pooled_T2'])
        for x,y in zip(r['intervals'],q['intervals']):
            for k in ['marginal','bonferroni_family','hotelling_all_directions']:np.testing.assert_allclose(x[k],-np.array(y[k])[::-1])
    def test_singular_and_missing_rejected(self):
        with self.assertRaises(ValueError):compare_groups(np.repeat(self.a[:,:1],2,axis=1),np.repeat(self.b[:,:1],2,axis=1))
        a=self.a.copy();a[0,0]=np.nan
        with self.assertRaises(ValueError):compare_groups(a,self.b)
    def test_intervals_nest(self):
        for row in compare_groups(self.a,self.b)['intervals']:
            for key in ['bonferroni_family','hotelling_all_directions']:
                self.assertLess(row[key][0],row['marginal'][0]);self.assertGreater(row[key][1],row['marginal'][1])
    def test_unpooled_wald_reduction(self):
        r=compare_groups(self.a[:,:1],self.b[:,:1]);t=stats.ttest_ind(self.a[:,0],self.b[:,0],equal_var=False)
        np.testing.assert_allclose(r['unpooled_Wald_chi2'],t.statistic**2)
        np.testing.assert_allclose(r['unpooled_asymptotic_p'],stats.chi2.sf(t.statistic**2,1))
        # Aynı istatistik karesi; Welch sd ile t p'si olduğu iddia edilmez.
if __name__=='__main__':unittest.main()
