#Herencia permite modelar jerarquia de clases
#Permite compartir comportamiento comun en la jerarquia
#Al padre se le conoce como superclase y al hijo como subclase
#Posibilidad de reutilizar codigo.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
class Cuadrado(Rectangulo):
    def __init__(self,lado):
        #super --> permite obtener referencia de la superclase (rectangulo)
        #llamamos al constructor de rectangulo
        super().__init__(lado,lado)

#Si este es el archivo que se ejecuta desde consola
if __name__ == '__main__':
    rectangulo = Rectangulo(base=3,altura=4)
    print("area rectangulo: ",rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print("area cuadrado: ",cuadrado.area())