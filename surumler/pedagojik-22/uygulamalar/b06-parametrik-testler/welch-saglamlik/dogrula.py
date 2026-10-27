import unittest
import numpy as np
from scipy import stats
from analiz import yuen


class RobustChecks(unittest.TestCase):
    def test_trimmed_hand_example(self):
        a = np.array([0.,1.,2.,3.,100.])
        r = yuen(a,a+5)
        self.assertEqual(r['groups'][0]['g'],1)
        self.assertEqual(r['groups'][0]['h'],3)
        self.assertAlmostEqual(r['groups'][0]['winsor_SS'],4)
        self.assertAlmostEqual(r['estimate'],-5)
        self.assertAlmostEqual(r['df'],4)

    def test_zero_trim_reduces_to_welch(self):
        a,b = [1,2,4,9,12],[0,1,3,4,8,9]
        r = yuen(a,b,trim=0)
        direct = stats.ttest_ind(a,b,equal_var=False)
        self.assertAlmostEqual(r['t'],direct.statistic)
        self.assertAlmostEqual(r['df'],direct.df)

    def test_location_scale_and_direction(self):
        a = np.array([0.,1.,2.,3.,100.]);b=a+5
        r,s,rev = yuen(a,b),yuen(3*a+7,3*b+7),yuen(b,a)
        self.assertAlmostEqual(s['estimate'],3*r['estimate'])
        self.assertAlmostEqual(s['p'],r['p'])
        np.testing.assert_allclose(s['CI95'],3*np.array(r['CI95']))
        self.assertAlmostEqual(rev['p'],r['p'])
        np.testing.assert_allclose(rev['CI95'],-np.array(r['CI95'])[::-1])

    def test_equal_n_standard_errors_identity(self):
        a,b = np.array([1.,2.,6.,9.]),np.array([0.,1.,2.,3.])
        se_w = np.sqrt(a.var(ddof=1)/4+b.var(ddof=1)/4)
        pooled = ((3*a.var(ddof=1)+3*b.var(ddof=1))/6)**.5
        self.assertAlmostEqual(se_w,pooled*(1/4+1/4)**.5)
        self.assertAlmostEqual(stats.ttest_ind(a,b,equal_var=True).statistic,stats.ttest_ind(a,b,equal_var=False).statistic)

    def test_invalid_inputs(self):
        for a,b,trim in [([], [1,2],.2),([1,np.nan],[1,2],.2),([1,2],[2,3],.5),([1,1],[2,2],.2)]:
            with self.assertRaises(ValueError):
                yuen(a,b,trim)


if __name__=='__main__':
    unittest.main(verbosity=2)
