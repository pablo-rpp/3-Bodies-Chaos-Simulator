
from bodyClass import *
from RKClass import *
from brahma import *
import numpy as np
import sys
import os
import vpython as vp
from colorama import Fore, Style
from tqdm import tqdm


N = 100000
a = 0
b = 1000
#L = 384399E3
#locations
q1 = np.array([0.5, 0.1, 0.3])
q2 = np.array([0., 0.5, 0.])
q3 = np.array([0., 0., 0.5])

#momentums
p1 = np.array([0., 0., 0.])
p2 = np.array([0., 0, 0.])
p3 = np.array([0., 0., 0.])

#mass
mass = [1E5, 2E5, 5E5]

body1 = Body(q1, p1, mass[0])
body2 = Body(q2, p2, mass[1])
body3 = Body(q3, p3, mass[2])

RK = rungeKutta(body1, body2, body3, N, a, b)

del(p1, p2, p3, q1, q2, q3, mass, N, a, b)


def Bosco():
    global G
    nullIncrement = np.zeros((3, 3))


    try:
        os.mkdir('./Simulation_Data')
    except FileExistsError:
        pass

    file = open('Simulation_Data/positions_simulation.txt', 'w')
#    fileAux = open('Simulation_Data/momentums_simulation.txt', 'w')
    print("Calculando trayectorias...")
    for j in tqdm(range(RK.numIter)):
        RK.wrapKL()
        if (j<30):
#            print(RK.bodies[0].k[0])
#            print(RK.bodies[0].l[0])
#            print(RK.bodies[1].k[0])
#            print(RK.bodies[1].l[0])
#            print(RK.bodies[2].k[0])
#            print(RK.bodies[2].l[0])

            print("Iter "+str(j))
        #k1, l1
        RK.kCalculus(0, RK.wrappedK)
        RK.lCalculus(0, RK.wrappedL)
        #k2, l2
        RK.kCalculus(1, 0.5*RK.h*RK.wrappedK)
        RK.lCalculus(1, 0.5*RK.h*RK.wrappedL)
        #k3, l3
        RK.kCalculus(2, 0.5*RK.h*RK.wrappedK)
        RK.lCalculus(2, 0.5*RK.h*RK.wrappedL)
        #k4, l4
        RK.kCalculus(3, (RK.h-1)*RK.wrappedK)
        RK.lCalculus(3, (RK.h-1)*RK.wrappedL)

        RK.rkLocation()
        RK.rkMomentum()



        file.write(str(RK.bodies[0].location[0]) + ',' + str(RK.bodies[0].location[1])+ ','+ str(RK.bodies[0].location[2])+ ';')
        file.write(str(RK.bodies[1].location[0]) + ',' + str(RK.bodies[1].location[1])+ ','+ str(RK.bodies[1].location[2])+ ';')
        file.write(str(RK.bodies[2].location[0]) + ',' + str(RK.bodies[2].location[1])+ ','+ str(RK.bodies[2].location[2])+ '\n')


#        fileAux.write(str(RK.bodies[0].momentum[0]) + ',' + str(RK.bodies[0].momentum[1])+ ','+ str(RK.bodies[0].momentum[2])+ ';')
#        fileAux.write(str(RK.bodies[1].momentum[0]) + ',' + str(RK.bodies[1].momentum[1])+ ','+ str(RK.bodies[1].momentum[2])+ ';')
#        fileAux.write(str(RK.bodies[2].momentum[0]) + ',' + str(RK.bodies[2].momentum[1])+ ','+ str(RK.bodies[2].momentum[2])+ '\n')

    file.close()

Bosco()

Brahma()
