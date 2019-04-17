# coding: utf-8
import unittest
from personaje import Personaje
from mago import Mago
from magia import Magia

class Mago_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando la clase Mago")
    
        self.magoA = Mago("Ezio")
        self.magoB = Mago("Altair")
        
    def test_personaje_name(self):
        self.assertEqual(self.magoA.nombre, 'Ezio')
        self.assertNotEqual(self.magoA.nombre, 'Altair')
        
    def test_comprobar_vida_restante(self):

        self.assertEqual(self.magoA.vida_restante, 70)

        self.magoA.modificar_vida(-50)
        self.assertEqual(self.magoA.vida_restante, 20)
        self.magoA.modificar_vida(30)
        self.assertEqual(self.magoA.vida_restante, 50)

        self.magoA.modificar_vida(30)
        self.assertNotEqual(self.magoA.vida_restante, 80)
        
        with self.assertRaises(Exception) as context:
            self.magoA.modificar_vida(-200)
        self.assertTrue(context, "El personaje a muerto" )
        self.assertEqual(self.magoA.vida_restante, 0)

    def test_comprobar_vida_total(self):
        
        self.assertEqual(self.magoA.vida_total, 70)

        self.magoA.modificar_vida_total(70)
        self.assertEqual(self.magoA.vida_total, 140)
        self.magoA.modificar_vida_total(-50)
        self.assertEqual(self.magoA.vida_total, 90)

        with self.assertRaises(Exception) as context:
            self.magoA.modificar_vida_total(-130)
        self.assertTrue(context, "El personaje a muerto" )

    def test_comprobar_vida_restante_total(self):
        
        with self.assertRaises(Exception) as context:
            self.magoA.modificar_vida_total(-130)
        self.assertTrue(context, "El personaje a muerto" )

        self.magoA.modificar_vida_total(70)
        self.assertEqual(self.magoA.vida_total, 70)
        self.magoA.modificar_vida(100)
        self.assertEqual(self.magoA.vida_restante, 70)

    def test_comprobar_mana(self):

        self.assertEqual(self.magoA.mana_restante, 100)
       
        self.magoA.modificar_mana(-15)
        self.assertEqual(self.magoA.mana_restante, 85)
        self.magoA.modificar_mana(40)
        self.assertEqual(self.magoA.mana_restante, 100)

        with self.assertRaises(Exception) as context:
            self.magoA.modificar_mana(-130)
        self.assertTrue(context, "No queda mana" )
        self.assertEqual(self.magoA.mana_restante, 0)

    def test_comprobar_mana_total(self):

        self.assertEqual(self.magoA.mana_total, 100)
        
        self.magoA.modificar_mana_total(-10)
        self.assertEqual(self.magoA.mana_total, 90)
        self.magoA.modificar_mana_total(100)
        self.assertEqual(self.magoA.mana_total, 190)

        with self.assertRaises(Exception) as context:
            self.magoA.modificar_mana_total(-200)
        self.assertTrue(context, "No queda mana" )
        self.assertEqual(self.magoA.mana_total, 0)

    def test_comprobar_mana_restante_total(self):
        
        with self.assertRaises(Exception) as context:
            self.magoA.modificar_mana_total(-130)
        self.assertTrue(context, "No queda mana" )

        self.assertEqual(self.magoA.mana_total, 0)
        self.assertEqual(self.magoA.mana_restante, 0)

        self.magoA.modificar_mana_total(70)
        self.magoA.modificar_mana(120)
        self.assertEqual(self.magoA.mana_restante, 70)


    def test_add_magia(self):
        self.magoA.add_habilidad(Magia("Bola de Fuego", 50, 15))
        self.assertEqual("Bola de Fuego", self.magoA.habilidades[0].nombre)
        with self.assertRaises(Exception) as context:
            self.magoA.add_habilidad(Fisica("Testarazo", 50, 15))
        self.assertTrue(context, "La habilidad tiene que ser de tipo magia" )
    
    def test_atacar(self):
        self.magoA.add_habilidad(Magia("Bola de Fuego", 50, 50))
        
        self.magoA.atacar(self.magoB, self.magoA.habilidades[0])
        self.assertEqual(self.magoB.vida_restante,20)
        self.assertEqual(self.magoA.mana_restante,50)
        
        with self.assertRaises(Exception) as context:
            self.magoA.atacar(self.magoB, self.magoA.habilidades[0])
        self.assertTrue(context, "El personaje a muerto" )
        
        with self.assertRaises(Exception) as context:
            self.magoA.atacar(self.magoB, self.magoA.habilidades[0])
        self.assertTrue(context, "No tienes suficiente mana" )


if __name__ == '__main__':
    unittest.main()