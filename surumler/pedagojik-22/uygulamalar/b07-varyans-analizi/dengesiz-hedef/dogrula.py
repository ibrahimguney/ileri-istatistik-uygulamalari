import unittest
import numpy as np
import pandas as pd
import statsmodels.api as sm
from analiz import fit_cells,contrast,CELLS

class Checks(unittest.TestCase):
    def data(self,counts):
        return pd.DataFrame([dict(supp=s,dose=d,len=3*j+i*.3+(i%2)*.2) for j,((s,d),n) in enumerate(zip(CELLS,counts)) for i in range(n)])
    def test_balanced_marginal_equality(self):
        d=self.data([4]*6);b,V,X,df=fit_cells(d);c=np.r_[np.ones(3)/3,-np.ones(3)/3]
        self.assertAlmostEqual(c@b,d[d.supp=='OJ'].len.mean()-d[d.supp=='VC'].len.mean())
    def test_unbalanced_composition_identity(self):
        d=self.data([3,5,4,7,3,6]);b,V,X,df=fit_cells(d);n=X.sum(0);c=np.r_[n[:3]/n[:3].sum(),-n[3:]/n[3:].sum()]
        self.assertAlmostEqual(c@b,d[d.supp=='OJ'].len.mean()-d[d.supp=='VC'].len.mean())
        self.assertGreater(abs(c@b-np.r_[np.ones(3)/3,-np.ones(3)/3]@b),.1)
    def test_hc3_reference(self):
        d=self.data([3,5,4,7,3,6]);b,V,X,df=fit_cells(d);r=sm.OLS(d.len,X).fit().get_robustcov_results(cov_type='HC3')
        np.testing.assert_allclose(V,r.cov_params(),atol=1e-12)
    def test_interaction_difference_identity(self):
        b=np.array([2.,6.,7.,1.,3.,3.]);c=np.array([-1,1,0,1,-1,0.])
        self.assertAlmostEqual(c@b,(b[1]-b[4])-(b[0]-b[3]))
    def test_reordering(self):
        d=self.data([3,5,4,7,3,6]);a=fit_cells(d);b=fit_cells(d.sample(frac=1,random_state=1))
        np.testing.assert_allclose(a[0],b[0]);np.testing.assert_allclose(a[1],b[1])
    def test_family_interval_widens(self):
        b,V,_,df=fit_cells(self.data([4]*6));c=np.array([-1,1,0,1,-1,0.])
        a=contrast(b,V,c,df);f=contrast(b,V,c,df,2);self.assertLess(f['ci_family95'][0],a['ci_family95'][0])
    def test_missing_cell_rejected(self):
        with self.assertRaises(ValueError):fit_cells(self.data([0,4,4,4,4,4]))

if __name__=='__main__':unittest.main(verbosity=2)
