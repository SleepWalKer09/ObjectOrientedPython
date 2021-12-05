#La encapsulacion permite agrupar datos y su comportamientos
#controla el acceso a esos datos
#previene modificaciones no autorizadas

#getters --> implementacion mediante add.properties o el decorador de propuedades
#setters --> implementacion definiendo el nombre de la propiedad a ejecutar para el setter con .setter con denotacion de decorador
#con getters y setters podemos determinar cuando y como se acceden o modifican estas variables

#Ejemplo de encapsulacion usando getters y setters
class House:

    def __init__(self,price):
        self._price = price
    # price como variable privada, generamos sus set/get/del
# =============================================
    # definimos la property price y el getter
    @property
    def price(self):
        return self._price
    
# =============================================
    # setter method
    @price.setter
    def price(self,new_price):
        if new_price < 0 or not isinstance(new_price, float):
            raise ValueError("price cannot be negative and must be a float number")

        self._price = new_price
# =============================================
    # deleter method
    @price.deleter
    def price(self):
        del self._price

my_house = House(100)

print(my_house.price) # 100
my_house.price = 200.0
print(my_house.price) # 200.0
del my_house.price