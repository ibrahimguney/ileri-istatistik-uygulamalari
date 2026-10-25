import unittest
import numpy as np
import pandas as pd
from analiz import checked_join, fit_center


class PreparationChecks(unittest.TestCase):
    def test_cardinality_and_row_order(self):
        a = pd.DataFrame({'id':[2,1], 'A':[20,10]})
        c = pd.DataFrame({'id':[3,2], 'C':[30,20]})
        self.assertEqual(len(checked_join(a,c,'id','inner')),1)
        self.assertEqual(len(checked_join(a,c,'id','left')),2)
        self.assertEqual(len(checked_join(a,c,'id','outer')),3)
        r = checked_join(a,c,'id','inner')
        self.assertEqual((r.iloc[0].A,r.iloc[0].C),(20,20))

    def test_reject_duplicate_null_and_empty_keys(self):
        good = pd.DataFrame({'id':[1,2], 'A':[10,20]})
        for keys in [[1,1],[1,None],['','2']]:
            bad = pd.DataFrame({'id':keys,'C':[10,20]})
            with self.assertRaises(ValueError):
                checked_join(good,bad,'id','left')

    def test_no_silent_key_type_conversion(self):
        with self.assertRaises(ValueError):
            checked_join(pd.DataFrame({'id':[1]}),pd.DataFrame({'id':['01']}),'id','inner')

    def test_test_values_do_not_change_training_center(self):
        train = np.array([0.,2.])
        for test in [np.array([100.,102.]),np.array([-1e5,1e5])]:
            self.assertEqual(fit_center(train),1)
            np.testing.assert_array_equal(train-fit_center(train),[-1,1])
        self.assertNotEqual(fit_center(np.r_[train,[100,102]]),fit_center(train))

    def test_invalid_training_data(self):
        for y in [[],[1,np.nan]]:
            with self.assertRaises(ValueError):
                fit_center(y)


if __name__ == '__main__':
    unittest.main(verbosity=2)
