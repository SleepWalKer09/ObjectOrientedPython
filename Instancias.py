# 
class Coordenada:
    def __init__(self, x , y):
        self.x = x
        self.y = y

#el parametro otra_coordenada es una instancia,
#que hara uso del molde en la primer clase de inicializacion,
#la cual usaremos despues, tomar atencion.    
    def distancia(self, otra_coordenada):
        x_diff =(self.x - otra_coordenada.x) **2
        y_diff =(self.y - otra_coordenada.y) **2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
#estas dos expresiones son instancias que usan el molde que es el primer método de inicializacion.
    coord1 = Coordenada(3,30)
    coord2 = Coordenada(4,8)

    print(coord1.distancia(coord2))