# coding: UTF-8

import unittest
from personaje import Personaje
from mago import Mago
from magia import Magia
from fisica import Fisica

class Personaje_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando test de la clase Mago")
    
        self.personajeA = Mago("Fuelle carcomido por la veheméncia")
        self.personajeB = Mago("Fermín")
        
    def test_personaje_name(self):
        self.assertEqual(self.personajeA.nombre, 'Fuelle carcomido por la veheméncia')
        self.assertNotEqual(self.personajeB.nombre, 'Fuelle carcomido por la veheméncia')

    def test_add_magia(self):
        self.personajeA.add_habilidad(Magia("Bola de fuego", 10, 20))
        self.assertEqual("Bola de fuego", self.personajeA.habilidades[0].nombre)
        self.assertRaises(self.personajeB.add_habilidad(Fisica("Eviscerar", 20, 30)), )

if __name__ == '__main__':
    unittest.main()