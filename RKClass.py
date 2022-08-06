import numpy as np

def moduli(a, b):
    """
    moduli(a, b)
    Take an element a in a class of Z/3Z and return the representative of the class.

    Parameters
    ----------
    a: int


    """
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
    body1, body2, body3 : bodyClass.Body
        Objects of the 3-body problem.
    numIter: int
        Number of iteratios to use in the numerical method.
    initTime, finalTime: int
        Both define the solution interval .

    Methods
    -------

    wrapKL()
        Give a proper structure to the Runge-Kutta coefficients.

    kCalculus(index, increment)
        Calculate the coefficients k with given index for every body. Increment respond
        to the Runge-Kutta 4'th order formula.

    lCalculus(index, increment)
        Calculate the coefficients l with given index for every body. Increment respond
        to the Runge-Kutta 4'th order formula.

    rkMomentum()
        Update the bodies momentum by Runge-Kutta method.

    rkLocation()
        Update the bodies position by Runge-Kutta method.
    """

    def __init__(self, body1, body2, body3, numIter, initTime, finalTime):
        self.bodies = np.array([body1, body2, body3])
        self.numIter = numIter
        self.h = (finalTime - initTime)/numIter
        ##nullIncrement = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])


    def wrapKL(self):
        # wrappedK contiene (k1DeCadaCuerpo, k2DeCadaCuerpo, k3DeCadaCuerpo, k4DeCadaCuerpo)
        # Wrap both kinf of coefficients

        self.wrappedK = np.zeros((4, 3, 3))
        self.wrappedL = np.zeros((4, 3, 3))

        for index in range(4):
            for b in range(3):
                self.wrappedK[index, b] = self.bodies[b].k[index]
                self.wrappedL[index, b] = self.bodies[b].l[index]



    def kCalculus(self, index, increment): # WARNING: Aquí falla algo
        for i in range(3):
            self.bodies[i].k[index] = self.bodies[i].derivatePosition(increment[index][i])

    def lCalculus(self, index, increment):
        for i in range(3):
            self.bodies[i].l[index] = self.bodies[i].derivateMomentum(
                self.bodies[moduli(i+1, 3)], self.bodies[moduli(i+2, 3)], increment[index][i])

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
