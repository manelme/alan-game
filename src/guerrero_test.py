# coding: utf-8
import unittest
from personaje import Personaje
from guerrero import Guerrero
from fisica import Fisica

class Guerrero_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando la clase Guerrero")
    
        self.guerreroA = Guerrero("Dante")
        self.guerreroB = Guerrero("Saria")
        
    def test_personaje_name(self):
        self.assertEqual(self.guerreroA.nombre, 'Dante')
        self.assertNotEqual(self.guerreroB.nombre, 'Dante')

    def test_add_fisica(self):
        self.guerreroA.add_habilidad(Fisica("Golpe", 50, 15))
        self.assertEqual("Golpe", self.guerreroA.habilidades[0].nombre)

if __name__ == '__main__':
    unittest.main()