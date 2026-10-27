import unittest
from dogrula_22 import compare
class ComparisonPolicy(unittest.TestCase):
    def test_numeric_change_is_failure(self):
        self.assertTrue(compare({'estimate':1.0},{'estimate':1.1}))
    def test_version_and_runtime_are_metadata(self):
        self.assertEqual(compare({'surumler':{'numpy':'old'},'bootstrap':{'seconds':90,'mean':2}}, {'surumler':{'numpy':'new'},'bootstrap':{'seconds':60,'mean':2}}),[])
    def test_seconds_outside_runtime_are_compared(self):
        self.assertTrue(compare({'seconds':90},{'seconds':60}))
    def test_missing_statistic_is_failure(self):
        self.assertTrue(compare({'mean':2},{}))
    def test_boolean_scientific_check_is_compared(self):
        self.assertTrue(compare({'valid':True},{'valid':False}))
if __name__=='__main__':unittest.main(verbosity=2)
