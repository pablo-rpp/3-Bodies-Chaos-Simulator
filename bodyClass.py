import numpy as np

G = 6.7E-11

class Body():
    """
    A class used to represent the objects presents in the 3-body problem.
    ...

    Attributes
    ----------
    location : numpy.ndarray
        Object spatial position
    momentum : numpy.ndarray
        Object momentum
    mass : float
        Object mass
    k, l : numpy.ndarray
        Coefficients used by Runge-Kutta methods

    Methods
    -------
    distance(body, increment)
        Return a power distance between body object (plus increment) and self object.
        The power is (-3/2) and only used in derivateMomentum method.

    derivatePosition(increment)
        Return the numerical derivate of the position of the object, considering the increment in momentum.

    gForceInteractions(body, increment)
        Return the gravitational force between body and self, considering the increment in distance.

    derivateMomentum(body1, body2, increment)
        Return the numerical derivate of the momentum of the object, considering the increment in distance.
    """


    global G


    def __init__(self, location, momentum, mass):
        self.location = location
        self.momentum = momentum
        self.mass = mass
        self.k = np.zeros((4, 3))
        self.l = np.zeros((4, 3))

    def distance(self, body, increment):
        #Aquí la distancia está planteada como un elemento dinámico
        #esto puede dar errores en las colisiones???
        return np.inner(self.location - body.location + increment,
                            self.location - body.location + increment)**(-3/2)
    def derivatePosition(self, increment):
        return (self.momentum + increment)/self.mass

    def gForceInteractions(self, body, increment):
        return -G*self.mass*body.mass*(self.location + increment - body.location)*self.distance(body, increment)

    def derivateMomentum(self, body1, body2, increment):
        return self.gForceInteractions(body1, increment) + self.gForceInteractions(body2, increment)
