
from numpy.random import default_rng
import numpy as np

# def experimento(x,y,a):
#     """
#     simular el lanzamiento de un punto con x de 0 a 4a
#     e y de 0 a 2a de forma totalmente aleatoria

#     :param rng: generador de numero aleatorios
#     """

#     if(x>2*a):
#         #Puede estar dentro del circulo, comprobar como en clase
#         if((x-3*a)**2 + (y-a)**2 <= a**2):
#             return 1 
#         else:
#             return 0
#     else:
#         #Comprobar si esta dentro del cuadrado
#         if(x>a/2 and x<1.5*a and y>a/2 and y<1.5*a):
#             return 2
#         else:
#             return 0
    
# N = int(1e8)    
# a = 20 #cm
# rng = default_rng(20) 

# x = rng.uniform(0, 4*a, size=N)
# y = rng.uniform(0, 2*a, size=N)

# # combinamos en un array de N filas y 2 columnas
# var_sto = np.column_stack((x, y))
# resultados = [experimento(var_sto[i, 0], var_sto[i, 1],a) for i in range(N)]

# n_circulo = sum(1 for r in resultados if r == 1)
# n_cuadrado = sum(1 for r in resultados if r == 2)
# pi_aprox = n_circulo / n_cuadrado



# print("Valor de pi: ", pi_aprox)

######################################################################################
#ESTUDIAR EL EFECTO DEL PARÁMETRO a
######################################################################################

def experimento2(x,y,a):
    """
    simular el lanzamiento de un punto con x de 40
    e y de 80.

    :param rng: generador de numero aleatorios
    """
    #Puede estar dentro del circulo, comprobar como en clase
    if((x-3*a)**2 + (y-a)**2 <= a**2):
       return 1
    #Puede estar dentro del cuadrado
    elif(x>a/2 and x<1.5*a and y>a/2 and y<1.5*a):
        return 2
    else:
        return 0

a = [2,5,10,11,15]

for a in a:    
    N = int(1e7)  

    rng = default_rng(20) 

    #Punto random que "caiga" entre los límites del rectangulo 
    x = rng.uniform(0, 40, size=N) 
    y = rng.uniform(0, 80, size=N)

    # combinamos en un array de N filas y 2 columnas
    var_sto = np.column_stack((x, y))
    resultados = [experimento2(var_sto[i, 0], var_sto[i, 1],a) for i in range(N)]

    n_circulo = sum(1 for r in resultados if r == 1)
    n_cuadrado = sum(1 for r in resultados if r == 2)
    pi_aprox = n_circulo / n_cuadrado

    print("Valor de pi: ", pi_aprox)

