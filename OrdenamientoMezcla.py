"""
El ordenamiento por mezcla es un algoritmo de divide y conquista
Primero divide una lista en partes iguales hasta que quedan sublistas de 1 a 0 elementos. Luego las recombina en forma ordenada

Pasos:
1. Una lista desordenaba, se va diviendo a la mitad hasta que solo quedan sublistas de 1 o 0 elementos
2. Se hace una comparacion entre las sublistas adyacentes (e.g sublista[1] y sublista[2])
3. Si el primer valor es menor, se MEZCLA e intercambia posicion con el segundo creando una sublista de 2 elementos, asi hasta terminar la lista
4. Toma el primer valor de la primer sublista y lo compara contra los valores de la segunda sublista ordenandolos en otra lista diferente
5. Se compara el primer valor de la segunda sublista contra el segundo valor de la misma sublista(que ya esta ordenado) y se inserta donde corresponda
6. Continua con el paso 5 hasta que solo quede un valor por revisar que por default sera el valor mas grande de la lista}
"""
from math import degrees
import random
#Ordenamiento recursivo, crecimiento logaritmico
def ordenamiento_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista)//2
        izq = lista[:medio]
        der = lista[medio:]
        print(izq, '*'* 5, der)
        #LLamado recursivo en cada mitad
        ordenamiento_mezcla(izq)
        ordenamiento_mezcla(der)
        #Iteraciones para recorrer las sublistas
        i= 0
        j= 0
        #iterador de lista principal
        k=0

        #mientras i sea menor a la longitud del valor izquierdo y j menor a la longitud del valor derecho
        while i< len(izq) and j<len(der):
        #si la izquierda en el indice I es menor a la derecha en el indice J    
            if izq[i]< der[j]:
                lista[k] = izq[i]
                i+=1
            else:#derecha mas grande que la izquierda
                lista[k] = der[j]
                j+=1
            k+=1
        #ambos whiles pasan directo los valores que sobran
        while i < len(izq):
            lista[k] = izq[i]
            i+=1
            k+=1
        while j <len(der):
            lista[k] = der[j]
            j+=1
            k*=1
        print(f'Izquierda {izq}, Derecha {der}')
        print(lista)
        print('-'*50)

    return lista


if __name__ == '__main__':
    size = int(input('De que tamaño sera la lista'))

    lista = [random.randint(0,100) for i in range(size)]
    print(lista)
    print('-'*20)

    lista_ordenada = ordenamiento_mezcla(lista)
    print(lista_ordenada)