import unittest
import numpy as np
import pandas as pd
from analiz import mask_followup, validate_panel


def toy_panel():
    return pd.DataFrame([{'Subject':i,'Days':d+2,'DaysB':d,'Reaction':250.+i+d} for i in range(1,6) for d in range(8)])


class FollowupChecks(unittest.TestCase):
    def test_reproducibility_and_order(self):
        source = toy_panel()
        a,mask = mask_followup(source)
        b,other = mask_followup(source.sample(frac=1,random_state=21))
        pd.testing.assert_frame_equal(a.reset_index(drop=True),b.reset_index(drop=True))
        pd.testing.assert_frame_equal(mask,other)
        self.assertFalse(source.Reaction.isna().any())

    def test_baseline_and_monotone_dropout(self):
        masked,mask = mask_followup(toy_panel())
        self.assertTrue(masked.loc[masked.DaysB.lt(2),'Reaction'].notna().all())
        for _,g in mask.groupby('Subject'):
            self.assertTrue(np.all(np.diff(g.masked.astype(int))>=0))

    def test_observed_values_unchanged(self):
        original = toy_panel()
        masked,_ = mask_followup(original)
        valid = masked.Reaction.notna()
        np.testing.assert_array_equal(masked.loc[valid,'Reaction'],original.loc[valid,'Reaction'])

    def test_invalid_keys(self):
        f = toy_panel()
        for bad in [pd.concat([f,f.iloc[[0]]]),f.assign(Subject=np.nan)]:
            with self.assertRaises(ValueError):
                validate_panel(bad)

    def test_baseline_must_be_observed(self):
        f = toy_panel();f.loc[0,'Reaction']=np.nan
        with self.assertRaises(ValueError):
            mask_followup(f)


if __name__=='__main__':
    unittest.main(verbosity=2)
