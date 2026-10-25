import unittest
import numpy as np
from analiz import tost, holm_adjust


class DecisionChecks(unittest.TestCase):
    def test_tost_interval_inversion(self):
        for n in [4,10,25]:
            for mean in [-6,-2,0,2,6]:
                r = tost(n,mean,3,2)
                low,high = r['CI_1_minus_2alpha']
                self.assertEqual(r['equivalent_under_model'], low>-2 and high<2)

    def test_null_boundary_not_equivalent(self):
        r = tost(25,2,1,2)
        self.assertAlmostEqual(r['p_upper'],.5)
        self.assertFalse(r['equivalent_under_model'])

    def test_units_and_direction(self):
        a,b,c = tost(10,1.58,1.23,3),tost(10,158,123,300),tost(10,-1.58,1.23,3)
        self.assertAlmostEqual(a['p_tost'],b['p_tost'])
        self.assertAlmostEqual(a['p_tost'],c['p_tost'])
        np.testing.assert_allclose(b['CI_1_minus_2alpha'],100*np.array(a['CI_1_minus_2alpha']))

    def test_holm_hand_calculation_and_order(self):
        p = np.array([.20,.004,.024,.012])
        np.testing.assert_allclose(holm_adjust(p),[.20,.016,.048,.036])
        np.testing.assert_allclose(holm_adjust(p[::-1]),holm_adjust(p)[::-1])
        np.testing.assert_allclose(holm_adjust([.8,.9]),[1,1])

    def test_invalid_inputs(self):
        for args in [(1,0,1,1),(10,0,0,1),(10,0,1,-1),(10,0,1,1,.8)]:
            with self.assertRaises(ValueError):
                tost(*args)
        for p in [[],[-.1],[np.nan],[1.1]]:
            with self.assertRaises(ValueError):
                holm_adjust(p)


if __name__ == '__main__':
    unittest.main(verbosity=2)
