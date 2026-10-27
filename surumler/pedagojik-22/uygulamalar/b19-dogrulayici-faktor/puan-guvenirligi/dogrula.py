import unittest
import numpy as np
from analiz import score_share,expected_covariance,quantities,complex_jacobian


class Checks(unittest.TestCase):
    def test_score_variance_matrix_reference(self):
        l=np.array([.6,.7]);E=np.array([[.64,.1],[.1,.51]]);w=np.array([1.,2.])
        S=np.outer(l,l)+E
        expected=(w@l)**2/(w@S@w)
        self.assertAlmostEqual(score_share(l,E,w),expected)
        self.assertLess(score_share(l,E),score_share(l,np.diag(np.diag(E))))

    def test_delta_derivative_independent_central_difference(self):
        for model in ['correlated','resid_cov']:
            p=np.r_[np.linspace(.4,.8,10),np.log(np.linspace(.4,.7,10)),.3]
            if model=='resid_cov':p=np.r_[p,[.06,.05,.04]]
            fun=lambda t:quantities(t,model,np.linspace(1.,1.8,10))
            G=complex_jacobian(fun,p);columns=[]
            for j in range(len(p)):
                d=np.zeros(len(p));d[j]=2e-5
                columns.append((fun(p+d)-fun(p-d))/4e-5)
            np.testing.assert_allclose(G,np.stack(columns,axis=-1),atol=2e-9)

    def test_factor_scale_invariance(self):
        l=np.array([.4,.6,.8]);E=np.diag([.5,.6,.7])
        self.assertAlmostEqual(score_share(l,E),score_share(3*l,E,factor_variance=1/9))

    def test_item_scale_and_compensating_weights(self):
        l=np.array([.4,.6,.8]);E=np.diag([.5,.6,.7]);D=np.diag([2.,.5,3.])
        self.assertAlmostEqual(score_share(l,E),score_share(D@l,D@E@D,weights=1/np.diag(D)))
        self.assertNotAlmostEqual(score_share(l,E),score_share(D@l,D@E@D))

    def test_expected_information_closed_form(self):
        S=np.diag([2.,3.]);D=np.array([[[2.,0.],[0.,0.]],[[0.,0.],[0.,3.]]])
        np.testing.assert_allclose(expected_covariance(S,D,101),np.eye(2)*.02,atol=1e-14)

    def test_full_covariance_contrast(self):
        covariance=np.array([[1.,.8],[.8,1.]])
        plus=np.array([1.,1.]);minus=np.array([1.,-1.])
        self.assertAlmostEqual(plus@covariance@plus,3.6)
        self.assertAlmostEqual(minus@covariance@minus,.4)
        self.assertAlmostEqual(np.sum(plus**2*np.diag(covariance)),2.)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):score_share([.5,.6],[[1,2],[2,1]])
        with self.assertRaises(ValueError):score_share([.5,.6],np.eye(2),[0.,0.])
        with self.assertRaises(ValueError):score_share([.5,.6],np.eye(2),factor_variance=-1.)
        with self.assertRaises(ValueError):expected_covariance(np.eye(2),np.zeros((1,2,2)),100)


if __name__=='__main__':unittest.main(verbosity=2)
