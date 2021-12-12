"""
Algoritmo que recorre repetidamente una lista que necesita ordenarse. compara elementos adyacentes y los intercambia si estan en el orden incorrecto.
Este procedimiento no se repite hasta que no se requieran mas intercambios, lo que se indica que la lista esta ordenada

Se recorrera la lista cada vez por cada elemento que vive en la lista

Excelente con pocos registros, en caso de listas muy grandes este algoritmo puede tener un costo computacional muy grande
"""
import random

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
 # n=TamañoLista i=Recorrido -1= estamos tomando la longitud y se accedera por indices
        for j in range(0, n-i-1): # O(n) * O(n) = O(n * n) = 0(n**2) ---> Complejidad elementos
            if lista[j] > lista[j+1]:
                #intercambio de elementos de la lista
                lista[j],lista[j+1] = lista[j+1],lista[j]
    return lista

if __name__ == '__main__':
    size = int(input("Tamaño de la lista:"))
    lista = [random.randint(0,100) for i in range(size)]
    print(lista)

    lista_ordenada = bubble_sort(lista)
    print(lista_ordenada)
