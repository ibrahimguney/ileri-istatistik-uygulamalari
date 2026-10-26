import unittest
import importlib.util
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from analiz import residual_sensitivity


def reference_module():
    spec=importlib.util.spec_from_file_location('test_sem_reference',Path(__file__).resolve().parents[1]/'analiz.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


class Checks(unittest.TestCase):
    def test_rho_zero_original_decomposition(self):
        r=residual_sensitivity(2.,5.,1.,.4,.7,0.)
        self.assertAlmostEqual(r['b'],.5);self.assertAlmostEqual(r['psi_C'],4.5)
        self.assertAlmostEqual(r['c_prime'],.5);self.assertAlmostEqual(r['indirect'],.2)

    def test_joint_covariance_reconstruction(self):
        u,v,w,a,total,varK=2.,5.,1.,.4,.7,.2
        expected=np.array([[a*a*varK+u,a*total*varK+w,a*varK],
                           [a*total*varK+w,total*total*varK+v,total*varK],
                           [a*varK,total*varK,varK]])
        for rho in np.linspace(-.8,.8,9):
            r=residual_sensitivity(u,v,w,a,total,rho);b,s,p=r['b'],r['residual_covariance'],r['psi_C']
            actual=expected.copy();actual[0,1]=actual[1,0]=a*total*varK+b*u+s
            actual[1,1]=total*total*varK+b*b*u+p+2*b*s
            np.testing.assert_allclose(actual,expected,atol=1e-13)

    def test_zero_threshold_independent_root(self):
        root=brentq(lambda rho:residual_sensitivity(2.,5.,1.,.4,.7,rho)['b'],-.9,.9)
        self.assertAlmostEqual(root,1/np.sqrt(10),places=11)

    def test_latent_scale_invariance(self):
        r=residual_sensitivity(2.,5.,1.,.4,.7,.3)
        changed=residual_sensitivity(2.*9,5.*4,1.*3*2,.4*3,.7*2,.3)
        self.assertAlmostEqual(changed['b'],r['b']*2/3)
        self.assertAlmostEqual(changed['indirect'],r['indirect']*2)
        self.assertAlmostEqual(changed['total'],r['total']*2)

    def test_mimic_path_derivatives(self):
        module=reference_module();base=module.build_models()['mediation']
        model=module.Model('mediation',base.observed,base.parameters+[('A1~K','A','A1','K','lin')],base.fixed)
        t=module.starting_values(model,np.eye(11));t[-1]=.2
        lower=np.tril_indices(11)
        numeric=module.numeric_jacobian(lambda p:model.covariance(p)[lower],t)
        analytic=model.derivatives(t)[:,lower[0],lower[1]].T
        np.testing.assert_allclose(analytic,numeric,atol=1e-8)

    def test_binary_predictor_group_gap(self):
        module=reference_module();base=module.build_models()['mediation']
        model=module.Model('mediation',base.observed,base.parameters+[('A1~K','A','A1','K','lin')],base.fixed)
        t=module.starting_values(model,np.eye(11))
        for name,value in [('A~K',.2),('C~A',.5),('C~K',.1),('A1~K',.3)]:t[model.labels().index(name)]=value
        S=model.covariance(t);slopes=S[:-1,-1]/S[-1,-1]
        self.assertAlmostEqual(slopes[0],.5);self.assertAlmostEqual(slopes[1],.2)
        self.assertAlmostEqual(slopes[5],.2)

    def test_invalid_conditional_model(self):
        for rho in [-1.,1.,np.nan]:
            with self.assertRaises(ValueError):residual_sensitivity(2.,5.,1.,.4,.7,rho)
        with self.assertRaises(ValueError):residual_sensitivity(0.,5.,1.,.4,.7,0.)
        with self.assertRaises(ValueError):residual_sensitivity(1.,1.,2.,.4,.7,0.)


if __name__=='__main__':unittest.main(verbosity=2)
