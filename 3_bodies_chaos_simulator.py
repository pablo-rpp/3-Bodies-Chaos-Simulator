import numpy as np
import sys
import vpython as vp
from colorama import Fore, Style
from tqdm import tqdm
import os
global G, n_01, n_02, n_12, n_10, n_20, n_21, q0, q1, q2, p0, p1, p2, m
global N, a, b

rate = 3000
N = 100000
a = 0
b = 1000
q0 = [0.5, 0.1, 0.3]
q1 = [0, 0.5, 0]
q2 = [0, 0, 0.5]
p0 = [0, 0, 0]
p1 = [0, 0, 0]
p2 = [0, 0, 0]
m = [1E5, 2E5, 5E5]


############################
# NOTE: Funciones para Bosco
############################
def norma(x,y):
    sol=0
    for i in range(len(x)):
        sol += (x[i] - y[i])**2

    return np.sqrt(sol)

## NOTE: Derivada del momento
def P_0(q0x, q1x, q2x, n_01, n_02):
    a = m[1]*(q0x - q1x)*n_01**(-3)
    b = m[2]*(q0x - q2x)*n_02**(-3)
    Sol = -G*m[0]*(a+b)
    return Sol

def P_1(q1x, q0x, q2x, n_10, n_12):
    a = m[0]*(q1x - q0x)*n_10**(-3)
    b = m[2]*(q1x - q2x)*n_12**(-3)
    Sol = -G*m[1]*(a+b)
    return Sol

def P_2(q2x, q0x, q1x, n_20, n_21):
    a = m[0]*(q2x - q0x)*n_20**(-3)
    b = m[1]*(q2x - q1x)*n_21**(-3)
    Sol = -G*m[2]*(a+b)
    return Sol

## NOTE: Derivada posición
def Q_0(p):return p/m[0]
def Q_1(p):return p/m[1]
def Q_2(p):return p/m[2]

############################
############################

def Man():
    print(Fore.CYAN)
    print('''
#############################################################################
#############################################################################
Help: Abre esta guía
Modify: Permite modificar el PVI de la simulación.
Setup: Carga los datos necesarios para ejecutar la simulación. Hay que
ejecutar esta opción cada vez que se modifica el PVI.
Chaos: Activa la simulación en pantalla. Si se ejecutan varias simulaciones
en la misma sesión se irán mostrando las distintas trayectorias superpuestas.
Exit: Sale del programa.(aunque hay que cerrar la ventana de la simulación
igualmente.)

PVI: Problema de Valores Iniciales. Determina los valores de masa, velocidad
y posición en el instante inicial de cada cuerpo. Ya hay unos cargados por
defecto.
    Valores de posición y momento(q y p):
        A la hora de modificarlos es recomendable que sus valores estén
        comprendidos en [-1, 1]
    Masa(m):
        La masa de cada cuerpo está multiplicada por 10^5. La masa tiene más
        libertad de modificación, aunque una excesivamente grande podría
        impedir los cálculos.

Sudo su: Con este código se puede acceder a los valores de tiempo e iteraciones
    Tiempo: a = 0, b = 10000 por defecto. Si se modifican estos valores
    en aumento es recomendable aumentar N.
    Iteraciones: N = 100000 por defecto. Aumentar este valor ralentizará los
    cálculos pero ofrecerá simulaciones más precisas.
    Factor de convergencia h: h = (b-a)/N por definición. Es recomendable que
    h <= 0.1(como lo está por defecto)
#############################################################################
#############################################################################
    ''')
    return main()

def Modify():
    global q0, q1, q2, p0, p1, p2, m
    print(Fore.RED)
    print("Antes de modificar los valores del PVI aseguresé de haber leído"+
    " la sección de ayuda para un correcto uso.")
    print(Style.RESET_ALL)
    order = input("¿Desea continuar igualmente?(Y/N): ")
    order = order.upper()
    if order in ("Y", "YES"):
        pass
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        return main()

    print("Modifique los valores según vayan apareciendo.")
    print("Pulse intro solo par usar los dantos anteriores.")
    print("q0: ", q0)
    try:
        x = float(input("q0(0): "))
    except:
        x = q0[0]
    try:
        y = float(input("q0(1): "))
    except:
        y = q0[1]
    try:
        z = float(input("q0(2): "))
    except:
        z = q0[2]
    q0 = [x, y, z]

    print("q1: ", q1)
    try:
        x = float(input("q1(0): "))
    except:
        x = q1[0]
    try:
        y = float(input("q1(1): "))
    except:
        y = q1[1]
    try:
        z = float(input("q1(2): "))
    except:
        z = q1[2]
    q1 = [x, y, z]
    print("q2: ", q2)
    try:
        x = float(input("q2(0): "))
    except:
        x = q2[0]
    try:
        y = float(input("q2(1): "))
    except:
        y = q2[1]
    try:
        z = float(input("q2(2): "))
    except:
        z = q2[2]
    q2 = [x, y, z]
    print("p0: ", p0)
    try:
        x = float(input("p0(0): "))
    except:
        x = p0[0]
    try:
        y = float(input("p0(1): "))
    except:
        y = p0[1]
    try:
        z = float(input("p0(2): "))
    except:
        z = p0[2]
    p0 = [x, y, z]
    print("p1: ", p1)
    try:
        x = float(input("p1(0): "))
    except:
        x = p1[0]
    try:
        y = float(input("p1(1): "))
    except:
        y = p1[1]
    try:
        z = float(input("p1(2): "))
    except:
        z = p1[2]
    p1 = [x, y, z]
    print("p2: ", p2)
    try:
        x = float(input("p2(0): "))
    except:
        x = p2[0]
    try:
        y = float(input("p2(1): "))
    except:
        y = p2[1]
    try:
        z = float(input("p2(2): "))
    except:
        z = p2[2]
    p2 = [x, y, z]
    print("El valor siguiente se muntiplicará por 10^5.\n"
    +"m: ", m)
    try:
        x = float(input("m(0): "))
    except:
        x = m[0]*10**-5
    try:
        y = float(input("m(1): "))
    except:
        y = m[1]*10**-5
    try:
        z = float(input("m(2): "))
    except:
        z = m[2]*10**-5
    m = [x*10**5, y*10**5, z*10**5]

    print("Nuevo PVI asignado:\n"+
    "q0: ", q0, "\nq1: ", q1, "\nq2: ",q2, "\np0: ", p0, "\np1: ", p1, "\np2: ",
    p2, "\nm: ", m)
    input("Presione Intro para continuar.")
    return main()



def Brahma():

    Rsun = 2E9 #Radio solar
    L = 4e10 #Factor para distancias
    # NOTE: Ajustes de la escena
    vp.scene.width = vp.scene.height = 800 #Dimensiones de la pantalla
    vp.scene.title = "Interacción gravitatoria 3 Cuerpos"
    vp.scene.caption = "Usa el botón derecho del ratón para mover la visualización, izquierdo para zoom "
    vp.scene.range = 2*L
    vp.scene.forward = vp.vec(-1, -1, -1) #Zoom
    ## NOTE: Ejes de referencia
    xaxis = vp.curve(color = vp.color.gray(0.5), radius = 3e8)
    xaxis.append(vp.vec(0, 0, 0))
    xaxis.append(vp.vec(L, 0, 0))
    yaxis = vp.curve(color = vp.color.gray(0.5), radius = 3e8)
    yaxis.append(vp.vec(0, 0, 0))
    yaxis.append(vp.vec(0, L, 0))
    zaxis = vp.curve(color = vp.color.gray(0.5), radius = 3e8)
    zaxis.append(vp.vec(0, 0, 0))
    zaxis.append(vp.vec(0, 0, L))

    aux0 = list()
    aux1 = list()
    try:
        data = open('Simulation_Data/positions_simulation.txt', 'r')
    except:
        print(Fore.RED)
        print("¡Error! No se han encontrado datos para realizar la simulación."+
        "\nAseguresé de haber ejecutado <<SetUp>> antes.\n")
        print(Style.RESET_ALL)
        input("Presione Intro para continuar.")
        return main()
    init = data.readline()
    init = init[:-1].split(';')
    for i in range(len(init)):
        aux1.append(init[i].split(','))
        for j in range(len(aux1[i])):
            aux0.append(float(aux1[i][j]))

    # NOTE: Preparación valores iniciales
    Bodies = list()
    body_colors = [vp.color.red, vp.color.green, vp.color.blue,
                vp.color.yellow, vp.color.cyan, vp.color.magenta]

    q0 = [vp.vec(aux0[0], aux0[1], aux0[2]), vp.vec(aux0[3], aux0[4], aux0[5]),
    vp.vec(aux0[6], aux0[7], aux0[8])] #Posición inicial
    ###############################################################################
    #################################CREACIÓN DE CUERPOS###########################
    ###############################################################################

    for i in range(3):
        body = vp.sphere(pos = L*q0[i], make_trail = True, retain = 300,
                trail_radius = 2e8)
        body.radius = Rsun
        body.color = body.trail_color = body_colors[3+i]
        Bodies.append(body)

    while True:
        vp.rate(rate)
        i = 0
        for body in Bodies:

            try:
                ite = data.readline()
            except:
                break
            aux1 = aux0 = []
            ite = ite[:-1].split(';')

            for terna in ite:
                aux1.append(terna.split(','))
            ## NOTE: Actualización de posición
            try:
                body.pos = L*vp.vec(float(aux1[i][0]), float(aux1[i][1]), float(aux1[i][2]))
                i+=1
            except:
                return main()

    data.close()


def Bosco():
    global G, N, a, b
    G = 6.7E-11
    n_01 = n_10 = norma(q0,q1)
    n_02 = n_20 = norma(q0,q2)
    n_12 = n_21 = norma(q1,q2)

    try:
        os.mkdir('./Simulation_Data')
    except:
        pass

    # NOTE: x_i = Q_i, y_i = P_i
    """a, b = 0, 1000
    N = 100000"""
    h = (b-a)/N
    y0_n = [q0[0], q0[1], q0[2]]
    y1_n = [q1[0], q1[1], q1[2]]
    y2_n = [q2[0], q2[1], q2[2]]


    x0_n = [p0[0], p0[1], p0[2]]
    x1_n = [p1[0], p1[1], p1[2]]
    x2_n = [p2[0], p2[1], p2[2]]

    n_01 = n_10 = norma(y0_n,y1_n)
    n_02 = n_20 = norma(y0_n,y2_n)
    n_12 = n_21 = norma(y1_n,y2_n)

    Q_n = [[y0_n, y1_n, y2_n]]
    P_n = [[x0_n, x1_n, x2_n]]
    print('Iter: 0\n---------P--------\n', P_n[0], '\n\n',
    '---------Q--------\n', Q_n[0], '\n\n')

    f = open('Simulation_Data/rk_results.txt', 'w')
    g = open('Simulation_Data/positions_simulation.txt', 'w')

    print("Calculando trayectorias...")
    for j in tqdm(range(N)):

        #k1 y l1
        k1_00 = Q_0(x0_n[0])
        k1_01 = Q_0(x0_n[1])
        k1_02 = Q_0(x0_n[2])

        k1_10 = Q_1(x1_n[0])
        k1_11 = Q_1(x1_n[1])
        k1_12 = Q_1(x1_n[2])

        k1_20 = Q_2(x2_n[0])
        k1_21 = Q_2(x2_n[1])
        k1_22 = Q_2(x2_n[2])

        l1_00 = P_0(y0_n[0], y1_n[0], y2_n[0], n_01, n_02)
        l1_01 = P_0(y0_n[1], y1_n[1], y2_n[1], n_01, n_02)
        l1_02 = P_0(y0_n[2], y1_n[2], y2_n[2], n_01, n_02)

        l1_10 = P_1(y1_n[0], y0_n[0], y2_n[0], n_10, n_12)
        l1_11 = P_1(y1_n[1], y0_n[1], y2_n[1], n_10, n_12)
        l1_12 = P_1(y1_n[2], y0_n[2], y2_n[2], n_10, n_12)

        l1_20 = P_2(y2_n[0], y0_n[0], y1_n[0], n_20, n_21)
        l1_21 = P_2(y2_n[1], y0_n[1], y1_n[1], n_20, n_21)
        l1_22 = P_2(y2_n[2], y0_n[2], y1_n[2], n_20, n_21)

        #k2 y l2
        k2_00 = Q_0(x0_n[0] + h*0.5*k1_00)
        k2_01 = Q_0(x0_n[1] + h*0.5*k1_01)
        k2_02 = Q_0(x0_n[2] + h*0.5*k1_02)

        k2_10 = Q_1(x1_n[0] + h*0.5*k1_10)
        k2_11 = Q_1(x1_n[1] + h*0.5*k1_11)
        k2_12 = Q_1(x1_n[2] + h*0.5*k1_12)

        k2_20 = Q_2(x2_n[0] + h*0.5*k1_20)
        k2_21 = Q_2(x2_n[1] + h*0.5*k1_20)
        k2_22 = Q_2(x2_n[2] + h*0.5*k1_20)

        l2_00 = P_0(y0_n[0] + h*0.5*l1_00, y1_n[0], y2_n[0], n_01, n_02)
        l2_01 = P_0(y0_n[1] + h*0.5*l1_01, y1_n[1], y2_n[1], n_01, n_02)
        l2_02 = P_0(y0_n[2] + h*0.5*l1_02, y1_n[2], y2_n[2], n_01, n_02)

        l2_10 = P_1(y1_n[0] + h*0.5*l1_10, y0_n[0], y2_n[0], n_10, n_12)
        l2_11 = P_1(y1_n[1] + h*0.5*l1_11, y0_n[1], y2_n[1], n_10, n_12)
        l2_12 = P_1(y1_n[2] + h*0.5*l1_12, y0_n[2], y2_n[2], n_10, n_12)

        l2_20 = P_2(y2_n[0] + h*0.5*l1_20, y0_n[0], y1_n[0], n_20, n_21)
        l2_21 = P_2(y2_n[1] + h*0.5*l1_21, y0_n[1], y1_n[1], n_20, n_21)
        l2_22 = P_2(y2_n[2] + h*0.5*l1_22, y0_n[2], y1_n[2], n_20, n_21)

        #k3 y l3
        k3_00 = Q_0(x0_n[0] + h*0.5*k2_00)
        k3_01 = Q_0(x0_n[1] + h*0.5*k2_01)
        k3_02 = Q_0(x0_n[2] + h*0.5*k2_02)

        k3_10 = Q_1(x1_n[0] + h*0.5*k2_10)
        k3_11 = Q_1(x1_n[1] + h*0.5*k2_11)
        k3_12 = Q_1(x1_n[2] + h*0.5*k2_12)

        k3_20 = Q_2(x2_n[0] + h*0.5*k2_20)
        k3_21 = Q_2(x2_n[1] + h*0.5*k2_21)
        k3_22 = Q_2(x2_n[2] + h*0.5*k2_22)

        l3_00 = P_0(y0_n[0] + h*0.5*l2_00, y1_n[0], y2_n[0], n_01, n_02)
        l3_01 = P_0(y0_n[1] + h*0.5*l2_01, y1_n[1], y2_n[1], n_01, n_02)
        l3_02 = P_0(y0_n[2] + h*0.5*l2_02, y1_n[2], y2_n[2], n_01, n_02)

        l3_10 = P_1(y1_n[0] + h*0.5*l2_10, y0_n[0], y2_n[0], n_10, n_12)
        l3_11 = P_1(y1_n[1] + h*0.5*l2_11, y0_n[1], y2_n[1], n_10, n_12)
        l3_12 = P_1(y1_n[2] + h*0.5*l2_12, y0_n[2], y2_n[2], n_10, n_12)

        l3_20 = P_2(y2_n[0] + h*0.5*l2_20, y0_n[0], y1_n[0], n_20, n_21)
        l3_21 = P_2(y2_n[1] + h*0.5*l2_21, y0_n[1], y1_n[1], n_20, n_21)
        l3_22 = P_2(y2_n[2] + h*0.5*l2_22, y0_n[2], y1_n[2], n_20, n_21)

        #k4 y l4
        k4_00 = Q_0(x0_n[0]*h*k3_00)
        k4_01 = Q_0(x0_n[1]*h*k3_01)
        k4_02 = Q_0(x0_n[2]*h*k3_02)

        k4_10 = Q_1(x1_n[0]*h*k3_10)
        k4_11 = Q_1(x1_n[1]*h*k3_11)
        k4_12 = Q_1(x1_n[2]*h*k3_12)

        k4_20 = Q_2(x2_n[0]*h*k3_20)
        k4_21 = Q_2(x2_n[1]*h*k3_21)
        k4_22 = Q_2(x2_n[2]*h*k3_22)

        l4_00 = P_0(y0_n[0]*h*l3_00, y1_n[0], y2_n[0], n_01, n_02)
        l4_01 = P_0(y0_n[1]*h*l3_01, y1_n[1], y2_n[1], n_01, n_02)
        l4_02 = P_0(y0_n[2]*h*l3_02, y1_n[2], y2_n[2], n_01, n_02)

        l4_10 = P_1(y1_n[0]*h*l3_10, y0_n[0], y2_n[0], n_10, n_12)
        l4_11 = P_1(y1_n[1]*h*l3_11, y0_n[1], y2_n[1], n_10, n_12)
        l4_12 = P_1(y1_n[2]*h*l3_12, y0_n[2], y2_n[2], n_10, n_12)

        l4_20 = P_2(y2_n[0]*h*l3_20, y0_n[0], y1_n[0], n_20, n_21)
        l4_21 = P_2(y2_n[1]*h*l3_21, y0_n[1], y1_n[1], n_20, n_21)
        l4_22 = P_2(y2_n[2]*h*l3_22, y0_n[2], y1_n[2], n_20, n_21)

        #Y_n+1

        x0_n[0] += (h/6)*(l1_00 + 2*(l2_00 + l3_00) + l4_00)
        x1_n[0] += (h/6)*(l1_10 + 2*(l2_10 + l3_10) + l4_10)
        x2_n[0] += (h/6)*(l1_20 + 2*(l2_20 + l3_20) + l4_20)

        x0_n[1] += (h/6)*(l1_01 + 2*(l2_01 + l3_01) + l4_01)
        x1_n[1] += (h/6)*(l1_11 + 2*(l2_11 + l3_11) + l4_11)
        x2_n[1] += (h/6)*(l1_21 + 2*(l2_21 + l3_21) + l4_21)

        x0_n[2] += (h/6)*(l1_02 + 2*(l2_02 + l3_02) + l4_02)
        x1_n[2] += (h/6)*(l1_12 + 2*(l2_12 + l3_12) + l4_12)
        x2_n[2] += (h/6)*(l1_22 + 2*(l2_22 + l3_22) + l4_22)


        y0_n[0] += (h/6)*(k1_00 + 2*(k2_00 + k3_00) + k4_00)
        y1_n[0] += (h/6)*(k1_10 + 2*(k2_10 + k3_10) + k4_10)
        y2_n[0] += (h/6)*(k1_20 + 2*(k2_20 + k3_20) + k4_20)

        y0_n[1] += (h/6)*(k1_01 + 2*(k2_01 + k3_01) + k4_01)
        y1_n[1] += (h/6)*(k1_11 + 2*(k2_11 + k3_11) + k4_11)
        y2_n[1] += (h/6)*(k1_21 + 2*(k2_21 + k3_21) + k4_21)

        y0_n[2] += (h/6)*(k1_02 + 2*(k2_02 + k3_02) + k4_02)
        y1_n[2] += (h/6)*(k1_12 + 2*(k2_12 + k3_12) + k4_12)
        y2_n[2] += (h/6)*(k1_22 + 2*(k2_22 + k3_22) + k4_22)

        g.write(str(y0_n[0]) + ',' + str(y0_n[1])+ ','+ str(y0_n[2])+ ';')
        g.write(str(y1_n[0]) + ',' + str(y1_n[1])+ ','+ str(y1_n[2])+ ';')
        g.write(str(y2_n[0]) + ',' + str(y2_n[1])+ ','+ str(y2_n[2])+ '\n')

        f.write('x0_n: ' + str(x0_n[0]) + ',' + str(x0_n[1])+ ','+ str(x0_n[2])+'\n')
        f.write('x1_n: ' + str(x1_n[0]) + ',' + str(x1_n[1])+ ','+ str(x1_n[2])+'\n')
        f.write('x2_n: ' + str(x2_n[0]) + ',' + str(x2_n[1])+ ','+ str(x2_n[2])+'\n')

        f.write('y0_n: ' + str(y0_n[0]) + ',' + str(y0_n[1])+ ','+ str(y0_n[2])+'\n')
        f.write('y1_n: ' + str(y1_n[0]) + ',' + str(y1_n[1])+ ','+ str(y1_n[2])+'\n')
        f.write('y2_n: ' + str(y2_n[0]) + ',' + str(y2_n[1])+ ','+ str(y2_n[2])+'\n\n')

    f.close()
    g.close()
    print("Calculo finalizado!")
    input("Presione Intro para continuar.")
    return main()
def main():
    global N, a, b, rate
    print(Fore.GREEN)
    print('''
     #############################################################################
     ############################························#########################
     ############################·········MENU···········#########################
     ############################························#########################
     #############################################################################

     Introduzca el código asociado a la opción del menu a las que desee acceder:

        -Ayuda ..........................................<Help>
        -Modificar PVI ..................................<Modify>
        -Cargar cálculos ................................<Setup>
        -Cargar simulación ..............................<Chaos>
        -Exit ...........................................<Exit>
            ''')
    print(Style.RESET_ALL)
    order = input("Introduzca código: ")

    order = order.upper()

    if order in ("H", "HELP"):
        Man()
    elif order in ("M", "MODIFY"):
        Modify()
    elif order in ("S", "SETUP"):
        Bosco()
    elif order in ("C", "CHAOS"):
        Brahma()
    elif order in ("E", "EXIT"):

        A = input('¿Desea cerrar el programa?(Y / N): ')
        A = A.upper()
        if A in ('Y', 'YES'):

            A = input('¿Seguro?(Y/N): ')
            A = A.upper()
            if A in ('N', 'NO'):
                pass
            elif A in ('Y', 'YES'):
                sys.exit()

        elif A in ('N', 'NO'):
            pass

    elif order in ("SUDO SU"):
        print(Fore.RED)
        conf = input("¿Desea modificar estos valores?(Yes/No)")
        print(Style.RESET_ALL)
        if conf in ("Yes", "yes"):
            print("N = ", N)
            x = input("Introduce nuevo valor: ")
            try:
                if int(x)<=0: return main()
                N = int(x)
            except:
                return main()

            print("a = ", a)
            x = input("Introduce nuevo valor: ")
            print("b = ", b)
            y = input("Introduce nuevo valor: ")
            try:
                y = float(y)
                x = float(x)
                if x>y: return main()
                if x<0 or y<=0: return main()
                a = x
                b = y
            except:
                return main()
            print("rate = ", rate)
            x = input("Introduce nuevo valor: ")
            try:
                if int(x)<=0: return main()
                rate = int(x)
            except:
                return main()


        else:
            os.system('cls' if os.name == 'nt' else 'clear')
        return main()


    else:
        print(Fore.RED)
        print("¡Error!  Orden no reconocida. Vuelva a intentarlo.")
        input("Presione Intro para continuar.")
        os.system('cls' if os.name == 'nt' else 'clear')


main()
