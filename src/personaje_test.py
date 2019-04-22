# coding: UTF-8

import unittest
from personaje import Personaje

class Personaje_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando test de la clase Persona")
    
        self.personajeA = Personaje("Paco", 100, 100)
        self.personajeB = Personaje("Fermín", 100, 100)
        
    def test_personaje_name(self):
        self.assertEqual(self.personajeA.nombre, 'Paco')
        self.assertNotEqual(self.personajeB.nombre, 'Paco')

    def test_comprobar_valores_inicio(self):
        self.assertEqual(self.personajeA.nivel, 1)
        self.assertEqual(self.personajeA.porcentaje_de_nivel, 0)
        self.assertEqual(self.personajeA.elo, 1200)

if __name__ == '__main__':
    unittest.main()