import RKClass
import unittest
import bodyClass
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

N = 100
a = 0
b = 10
RK = RKClass.rungeKutta(body1, body2, body3, N, a, b)
RK.wrapKL()
body1 = bodyClass.Body(q1, p1, mass[0])
body2 = bodyClass.Body(q2, p2, mass[1])
body3 = bodyClass.Body(q3, p3, mass[2])
nI = np.zeros((3))

class TestRKClass(unittest.TestCase):
    def test_kCalculust(self):
        #Test kCalculus
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(RK.kCalculus(0, RK.wrappedK)[i][j], [[0, 0, 0], [0, 1/3, 0], [0, 0, 0]][i][j])
