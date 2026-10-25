import unittest
import numpy as np
from scipy import stats
from analiz import superiority,brunner_munzel,bootstrap,sign_and_median
class Tests(unittest.TestCase):
    def setUp(self):self.x=np.array([1.,2,2,4,7]);self.y=np.array([0.,1,3,3,4,6])
    def test_tied_u_matches_A(self):
        u=stats.mannwhitneyu(self.x,self.y,method='asymptotic').statistic
        self.assertAlmostEqual(superiority(self.x,self.y),u/(len(self.x)*len(self.y)))
    def test_group_swap(self):
        a=brunner_munzel(self.x,self.y);b=brunner_munzel(self.y,self.x)
        self.assertAlmostEqual(a['A'],1-b['A']);self.assertAlmostEqual(a['t_positive_for_x_superiority'],-b['t_positive_for_x_superiority']);self.assertAlmostEqual(a['p_two_sided'],b['p_two_sided'])
    def test_increasing_transform(self):
        a=bootstrap(self.x,self.y,repetitions=1000);b=bootstrap(np.exp(self.x),np.exp(self.y),repetitions=1000)
        self.assertEqual(a,b)
    def test_row_order_invariance(self):self.assertEqual(bootstrap(self.x,self.y,repetitions=1000),bootstrap(self.x[::-1],self.y[::-1],repetitions=1000))
    def test_BM_reference(self):
        r=brunner_munzel(self.x,self.y);t,p=stats.brunnermunzel(self.x,self.y,distribution='t')
        np.testing.assert_allclose([-r['t_positive_for_x_superiority'],r['p_two_sided']],[t,p])
    def test_sign_zeros_and_median(self):
        d=np.array([0,.8,1,1.2,1.3,1.3,1.4,1.8,2.4,4.6]);r=sign_and_median(d)
        self.assertEqual((r['n_pairs'],r['n_signs'],r['n_zero']),(10,9,1));self.assertEqual(r['sign_p'],2/512);self.assertEqual(r['median_interval'],[.8,2.4]);self.assertEqual(r['continuous_model_coverage'],1-2*stats.binom.cdf(1,10,.5))
    def test_degenerate_and_missing_rejected(self):
        with self.assertRaises(ValueError):brunner_munzel([1,1],[1,1])
        with self.assertRaises(ValueError):superiority([np.nan,1],self.y)
        with self.assertRaises(ValueError):sign_and_median([0,0,0,0,0,0])
if __name__=='__main__':unittest.main()
