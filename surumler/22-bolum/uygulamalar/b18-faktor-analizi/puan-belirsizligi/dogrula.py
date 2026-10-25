import unittest
import numpy as np
from analiz import score_kernel,bartlett_kernel,correlation


class Checks(unittest.TestCase):
    def setUp(self):
        self.L=np.array([[.7,.1],[.6,-.1],[.1,.8],[.2,.6]])
        self.P=np.array([[1.,.3],[.3,1.]])
        self.psi=np.array([.4,.5,.3,.4])
        self.R,self.B,self.C,self.V=score_kernel(self.L,self.P,self.psi)

    def test_one_factor_closed_form(self):
        _,B,C,V=score_kernel([[.5],[.5]],[[1.]],[.75,.75])
        np.testing.assert_allclose(B,np.full((2,1),.4))
        self.assertAlmostEqual(C[0,0],.6);self.assertAlmostEqual(V[0,0],.4)

    def test_posterior_precision_reference(self):
        C=np.linalg.inv(np.linalg.inv(self.P)+self.L.T@np.diag(1/self.psi)@self.L)
        np.testing.assert_allclose(self.C,C,atol=1e-14)
        z=np.array([1.,-.2,.5,2.])
        mean=C@self.L.T@(z/self.psi)
        np.testing.assert_allclose(z@self.B,mean,atol=1e-14)

    def test_reparameterization(self):
        T=np.array([[1.2,.3],[-.2,.9]])
        R,B,C,V=score_kernel(self.L@np.linalg.inv(T),T@self.P@T.T,self.psi)
        np.testing.assert_allclose(R,self.R,atol=1e-14)
        np.testing.assert_allclose(B,self.B@T.T,atol=1e-14)
        np.testing.assert_allclose(C,T@self.C@T.T,atol=1e-14)
        np.testing.assert_allclose(V,T@self.V@T.T,atol=1e-14)

    def test_total_variance_and_error(self):
        np.testing.assert_allclose(self.B.T@self.R@self.B,self.V,atol=1e-14)
        error=self.P-self.B.T@self.L@self.P-self.P@self.L.T@self.B+self.B.T@self.R@self.B
        np.testing.assert_allclose(error,self.C,atol=1e-14)
        np.testing.assert_allclose(self.V+self.C,self.P,atol=1e-14)

    def test_bartlett_conditional_unbiasedness(self):
        B,E=bartlett_kernel(self.L,self.psi)
        np.testing.assert_allclose(B.T@self.L,np.eye(2),atol=1e-14)
        np.testing.assert_allclose(B.T@np.diag(self.psi)@B,E,atol=1e-14)
        self.assertGreaterEqual(np.linalg.eigvalsh(E-self.C).min(),-1e-14)

    def test_score_correlation_is_not_factor_correlation(self):
        B,E=bartlett_kernel(self.L,self.psi)
        np.testing.assert_allclose(B.T@self.R@B,self.P+E,atol=1e-14)
        self.assertGreater(abs(correlation(self.V)[0,1]-self.P[0,1]),.01)
        self.assertGreater(abs(correlation(self.P+E)[0,1]-correlation(self.V)[0,1]),.01)

    def test_invalid_or_uninformative_model(self):
        _,B,C,V=score_kernel(np.zeros((3,2)),self.P,[1.,1.,1.])
        np.testing.assert_array_equal(B,np.zeros((3,2)))
        np.testing.assert_allclose(C,self.P)
        with self.assertRaises(ValueError):correlation(V)
        with self.assertRaises(ValueError):score_kernel(self.L,self.P,[.2,.3,-.1,.5])
        with self.assertRaises(ValueError):score_kernel(self.L,[[1,2],[2,1]],self.psi)
        with self.assertRaises(ValueError):bartlett_kernel(np.ones((4,2)),self.psi)


if __name__=='__main__':unittest.main(verbosity=2)
