"""
Se basa en el flujo del programa
Prueba todos los caminos posibles de una funcion. (Ramificaciones, bucles for y while, recursion)
Regresion Testing o mocks
"""

import unittest
from unittest import result

def mayoriaEdad(edad):
    if edad >=18:
        return True
    else:
        return False

        
class PruebaCristalTest(unittest.TestCase):
    def testEdadMayor(self):
        edad=20
        resultado = mayoriaEdad(edad)
        self.assertEqual(resultado, True)#se verifica que el resultado sea igual a True

    def testEdadMenor(self):
        edad=15
        resultado = mayoriaEdad(edad)
        self.assertEqual(resultado, False)

if __name__ == "__main__":
    unittest.main()