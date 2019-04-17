# coding: UTF-8

import unittest
from personaje import Personaje

class Personaje_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando test de la clase Persona")
    
        self.personajeA = Personaje("Paco")
        self.personajeB = Personaje("Fermín")
        
    def test_personaje_name(self):
        self.assertEqual(self.personajeA.nombre, 'Paco')
        self.assertNotEqual(self.personajeB.nombre, 'Paco')

if __name__ == '__main__':
    unittest.main()