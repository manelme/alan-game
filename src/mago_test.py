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

    def test_comprobar_vida(self):
        self.personajeA.modificar_vida_total(20)
        self.assertEqual(self.personajeA.vida_total, 100)
        self.personajeA.modificar_vida(10)
        self.assertEqual(self.personajeA.vida_restante, 90)
        self.personajeA.modificar_vida(20)
        self.assertEqual(self.personajeA.vida_restante, 100)
        self.personajeB.modificar_vida_total(-50)
        self.personajeB.modificar_vida(10)
        self.assertEqual(self.personajeB.vida_restante, 30)

    def test_comprobar_mana(self):
        self.personajeA.modificar_mana_total(50)
        self.assertEqual(self.personajeA.mana_total, 150)
        self.personajeA.modificar_mana(30)
        self.assertEqual(self.personajeA.mana_restante, 130)
        self.personajeA.modificar_mana(50)
        self.assertEqual(self.personajeA.mana_restante, 150)
        self.personajeB.modificar_mana_total(-50)
        self.personajeB.modificar_mana(10)
        self.assertEqual(self.personajeB.mana_restante, 50)

    def test_add_magia(self):
        self.personajeA.add_habilidad(Magia("Bola de fuego", 10, 20))
        self.assertEqual("Bola de fuego", self.personajeA.habilidades[0].nombre)
        #self.assertRaises(self.personajeB.add_habilidad(Fisica("Eviscerar", 20, 30)), )

if __name__ == '__main__':
    unittest.main()