# coding: UTF-8

import unittest
from fisica import Fisica

class Fisica_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando test de la clase Fisica")
    
        self.fisicaA = Fisica("Testarazo",10,15)
        self.fisicaB = Fisica("Golpe certero",20,25)
        
    def test_fisica_name(self):
        self.assertEqual(self.fisicaA.nombre, 'Testarazo')
        self.assertNotEqual(self.fisicaB.nombre, 'Testarazo')
    
    def test_fisica_danyo(self):
        self.assertEqual(self.fisicaA.danyo, 10)
        self.assertEqual(self.fisicaB.danyo, 20)
    
    def test_fisica_coste(self):
        self.assertEqual(self.fisicaA.coste_furia, 15)
        self.assertEqual(self.fisicaB.coste_furia, 25)

if __name__ == '__main__':
    unittest.main()