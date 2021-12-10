#Algoritmica
#Forma de crear soluciones usando el principio de "divide y venceras"
#Programatica
#Una tecnica programatica mediante la cual una funcion se llama a si misma

#python tiene un limite de recursividad
import sys
print("limite de recursividad", sys.getrecursionlimit())

#se ejecuta la cantidad de veces iguales al input
def factorial(n):
    """Calcula el factorial de n
    n int > 0
    returns n!    
    """
    print(n)
    if n == 1:
        return 1
    
    return n * factorial(n-1)

n = int(input("Escribe un entero: "))

print(factorial(n))
