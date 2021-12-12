"""
Algoritmos codiciosos
1-0-BagProblem
Tenemos una mochila con cupo maximo y de un conjunto de datos necesitamos saber cual combinacion de ell
de ellos nos otorga un valor mayor 

LOS DATOS NO SE PUEDEN DIVIDIR 
Los datos se pueden escoger o no
"""

def mochila(size, pesos, valores, n):
    #no quedan elementos o mochila llena
    if n== 0 or size== 0:
        print('pesos: ', pesos)
        print('tamaño: ',size)
        return 0
    #elemento a incluir pesa mas que el limite de la mochila
    if pesos[n-1]>size:
        print('pesos: ', pesos)
        print('tamaño: ',size)
        return mochila(size,pesos,valores,n-1)#se va al indice anterior con esta recursividad
    #puedo o no tomar el elemento
    #si me quedan elementos y espacio en la mochila, debe decidir si lo mete o no
    #lo va a meter si es el valor maximo
    #Si se mete el elemento, se debe reducir el espacio de la mochila, si no se mete solo revisa el siguiente elemento
    return max(valores[n-1] + mochila(size-pesos[n-1], pesos, valores, n-1),
                mochila(size,pesos,valores, n-1))


if __name__ == '__main__':
    valores = [60,100,120]
    pesos = [10,20,30]
    size = 25 #limite
    n = len(valores)

#valor maximo posible de las mezclas
    resultado = mochila(size, pesos,valores,n)
    print(resultado)