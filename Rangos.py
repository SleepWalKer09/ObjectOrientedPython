"""
Representan una secuencia de enteros

sintaxis: range(comienzo,fin,pasos)

Al igual que las cadenas y las tuplas los rangos sin inmutables

Muy eficientes en el uso de memoria y normalmente utilizados en for loops
"""

my_range = range(0,7, 2)
my_range2 = range(0,8, 2)
my_range == my_range2

#Nos regresan la misma lista de valores
for i in my_range:
    print(i)
for i in my_range2:
    print(i)

#Tienen los mismos valores pero NO SON EL MISMO OBJETO
#Revisar object equiality
my_range is my_range2


#lista del 0 al 101 con numeros pares
for i in range(0,101,2):
    print(i)

#lista del 1 al 99 con numeros inpares
for i in range(1,100,2):
    print(i)