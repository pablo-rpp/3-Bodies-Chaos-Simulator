
import numpy as np
from math import pow

G = 6.7E-11

class Body():
    """
    A class used to represent the objects presents in the 3 bodies problem.
    ...

    Attributes
    ----------
    location : numpy.ndarray
    momentum : numpy.ndarray
    mass : float
    k, l : numpy.ndarray

    Methods
    -------
    distance :
    derivatePosition :
    gForceInteractions :
    derivateMomentum :
    """

    global G ## WARNING: no se si estoy funciona bien...

    k = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
    l = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def __init__(self, location, momentum, mass):
        self.location = location
        self.momentum = momentum
        self.mass = mass

    def distance(self, body):
        #Aquí la distancia está planteada como un elemento dinámico
        #esto puede dar errores en las colisiones???
        return pow(np.inner(self.location, body.location))

    #Lo de incremento hay que revisarlo
    def derivatePosition(self, increment):
        return (self.momentum + increment)/self.mass

    def gForceInteractions(self, body, increment):
        return -G*self.mass*body.mass*(self.location + increment - body.location)*self.distance(body)

    def derivateMomentum(self, body1, body2, increment):
        return self.gForceInteractions(self, body1, increment) + self.gForceInteractions(self, body2, increment)
