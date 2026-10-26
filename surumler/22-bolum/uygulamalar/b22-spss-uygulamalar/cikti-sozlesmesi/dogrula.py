import unittest
from pathlib import Path
from copy import deepcopy
from analiz import expected,compare,FIELDS

class Checks(unittest.TestCase):
    def setUp(self):self.reference=expected(Path(__file__).resolve().parents[1])
    def test_rounded_rows(self):
        rows=[{k:(r[k] if k=='model' else f'{r[k]:.3f}') for k in FIELDS} for r in self.reference]
        self.assertEqual(compare(self.reference,rows),[])
    def test_direction_rejected(self):
        rows=deepcopy(self.reference);rows[0]['difference']*=-1;self.assertTrue(compare(self.reference,rows))
    def test_wrong_model_row_rejected(self):
        rows=deepcopy(self.reference);rows[1]['df']=18.;self.assertTrue(compare(self.reference,rows))
    def test_p_zero_rejected(self):
        rows=deepcopy(self.reference);rows[0]['p']=0;self.assertTrue(compare(self.reference,rows))
    def test_upper_bound(self):
        rows=deepcopy(self.reference);rows[0]['p']='<0.01';self.assertEqual(compare(self.reference,rows),[])
        rows[0]['p']='<0.001';self.assertTrue(compare(self.reference,rows))
    def test_duplicate_rows(self):
        with self.assertRaises(ValueError):compare(self.reference,[self.reference[0],self.reference[0]])
    def test_missing_column(self):
        rows=deepcopy(self.reference);del rows[0]['df']
        with self.assertRaises(ValueError):compare(self.reference,rows)

if __name__=='__main__':unittest.main(verbosity=2)
