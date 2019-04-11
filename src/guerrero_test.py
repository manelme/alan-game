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
        
    def test_comprobar_vida(self):
        self.guerreroA.modificar_vida_total(50)
        self.assertEqual(self.guerreroA.vida_total, 150)
        self.guerreroA.modificar_vida(30)
        self.assertEqual(self.guerreroA.vida_restante, 130)
        self.guerreroA.modificar_vida(50)
        self.assertEqual(self.guerreroA.vida_restante, 150)
        self.guerreroB.modificar_vida_total(-50)
        self.guerreroB.modificar_vida(10)
        self.assertEqual(self.guerreroB.vida_restante, 50)

    def test_comprobar_furia(self):
        self.guerreroA.modificar_furia_total(50)
        self.assertEqual(self.guerreroA.furia_total, 150)
        self.guerreroA.modificar_furia(30)
        self.assertEqual(self.guerreroA.furia_restante, 130)
        self.guerreroA.modificar_furia(50)
        self.assertEqual(self.guerreroA.furia_restante, 150)
        self.guerreroB.modificar_furia_total(-50)
        self.guerreroB.modificar_furia(10)
        self.assertEqual(self.guerreroB.furia_restante, 50)

    def test_add_fisica(self):
        self.guerreroA.add_habilidad(Fisica("Golpe", 50, 15))
        self.assertEqual("Golpe", self.guerreroA.habilidades[0].nombre)

if __name__ == '__main__':
    unittest.main()