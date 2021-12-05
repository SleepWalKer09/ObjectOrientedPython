#Complejidad temporal vs espacial
#Definida como T(n)
#Cronometrar el tiempo en el que corre un algoritmo
#Contar los pasos con una medida abstracta de operacion
#Contar los pasos conforme nos aproximamos al infinito

import time

def factorial(n):
    respuesta = 1

    while n>1:
        respuesta *= n
        n -= 1
    return respuesta

def factorial_r(n):
    if n==1:
        return 1
    else:
        return n*factorial_r(n-1)

if __name__ == '__main__':
    n = 200000
    #medir tiempo de factorial
    comienzo = time.time()
    #print(factorial(n))
    final = time.time()
    print("factorial; ", final - comienzo)
    #medir tiempo de factorial recursivo
    comienzo = time.time()
    #print(factorial_r(n))
    final = time.time()
    print("factorial recursivo: ",final-comienzo)
