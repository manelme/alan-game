# coding: UTF-8

import unittest
from personaje import Personaje

class Personaje_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando test de la clase Instituto")
    
        self.personajeA = Personaje("Fuelle carcomido por la veheméncia")
        self.personajeB = Personaje("Fermín")
        
    def test_personaje_name(self):
        self.assertEqual(self.personajeA.nombre, 'Fuelle carcomido por la veheméncia')
        self.assertNotEqual(self.personajeB.nombre, 'Fuelle carcomido por la veheméncia')

if __name__ == '__main__':
    unittest.main()