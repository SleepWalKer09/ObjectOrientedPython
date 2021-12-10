"""
Tuplas 

son secuencias inmutables de objetos

A diferencia de las cadenas pueden contener cualquier tipo de objetos

Pueden utilizarse para devolver varios valores en una funcion
"""

#creacion de una tupla vacia
my_tuple = ()
print(type(my_tuple))

my_tuple = (1, 'dos' , True)

#se puede acceder a las duplas por el index
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

#no se pueden modificar las tuplas, provoca error
# my_tuple[0] = 2

#no se pueden modificar pero si pueden apuntar a otro lugar de memoria
my_tuple = (1)

#tipo de objeto int debido a que no se uso sintaxis adecuada
print(type(my_tuple))

#los items deberan estar separados por comas
my_tuple = (1,)
print(type(my_tuple))

#tuplas pueden sumarse
#la variable no se modifica, apunta a otro lugar de memoria
my_other_tuple = (2,3,4)
my_tuple += my_other_tuple
print(my_tuple)

#se pueden asignar los items de las tuplas a otras variables
x, y, z = my_other_tuple
print (x,y,z)

#se pueden asignar el retorno de las funciones a una tupla
def coordenadas():
    return(5,4)

coordenada = coordenadas()
print(coordenada)

#asignar los items de la tupla a variables x y
x , y = coordenada

print(x, y)