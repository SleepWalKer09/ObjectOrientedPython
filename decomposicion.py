#La decomposición en python significa dividir un problema en problemas más pequeños.
#Las clases permiten crear mayores abstracciones en forma de componentes.
#Cada clase se encarga de una parte del problema y el programa se vuelve más fácil de mantener.

#Para realizar un ejemplo de decomposición modelaremos un automóvil.
class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.modelo = marca
        self.color = color
        self.estado = 'en_reposo'
        self.motor = Motor(cilindros = 4)
    
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        self.estado = 'en_movimiento'

class Motor:
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindroas = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass
