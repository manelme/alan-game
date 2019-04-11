# coding: utf-8
import unittest
from personaje import Personaje
from asesino import Asesino
from subterfujio import Subterfujio

class Asesino_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando la clase Guerrero")
    
        self.asesinoA = Asesino("Ezio")
        self.asesinoB = Asesino("Altair")
        
    def test_personaje_name(self):
        self.assertEqual(self.asesinoA.nombre, 'Ezio')
        self.assertNotEqual(self.asesinoA.nombre, 'Altair')
        
    def test_comprobar_vida(self):
        self.asesinoA.modificar_vida_total(50)
        self.assertEqual(self.asesinoA.vida_total, 120)
        self.asesinoA.modificar_vida(30)
        self.assertEqual(self.asesinoA.vida_restante, 100)
        self.asesinoA.modificar_vida(50)
        self.assertEqual(self.asesinoA.vida_restante, 120)
        self.asesinoB.modificar_vida_total(-50)
        self.asesinoB.modificar_vida(10)
        self.assertEqual(self.asesinoB.vida_restante, 20)

    def test_comprobar_furia(self):
        self.asesinoA.modificar_energia_total(50)
        self.assertEqual(self.asesinoA.energia_total, 150)
        self.asesinoA.modificar_energia(30)
        self.assertEqual(self.asesinoA.energia_restante, 130)
        self.asesinoA.modificar_energia(50)
        self.assertEqual(self.asesinoA.energia_restante, 150)
        self.asesinoB.modificar_energia_total(-50)
        self.asesinoB.modificar_energia(10)
        self.assertEqual(self.asesinoB.energia_restante, 50)

    def test_add_fisica(self):
        self.asesinoA.add_habilidad(Subterfujio("Hola", 20, 15))
        self.assertEqual("Hola", self.asesinoA.habilidades[0].nombre)

if __name__ == '__main__':
    unittest.main()