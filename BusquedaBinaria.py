"""
Divide y conquista
El problema se divide en 2 en cada iteracion
Siempre piensa en ¿Cuañ es el peor caso?
ASUME QUE LA LISTA ESTA ORDENADA

Si vas a utilizar muchas veces este algoritmo es preferible ordenar la lista
RETO: incluir un contador de iteraciones a la busqueda
"""
import random

def busqueda_binaria(lista, comienzo, final, objetivo,iter_bin=0):
    iter_bin+=1
    print(f'Estamos buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')#siempre que accedemos por indices, si viene de un "len" restar un "1" al ultimo valor de la lista
    #si el comienzo es mas grande que el final, termina el programa significa que el valor no esta en la lista
    if comienzo > final:
        return (False,iter_bin)
    #// = Division de enteros, no se toma en cuenta los decimales
    medio = (comienzo + final) // 2

    # si el valor seleccionado es el objetivo, termina la ejeucion
    if lista[medio] == objetivo:
        return (True,iter_bin)
    # si el valor seleccionado es menor al objetivo, este se convierte en el nuevo valor "comienzo" y vuelve a buscar a partir de ese valor
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo,iter_bin=iter_bin)
    else:
    # si el valor seleccionado es mayor al objetivo, este se convierte en el nuevo valor "final"
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo,iter_bin=iter_bin)

if __name__ == '__main__':
    list_size = int(input('De que tamaño es la lista? '))
    objetivo = int(input('¿Qué número quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(list_size)])

    (encontrado,iter_bin) = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones busqueda binaria: {iter_bin}')#cuantos pasos tardo la busqueda