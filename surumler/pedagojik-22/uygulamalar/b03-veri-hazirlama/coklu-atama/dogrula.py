"""Çoklu atama öğretim paketinin bağımsız sayısal ve girdi kontrolleri."""
import unittest
import numpy as np
from analiz import pool_estimates, impute_regression, generate_example


class MissingDataChecks(unittest.TestCase):
    def test_hand_worked_rubin_example(self):
        # Q=(10,12), U=(4,4): Qbar=11, B=2, T=4+1.5*2=7.
        result = pool_estimates([10, 12], [4, 4], 239)
        self.assertAlmostEqual(result['estimate'], 11)
        self.assertAlmostEqual(result['between'], 2)
        self.assertAlmostEqual(result['total'], 7)
        self.assertAlmostEqual(result['se'], np.sqrt(7))

    def test_degrees_of_freedom_against_mice_form(self):
        # MICE'nin yayımladığı alternatif cebirsel biçim; sıfır B sınırı hariç.
        # https://github.com/amices/mice/blob/master/R/barnard.rubin.R
        for ndf in [9, 39, 239]:
            result = pool_estimates([9, 11, 10, 12], [2, 3, 2, 3], ndf)
            m, b, total = result['m'], result['between'], result['total']
            lam = (1 + 1 / m) * b / total
            tmp = (1 - lam) * (1 + ndf) * ndf
            reference_df = (m - 1) * tmp / ((ndf + 3) * (m - 1) + lam ** 2 * tmp)
            self.assertAlmostEqual(result['df'], reference_df, places=11)

    def test_no_between_variance_limit(self):
        result = pool_estimates([5, 5, 5], [4, 4, 4], 39)
        self.assertEqual(result['between'], 0)
        self.assertEqual(result['total'], 4)
        self.assertEqual(result['df'], 39)

    def test_bad_imputations_are_not_silently_removed(self):
        for q, u in [([1, np.nan], [1, 1]), ([1, 2], [1, -1]), ([1], [1])]:
            with self.assertRaises(ValueError):
                pool_estimates(q, u, 239)

    def test_observed_values_and_reproducibility(self):
        observed, full = generate_example()
        seen = observed.y.notna().to_numpy()
        first, draws, _ = impute_regression(observed, m=20)
        second, _, _ = impute_regression(observed, m=20)
        np.testing.assert_array_equal(first, second)
        np.testing.assert_array_equal(first[:, seen], np.broadcast_to(observed.y[seen], (20, seen.sum())))
        self.assertTrue(np.isfinite(first).all())
        self.assertEqual(len(draws), 20)
        self.assertGreater(np.std([r['sigma2'] for r in draws]), 0)
        self.assertGreater(np.std([r['beta1'] for r in draws]), 0)
        np.testing.assert_array_equal(observed.y[seen], full.y_full[seen])


if __name__ == '__main__':
    unittest.main(verbosity=2)
