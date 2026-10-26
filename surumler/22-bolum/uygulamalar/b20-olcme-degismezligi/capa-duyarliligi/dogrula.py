import unittest
import importlib.util
from pathlib import Path
import numpy as np
from analiz import expected_covariance,pooled_effect,reverse_reference,mean_parts,moment_derivatives


class Checks(unittest.TestCase):
    def setUp(self):
        self.m=dict(L=np.array([[.8,.1],[.2,.7],[.6,.2]]),nu=np.array([[2.],[3.],[4.]]),
                    alpha=np.array([[.5],[.2]]),Phi=np.array([[1.,.3],[.3,1.2]]),Theta=np.diag([.5,.6,.7]))

    def test_information_mean_and_variance_closed_form(self):
        V=expected_covariance([(100,np.array([[4.]]),np.array([[[0.]],[[1.]]]),np.array([[1.],[0.]]))])
        np.testing.assert_allclose(V,np.diag([.04,.32]),atol=1e-14)

    def test_analytic_moment_derivatives(self):
        path=Path(__file__).resolve().parents[1]/'analiz.py'
        specmod=importlib.util.spec_from_file_location('test_invariance_reference',path)
        module=importlib.util.module_from_spec(specmod);specmod.loader.exec_module(module)
        spec,fixed=module.build('scalar',('A1',));t=np.array(spec.starts,float)
        t[spec.labels.index('alpha.A.g2')]=.4;t[spec.labels.index('phi.AA.g2')]=1.3
        for g in [0,1]:
            _,_,_,dS,dm=moment_derivatives(t,spec,fixed,g,module)
            for j in range(len(t)):
                d=np.zeros(len(t));d[j]=1e-5
                _,S1,m1=module.matrices(t+d,spec,fixed,g);_,S0,m0=module.matrices(t-d,spec,fixed,g)
                np.testing.assert_allclose(dS[j],(S1-S0)/2e-5,atol=1e-9)
                np.testing.assert_allclose(dm[j],(m1-m0)/2e-5,atol=1e-9)

    def test_mean_decomposition(self):
        left={k:v.copy() for k,v in self.m.items()};right={k:v.copy() for k,v in self.m.items()}
        left['alpha'][:]=0;right['nu'][0]+=.3
        intercept,factor,total=mean_parts(left,right)
        np.testing.assert_allclose(total,(right['nu']+right['L']@right['alpha']-left['nu']).ravel())
        self.assertAlmostEqual(intercept.mean(),.1)
        np.testing.assert_allclose(factor,(self.m['L']@self.m['alpha']).ravel())

    def test_reference_change_preserves_observed_moments(self):
        out=reverse_reference(self.m,[.4,.1],[1.2,.8])
        np.testing.assert_allclose(out['nu']+out['L']@out['alpha'],self.m['nu']+self.m['L']@self.m['alpha'])
        np.testing.assert_allclose(out['L']@out['Phi']@out['L'].T+out['Theta'],self.m['L']@self.m['Phi']@self.m['L'].T+self.m['Theta'])

    def test_reference_change_not_only_sign(self):
        m=dict(L=np.array([[.7]]),nu=np.array([[3.]]),alpha=np.array([[0.]]),Phi=np.array([[1.]]),Theta=np.array([[.5]]))
        transformed=reverse_reference(m,[.8],[.5])
        self.assertAlmostEqual(transformed['alpha'][0,0],-.4)
        self.assertNotAlmostEqual(transformed['alpha'][0,0],-.8)

    def test_pooled_effect_scale_invariance(self):
        original=pooled_effect(.5,1.,2.,425,891)
        self.assertAlmostEqual(original,.5/np.sqrt((425+891*2)/1316))
        self.assertAlmostEqual(original,pooled_effect(1.5,9.,18.,425,891))

    def test_invalid_or_unidentified_model(self):
        with self.assertRaises(ValueError):pooled_effect(.5,0.,1.,425,891)
        with self.assertRaises(ValueError):reverse_reference(self.m,[0,0],[0,1])
        with self.assertRaises(ValueError):expected_covariance([(100,np.eye(2),np.zeros((1,2,2)),np.zeros((1,2)))])
        right={k:v.copy() for k,v in self.m.items()};right['L']*=2
        with self.assertRaises(ValueError):mean_parts(self.m,right)


if __name__=='__main__':unittest.main(verbosity=2)
