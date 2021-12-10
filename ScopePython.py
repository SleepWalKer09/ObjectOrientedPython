#Scope: Contexto al que pertenece una variable en python
###############
#Scope Global:#
###############
#  Crear una variable en el cuerpo principal del codigo de python, SE PUEDE USAR EN CUALQUIER PARTE
x = "Soy una variable global"
def funcion():
    print(x)
funcion()
print(x)
#Se puede crear una variable local con el mismo nombre de una variable global, pero pythonlo leera como 2 variables distintas
x="Soy una variable global"
def funcion():
    x="Y yo tambien soy una variable global"
    print(x)
funcion()
print(x)


###############
#Scope Local: #
###############
# Si creas una variable dentro de una funcion, ESTA PERTENECE SOLO A ESA FUNCION
def funcion():
    x= "Soy una variable local"
    print(x)
funcion()

#Tambien puedes usar la variable en una funcion dentro de otra funcion
def funcion():
    x= "esta es una variable local"
    
    def funcion_interior():
        print(x)
    funcion_interior
funcion()


##################
#Keyword Global: #
##################
# Se puede crear una variable global dentro de una funcion el Kkeyword "global"
def funcion():
    global x
    x = "Soy una variable global"
funcion()
print(x)

# Se puede cambiar el valor de una variable global con este keyword
x = "Esta es una variable global"
def funcion():
    global x
    x = "Y ahora cambiamos su valor"
funcion()
print(x)