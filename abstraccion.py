#la POO permite visualizar el objeto, entender como funciona e implementar los metodos para que funcione 
#tener en cuenta que cosas del codigo seran privadas o publicas

#Reto: programar una lavadora
class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura = 'caliente'):
       #Metodo PUBLICO para llamar a otros metodos PRIVADOS para el proceso de lavado de ropa
        self._llenar_tanque_de_agua(temperatura)
        self._agregar_jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua{temperatura}')
    
    def _agregar_jabon(self):
        print('Agregando jabon')

    def _lavar(self):
        print('Lavando la ropa')
    
    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__ == '__main__':
    Lavadora = Lavadora()
    Lavadora.lavar()