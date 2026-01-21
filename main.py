
from numpy.random import default_rng
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


print("1. Experimento inicial con a=20")
print("2. Experimento con diferentes valores de a")
print("3. Animación")
print("4. Análisis de las secciones disjuntas")

opcion = input("Selecciona una opción: ")



def experimento(x,y,a):
    """
    simular el lanzamiento de un punto con x de 40
    e y de 80.

    :param x: coordenada x del punto aleatorio
    :param y: coordenada y del punto aleatorio
    :param a: valor de a (radio del círculo y lado del cuadrado)
    """
    #Puede estar dentro del circulo, comprobar como en clase
    if((x-3*a)**2 + (y-a)**2 <= a**2):
       return 1
    #Puede estar dentro del cuadrado
    elif(x>a/2 and x<1.5*a and y>a/2 and y<1.5*a):
        return 2
    else:
        return 0


######################################################################################
#EXPERIMENTO INICIAL
######################################################################################


def experimentoInicial(): 
    N = int(1e7)    
    a = 20 #cm
    rng = default_rng(20) 

    x = rng.uniform(0, 4*a, size=N)
    y = rng.uniform(0, 2*a, size=N)

    # combinamos en un array de N filas y 2 columnas
    var_sto = np.column_stack((x, y))
    resultados = [experimento(var_sto[i, 0], var_sto[i, 1],a) for i in range(N)]

    n_circulo = sum(1 for r in resultados if r == 1)
    n_cuadrado = sum(1 for r in resultados if r == 2)
    pi_aprox = n_circulo / n_cuadrado

    print("Valor de aproximación de pi: ", pi_aprox)


######################################################################################
#ESTUDIAR EL EFECTO DEL PARÁMETRO a
######################################################################################

def estudiarParametroa():
    a = [2,5,10,11,15, 20]

    for a in a:    
        N = int(1e7)  

        rng = default_rng(20) 

        #Punto random que "caiga" entre los límites del rectangulo 
        x = rng.uniform(0, 80, size=N) 
        y = rng.uniform(0, 40, size=N)

        # combinamos en un array de N filas y 2 columnas
        var_sto = np.column_stack((x, y))
        resultados = [experimento(var_sto[i, 0], var_sto[i, 1],a) for i in range(N)]

        n_circulo = sum(1 for r in resultados if r == 1)
        n_cuadrado = sum(1 for r in resultados if r == 2)
        pi_aprox = n_circulo / n_cuadrado

        print("Valor de a:", a, " | Valor de pi:", pi_aprox)



######################################################################################
#GENERAR ANIMACIÓN
######################################################################################

def estimar_pi(N, a, seed=None):
    rng = default_rng(seed)
    x = rng.uniform(0, 40, size=N)
    y = rng.uniform(0, 80, size=N)

    n_circulo = 0
    n_cuadrado = 0

    for i in range(N):
        r = experimento(x[i], y[i], a)
        if r == 1:
            n_circulo += 1
        elif r == 2:
            n_cuadrado += 1

    return (n_circulo / n_cuadrado) if n_cuadrado > 0 else np.nan

def generarAnimacion():
    # --------- Parámetros ----------
    a = 10
    seed = 20
    n_max = 200_000
    step = 2_000
    interval_ms = 20

    # 1) Construir eje X (N) y eje Y (pi estimado)
    x = np.arange(step, n_max + 1, step)
    y = np.array([estimar_pi(n, a=a, seed=seed) for n in x])

    # 2) Filtrar valores no válidos
    mask = np.isfinite(y)
    x = x[mask]
    y = y[mask]

    # Si por algún motivo todo fueran valores no válidos, evitamos crash
    if len(x) == 0:
        raise ValueError("Todas las estimaciones han salido no válidas.")

    # 3) Plot base
    fig, ax = plt.subplots()
    line, = ax.plot(x[:1], y[:1], label="pi estimado")
    ax.axhline(np.pi, linestyle="--", label="pi real")

    ax.set(
        xlim=[0, x[-1]],
        ylim=[3.0, 3.3],
        xlabel="Repeticiones (N)",
        ylabel="Estimación de pi",
        title=f"Convergencia Monte Carlo (a={a})"
    )
    ax.legend()
    ax.grid(True)

    # 4) Animación
    def update(frame):
        line.set_xdata(x[:frame])
        line.set_ydata(y[:frame])
        return (line,)

    ani = FuncAnimation(fig=fig, func=update, frames=len(x) + 1, interval=interval_ms, blit=True)

    # Guarda GIF
    ani.save("pi_convergencia.gif")
    # plt.show()


######################################################################################
#ANÁLISIS DE LAS SECCIONES NO DISJUNTAS
######################################################################################


######################################################################################
#¿DEBEN SER LAS SECCIONES DISJUNTAS?
######################################################################################

def checkForPointInside(x,y,a):

    #Defino el cuadrado, centrado en el punto (a,a)
    squareArea = (x>a/2 and x<1.5*a and y>a/2 and y<1.5*a)

    #Defino el círculo, desplazado ligeramente para generar una intersección entre ambos
    circleArea = ((x - 1.5*a)**2 + (y - a)**2 <= a**2)

    return (1 if circleArea else 0) + (2 if squareArea else 0)

def randomPointInSurface(rng, N):
    x = rng.uniform(0, 80, size=N) 
    y = rng.uniform(0, 40, size=N)

    return np.column_stack((x, y))

def analisisDisjuntas():
    aValues = [2,5,10,15]    
    N = int(1e7) 
    seed = default_rng(20)

    for a in aValues:    

        surface = randomPointInSurface(seed, N)
        results = list(map(lambda v: checkForPointInside(v[0], v[1], a), surface))

        results = np.array(results)

        Ecircle = np.sum(results == 1)
        Esquare = np.sum(results == 2)
        Eintersection = np.sum(results ==3)

        piValue = (Ecircle+ Eintersection) / (Esquare + Eintersection)
        print("Para a = ",a, " contando la intersección para ambos, pi:" ,piValue)

        piValue = (Ecircle) / (Esquare)
        print("Para a = ",a, " excluyendo la interseccion para el círculo, pi:" ,piValue)

    print("")
    print("---------------------- JUSTIFICACION ----------------------")
    print("La justificación más precisa es que depende. Existen dos casos:")
    print("En el caso de que no sean disjuntos, y las pelotas que entren en " \
    " la intersección de ambas áreas cuenten como contenidas tanto en una como en " \
    "otra, la proporción real de las áreas se mantiene intacta, haciendo que la " \
    "estimación sea consistente ")
    print("Sin embargo, en el caso de que no sean disjuntos y las pelotas que entren en " \
    " la intersección de ambas áreas  no cuenten como contenidas en ninguna, establecería " \
    "un sesgo muy grande en favor al círculo, porque el cuadrado comprende más porcentaje de " \
    "su área en la intersección, aumentando el valor de pi de forma artificial")

if opcion == "1":
    experimentoInicial()
elif opcion == "2":
    estudiarParametroa()
elif opcion == "3":
    generarAnimacion()
elif opcion == "4":
    analisisDisjuntas()
else:
    print("Opción no válida")
