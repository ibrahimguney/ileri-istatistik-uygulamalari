"""Varyans formülünü küçük anakütlede tüm örnekleri sayarak denetle."""
import itertools
import unittest
import numpy as np
from analiz import exact_srs_variance, systematic_means


class DesignChecks(unittest.TestCase):
    def test_srs_formula_against_enumeration(self):
        y = np.array([0., 1., 4., 9., 12.])
        for n in range(1, len(y) + 1):
            means = np.array([np.mean(s) for s in itertools.combinations(y, n)])
            self.assertAlmostEqual(means.mean(), y.mean())
            self.assertAlmostEqual(means.var(ddof=0), exact_srs_variance(y, n))

    def test_systematic_expectation_and_order(self):
        y = np.array([1., 0., 0., 0.] * 3)
        means = systematic_means(y, 4)
        self.assertAlmostEqual(means.mean(), y.mean())
        self.assertAlmostEqual(means.var(ddof=0), .1875)
        self.assertFalse(np.allclose(means, systematic_means(np.sort(y), 4)))

    def test_invalid_sample_size(self):
        with self.assertRaises(ValueError):
            exact_srs_variance([1., 2.], 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
