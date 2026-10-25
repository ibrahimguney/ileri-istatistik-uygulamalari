import unittest
import numpy as np
import pandas as pd
from scipy import stats
from analiz import fit,predict,roles,calibrate,corrected_quantile,intervals
class Tests(unittest.TestCase):
    def setUp(self):
        self.train=pd.DataFrame(dict(kaynak_satir=range(1,11),G1=np.arange(10),G3=np.arange(10)*.7+np.array([1,0,1,-1,0,2,1,-2,0,1])))
        self.cal=pd.DataFrame(dict(kaynak_satir=range(11,31),G1=np.arange(20)/2,G3=np.arange(20)*.3))
        self.audit=pd.DataFrame(dict(kaynak_satir=range(31,36),G1=np.arange(5),G3=np.arange(5)))
    def test_OLS_scipy(self):
        m=fit(self.train);r=stats.linregress(self.train.G1,self.train.G3);np.testing.assert_allclose(m['beta'],[r.intercept,r.slope])
    def test_corrected_order_statistic(self):
        q,k=corrected_quantile(np.arange(1,21));self.assertEqual((q,k),(20.,20));self.assertNotEqual(q,np.quantile(np.arange(1,21),.95))
    def test_infinite_small_calibration(self):
        q,k=corrected_quantile(np.arange(1,19));self.assertTrue(np.isinf(q));self.assertEqual(k,19)
    def test_roles_overlap_and_invalid(self):
        roles(self.train,self.cal,self.audit)
        with self.assertRaises(ValueError):roles(self.train,self.train,self.audit)
        with self.assertRaises(ValueError):fit(self.train.assign(G1=1))
    def test_audit_labels_do_not_change_intervals(self):
        m=fit(self.train);c=calibrate(m,self.cal);a=intervals(m,c,self.audit.G1)
        changed=self.audit.assign(G3=-1000);roles(self.train,self.cal,changed);np.testing.assert_array_equal(a,intervals(m,c,changed.G1))
    def test_calibration_changes_width_not_model(self):
        m=fit(self.train);before=m['beta'].copy();c=calibrate(m,self.cal);q=calibrate(m,self.cal.assign(G3=self.cal.G3+100))
        self.assertGreater(q['q'],c['q']);self.assertEqual(before,m['beta'])
    def test_positive_affine_response(self):
        m=fit(self.train);c=calibrate(m,self.cal);a=intervals(m,c,self.audit.G1)
        model=fit(self.train.assign(G3=3*self.train.G3+4));ca=calibrate(model,self.cal.assign(G3=3*self.cal.G3+4))
        np.testing.assert_allclose(intervals(model,ca,self.audit.G1),3*a+4,rtol=1e-12,atol=1e-12)
if __name__=='__main__':unittest.main()
