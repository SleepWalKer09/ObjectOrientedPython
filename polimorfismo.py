#Describe el concepto de que objetos de diferentes tipos pueden ser accedidos a través de la misma interfaz
#Habilidad de tomar varias formas
#Python permite cambiar el comportamiento de una superclase para adaptarlo a la subclase

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')
   
#Clase con polimorfismo con Persona como superclase
class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print("Ando moviendome en mi bicicleta")

def main():
    persona = Persona('Chris')
    persona.avanza()

    ciclista = Ciclista('Luis')
    ciclista.avanza()

if __name__ == '__main__':
    main()