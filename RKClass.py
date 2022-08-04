import numpy as np

def moduli(a, b):

    if(a<b):
        return a
    else:
        return a%b

class rungeKutta():
    """
    A class used to execute Runge Kutta method and save results
    ...

    Attributes
    ----------


    Methods
    -------

    """

    def __init__(self, body1, body2, body3, numIter, initTime, finalTime):
        self.bodies = np.array([body1, body2, body3])
        self.numIter = numIter
        self.h = (finalTime - initTime)/numIter
        ##nullIncrement = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])


    def wrapKL(self):
        # wrappedK contiene (k1DeCadaCuerpo, k2DeCadaCuerpo, k3DeCadaCuerpo, k4DeCadaCuerpo)
        # Wrap both kinf of coefficients

        self.wrappedK = np.append(self.bodies[0].k, self.bodies[1].k, axis=0)
        self.wrappedK = np.append(self.wrappedK, self.bodies[2].k, axis=0)

        self.wrappedL = np.append(self.bodies[0].l, self.bodies[1].l, axis=0)
        self.wrappedL = np.append(self.wrappedL, self.bodies[2].l, axis=0)


    def kCalculus(self, index, increment):
        for i in range(3):
            self.bodies[i].k[index] = self.bodies[i].derivatePosition(increment[index, i])

    def lCalculus(self, index, increment):
        for i in range(3):

            self.bodies[i].l[index] = self.bodies[i].derivateMomentum(
                self.bodies[moduli(i+1, 3)], self.bodies[moduli(i+2, 3)], increment[index, i])

    def rkMomentum(self):
        for i in range(3):
            self.bodies[i].momentum += (self.h/6)*(self.bodies[i].l[0]
                                    + 2*(self.bodies[i].l[1] + self.bodies[i].l[2] )
                                    + self.bodies[i].l[3])

    def rkLocation(self):
        for i in range(3):
            self.bodies[i].location += (self.h/6)*(self.bodies[i].k[0]
                                    + 2*(self.bodies[i].k[1] + self.bodies[i].k[2] )
                                    + self.bodies[i].k[3])
