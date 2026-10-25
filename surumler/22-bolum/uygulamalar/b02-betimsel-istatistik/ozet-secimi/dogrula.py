import unittest
import numpy as np
from analiz import trimmed_mean, ecdf


class SummaryChecks(unittest.TestCase):
    def test_trimmed_hand_example_and_affine_transform(self):
        y = np.array([0., 2., 3., 4., 100.])
        self.assertEqual(trimmed_mean(y), 3)
        self.assertEqual(trimmed_mean(y[::-1]), 3)
        self.assertEqual(trimmed_mean(5*y+7), 22)

    def test_ecdf_ties_and_strict_inequality(self):
        y = [1, 2, 2, 5]
        self.assertEqual(ecdf(y, 2), .75)
        self.assertEqual(1-ecdf(y, 2), .25)
        self.assertEqual(sum(v>=2 for v in y)/4, .75)
        self.assertEqual(ecdf(y, 0), 0)
        self.assertEqual(ecdf(y, 5), 1)

    def test_invalid_inputs(self):
        for y,p in [([], .2), ([1, np.nan], .2), ([1, 2], .5)]:
            with self.assertRaises(ValueError):
                trimmed_mean(y,p)


if __name__ == '__main__':
    unittest.main(verbosity=2)
