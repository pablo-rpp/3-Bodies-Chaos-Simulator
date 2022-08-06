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

        self.wrappedK = np.zeros((4, 3, 3))
        self.wrappedL = np.zeros((4, 3, 3))

        for index in range(4):
            for b in range(3):
                self.wrappedK[index, b] = self.bodies[b].k[index]
                self.wrappedL[index, b] = self.bodies[b].l[index]



    def kCalculus(self, index, increment): # WARNING: Aquí falla algo
#        TestList = [] #Test
        for i in range(3):
            self.bodies[i].k[index] = self.bodies[i].derivatePosition(increment[index][i])
#            TestList.append(self.bodies[i].k[index]) #Test
        #print(TestList)
#        return TestList #Test

    def lCalculus(self, index, increment):
        for i in range(3):
            self.bodies[i].l[index] = self.bodies[i].derivateMomentum(
                self.bodies[moduli(i+1, 3)], self.bodies[moduli(i+2, 3)], increment[index][i])

    def rkMomentum(self):
        for i in range(3):
#
            self.bodies[i].momentum += (self.h/6)*(self.bodies[i].l[0]
                                    + 2*(self.bodies[i].l[1] + self.bodies[i].l[2] )
                                    + self.bodies[i].l[3])

    def rkLocation(self):
        for i in range(3):
            self.bodies[i].location += (self.h/6)*(self.bodies[i].k[0]
                                    + 2*(self.bodies[i].k[1] + self.bodies[i].k[2] )
                                    + self.bodies[i].k[3])
