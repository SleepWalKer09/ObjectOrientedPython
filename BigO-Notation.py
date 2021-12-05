# NO IMPORTAN VARIABLES PEQUEÑAS
# El enfoque se centra en lo que pase conforme el tamaño del problema se acerca al inifito
# Pensar en el mejor de los casos, promedio, peor de los casos
# Nada mas importa el termino de mayot tamaño
# Existe el Big O Omega que mide el mejor caso y el caso promedio

# El PEOR CASO es el mejor indicador para saber la carga computacional del algoritmo
# EL BIG O mide el péor de los casos

# Un loop => crecimiento lineal.
# Un loop dentro de otro => crecimiento cuadratico
# Llamadas recursivas => crecimiento exponecncial.

# Existen distintos tipos de complejidad algorítmica:
#     1. O(1) Constante: no importa la cantidad de input que reciba, siempre demorara el mismo tiempo.
#     2. O(n) Lineal: la complejidad crecerá de forma proporcional a medida que crezca el input.
#     3. O(log n) Logarítmica: nuestra función crecerá de forma logarítmica con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabilizara.
#     4. O(n log n) Log lineal: crecerá de forma logarítmica pero junto con una constante.
#     5. O(n²) Polinomial: crecen de forma cuadrática. No son recomendables a menos que el input de datos en pequeño.
#     6. O(2^n) Exponencial: crecerá de forma exponencial, por lo que la carga es muy alta. Para nada recomendable en ningún caso, solo para análisis conceptual.
#     7. O(n!) Factorial: crece de forma factorial, por lo que al igual que el exponencial su carga es muy alta, por lo que jamas utilizar algoritmos de este tipo.

#Codigo para demostrar el tiempo de ejeucion de cada complejidad algoritmica 

# -*- coding: utf-8 -*-
import math
import time 

class Complejidad_algoritmica:
	def __init__(self, n):
		self.n = n

	def constante(self):
		return 1

	def logaritmica(self):
		return math.log10(self.n)

	def lineal(self):
		return self.n

	def log_lineal(self):	
		return self.n * math.log10(self.n)

	def	polinomial(self):
		return self.n**2

	def	exponencial(self):
		return 2**self.n


def main():
	
    nums = [1, 10, 100, 1000, 10000]
    
    for n in nums:
        
        complejidad = Complejidad_algoritmica(n)
        
        print('n es igual a: {}'.format(n))
        
        principio = time.time()
        print(f'El resultado de complejidad constante para n igual a {n} es: ', complejidad.constante())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad logaritmica para n igual a {n} es: ', complejidad.logaritmica())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad lineal para n igual a {n} es: ', complejidad.lineal())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad logaritmica lineal para n igual a {n} es: ', complejidad.log_lineal())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad polinomial para n igual a {n} es: ', complejidad.polinomial())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
       
        principio = time.time()
        print(f'El resultado de complejidad exponencial para n igual a {n} es: ', complejidad.exponencial())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        print('\n\n')
        
	    

if __name__ == '__main__':
    
    main()