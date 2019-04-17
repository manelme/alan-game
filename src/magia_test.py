# coding: UTF-8

import unittest
from magia import Magia

class Magia_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando test de la clase Magia")
    
        self.magiaA = Magia("Bola de fuego",10,15)
        self.magiaB = Magia("Tormenta de escarcha",20,25)
        
    def test_magia_name(self):
        self.assertEqual(self.magiaA.nombre, 'Bola de fuego')
        self.assertNotEqual(self.magiaB.nombre, 'Bola de fuego')
    
    def test_magia_danyo(self):
        self.assertEqual(self.magiaA.danyo, 10)
        self.assertEqual(self.magiaB.danyo, 20)
    
    def test_magia_coste(self):
        self.assertEqual(self.magiaA.coste_mana, 15)
        self.assertEqual(self.magiaB.coste_mana, 25)

if __name__ == '__main__':
    unittest.main()