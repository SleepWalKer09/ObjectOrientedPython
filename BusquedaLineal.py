"""
Busca en todos los elementos de manera secuencial
Siempre piensa en: ¿Cual es el peor caso?
"""
import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break #aunque esta el break no afecta la complejidad algoritmica
    
    return match


if __name__ == '__main__':
    list_size = int(input('¿De que tamaño sera la lista?'))
    objetivo = int(input('¿Que numero quieres encontrar?'))
    lista = [random.randint(0,100) for i in range(list_size)]

    encontrado = busqueda_lineal(lista,objetivo)
    print(lista)
    print(f'El elemento {objetivo} {" esta" if encontrado else "no esta"} en la lista')