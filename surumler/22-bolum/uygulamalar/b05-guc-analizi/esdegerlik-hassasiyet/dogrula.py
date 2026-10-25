import unittest
from scipy import stats
from analiz import tost_power, width_probability, minimum_count


class PlanningChecks(unittest.TestCase):
    def test_tost_symmetry_units_and_boundary(self):
        a = tost_power(30,effect=2.5)
        self.assertAlmostEqual(a,tost_power(30,effect=-2.5),places=8)
        self.assertAlmostEqual(a,tost_power(30,effect=25,sigma=100,delta=50),places=8)
        self.assertLessEqual(tost_power(30,effect=5),.05+1e-8)

    def test_more_information_and_larger_bounds(self):
        self.assertLess(tost_power(20),tost_power(40))
        self.assertLess(tost_power(30,delta=4),tost_power(30,delta=6))

    def test_width_cdf_and_units(self):
        n = 20
        df = 2*n-2
        h_at_sigma = stats.t.ppf(.975,df)*10*(2/n)**.5
        self.assertAlmostEqual(width_probability(n,h_at_sigma),stats.chi2.cdf(df,df))
        self.assertAlmostEqual(width_probability(n,2),width_probability(n,20,sigma=100))

    def test_integer_search(self):
        self.assertEqual(minimum_count(lambda n: n/100,target=.801),81)
        with self.assertRaises(ValueError):
            minimum_count(lambda n:.1,target=.8,maximum=20)

    def test_invalid_inputs(self):
        for operation in [lambda:tost_power(1),lambda:tost_power(10,sigma=0),
                          lambda:tost_power(10,delta=-1),lambda:width_probability(20,0)]:
            with self.assertRaises(ValueError):
                operation()


if __name__ == '__main__':
    unittest.main(verbosity=2)
