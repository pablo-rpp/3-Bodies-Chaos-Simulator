import bodyClass
import unittest
import numpy as np

q1 = np.array([6, 0., 0.])
q2 = np.array([0., 6, 0.])
q3 = np.array([0., 0., 4])

p1 = np.array([0., 0., 0.])
p2 = np.array([0., 10, 0.])
p3 = np.array([0., 0., 0.])

mass = [20, 30, 50]

body1 = bodyClass.Body(q1, p1, mass[0])
body2 = bodyClass.Body(q2, p2, mass[1])
body3 = bodyClass.Body(q3, p3, mass[2])
nI = np.zeros((3))

class TestBodyClass(unittest.TestCase):

    def test_distance(self):
        #Test distance functionality
        self.assertAlmostEqual(body1.distance(body2, nI), 0.00163682)
        self.assertAlmostEqual(body2.distance(body3, nI), 0.00266683)
        #Test distance simetry
        self.assertAlmostEqual(body2.distance(body1, nI) - body1.distance(body2, nI), 0.)

    def test_derivatePosition(self):
        #Test derivatePosition
        np.testing.assert_array_equal(body2.derivatePosition(nI), [0, 1/3 , 0])
        np.testing.assert_array_equal(body1.derivatePosition(nI), [0, 0 , 0])

    def test_gForceInteractions(self):
        #Test gForceInteractions
        for i in range(3):
            self.assertAlmostEqual(body1.gForceInteractions(body2, nI)[i], [-3.94801*10**(-10), 3.94801*10**(-10), 0.][i])
            self.assertAlmostEqual(body2.gForceInteractions(body1, nI)[i], [3.94801*10**(-10), -3.94801*10**(-10), 0.][i])

    def test_derivateMomentum(self):
        #Test derivateMomentum
        for i in range(3):
            self.assertAlmostEqual(body1.derivateMomentum(body2, body3, nI)[i], [-1.46687*10**(-9), 3.94801*10**(-10), 7.1471*10**(-10)][i])
            self.assertAlmostEqual(body2.derivateMomentum(body1, body3, nI)[i], [3.94801*10**(-10), -2.0029*10**(-9), 1.07206*10**(-9)][i])
            self.assertAlmostEqual(body3.derivateMomentum(body2, body1, nI)[i], [1.07206*10**(-9), 1.6081*10**(-9), -1.78677*10**(-9)][i])
