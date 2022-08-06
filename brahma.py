import vpython as vp
from colorama import Fore, Style

def Brahma():
    rate = 3000
    Rsun = 2E9 #Radio solar
    L = 4e10 #Factor para distancias
    # NOTE: Ajustes de la escena
    vp.scene.width = vp.scene.height = 900 #Dimensiones de la pantalla
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
        body = vp.sphere(pos = q0[i], make_trail = True, retain = 300,
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
                #body.pos = L*vp.vec(float(aux1[i][0]), float(aux1[i][1]), float(aux1[i][2]))
                body.pos = vp.vec(float(aux1[i][0]), float(aux1[i][1]), float(aux1[i][2]))
                i+=1
            except:
                print('End')
                return 0

    data.close()
