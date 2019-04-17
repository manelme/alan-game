# coding: utf-8
import unittest
from personaje import Personaje
from guerrero import Guerrero
from fisica import Fisica

class Guerrero_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando la clase Guerrero")
    
        self.guerreroA = Guerrero("Aquiles")
        self.guerreroB = Guerrero("Garrosh")
        
    def test_personaje_name(self):
        self.assertEqual(self.guerreroA.nombre, 'Aquiles')
        self.assertNotEqual(self.guerreroB.nombre, 'Aquiles')
        
    def test_comprobar_vida_restante(self):

        self.assertEqual(self.guerreroA.vida_restante, 70)

        self.guerreroA.modificar_vida(-50)
        self.assertEqual(self.guerreroA.vida_restante, 20)
        self.guerreroA.modificar_vida(30)
        self.assertEqual(self.guerreroA.vida_restante, 50)

        self.guerreroA.modificar_vida(30)
        self.assertNotEqual(self.guerreroA.vida_restante, 80)
        
        with self.assertRaises(Exception) as context:
            self.guerreroA.modificar_vida(-200)
        self.assertTrue(context, "El personaje a muerto" )
        self.assertEqual(self.guerreroA.vida_restante, 0)

    def test_comprobar_vida_total(self):
        
        self.assertEqual(self.guerreroA.vida_total, 70)

        self.guerreroA.modificar_vida_total(70)
        self.assertEqual(self.guerreroA.vida_total, 140)
        self.guerreroA.modificar_vida_total(-50)
        self.assertEqual(self.guerreroA.vida_total, 90)

        with self.assertRaises(Exception) as context:
            self.guerreroA.modificar_vida_total(-130)
        self.assertTrue(context, "El personaje a muerto" )

    def test_comprobar_vida_restante_total(self):
        
        with self.assertRaises(Exception) as context:
            self.guerreroA.modificar_vida_total(-130)
        self.assertTrue(context, "El personaje a muerto" )

        self.guerreroA.modificar_vida_total(70)
        self.assertEqual(self.guerreroA.vida_total, 70)
        self.guerreroA.modificar_vida(100)
        self.assertEqual(self.guerreroA.vida_restante, 70)

    def test_comprobar_furia(self):

        self.assertEqual(self.guerreroA.furia_restante, 100)
       
        self.guerreroA.modificar_furia(-15)
        self.assertEqual(self.guerreroA.furia_restante, 85)
        self.guerreroA.modificar_furia(40)
        self.assertEqual(self.guerreroA.furia_restante, 100)

        with self.assertRaises(Exception) as context:
            self.guerreroA.modificar_furia(-130)
        self.assertTrue(context, "No queda furia" )
        self.assertEqual(self.guerreroA.furia_restante, 0)

    def test_comprobar_furia_total(self):

        self.assertEqual(self.guerreroA.furia_total, 100)
        
        self.guerreroA.modificar_furia_total(-10)
        self.assertEqual(self.guerreroA.furia_total, 90)
        self.guerreroA.modificar_furia_total(100)
        self.assertEqual(self.guerreroA.furia_total, 190)

        with self.assertRaises(Exception) as context:
            self.guerreroA.modificar_furia_total(-200)
        self.assertTrue(context, "No queda furia" )
        self.assertEqual(self.guerreroA.furia_total, 0)

    def test_comprobar_furia_restante_total(self):
        
        with self.assertRaises(Exception) as context:
            self.guerreroA.modificar_furia_total(-130)
        self.assertTrue(context, "No queda furia" )

        self.assertEqual(self.guerreroA.furia_total, 0)
        self.assertEqual(self.guerreroA.furia_restante, 0)

        self.guerreroA.modificar_furia_total(70)
        self.guerreroA.modificar_furia(120)
        self.assertEqual(self.guerreroA.furia_restante, 70)


    def test_add_fisica(self):
        self.guerreroA.add_habilidad(Fisica("Testarazo", 50, 15))
        self.assertEqual("Testarazo", self.guerreroA.habilidades[0].nombre)
        with self.assertRaises(Exception) as context:
            self.guerreroA.add_habilidad(Magia("Bola de fuego", 50, 15))
        self.assertTrue(context, "La habilidad tiene que ser de tipo fisica" )
    
    def test_atacar(self):
        self.guerreroA.add_habilidad(Fisica("Testarazo", 50, 50))
        
        self.guerreroA.atacar(self.guerreroB, self.guerreroA.habilidades[0])
        self.assertEqual(self.guerreroB.vida_restante,20)
        self.assertEqual(self.guerreroA.furia_restante,50)
        
        with self.assertRaises(Exception) as context:
            self.guerreroA.atacar(self.guerreroB, self.guerreroA.habilidades[0])
        self.assertTrue(context, "El personaje a muerto" )
        
        with self.assertRaises(Exception) as context:
            self.guerreroA.atacar(self.guerreroB, self.guerreroA.habilidades[0])
        self.assertTrue(context, "No tienes suficiente furia" )


if __name__ == '__main__':
    unittest.main()