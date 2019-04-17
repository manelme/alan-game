# coding: utf-8
import unittest
from personaje import Personaje
from asesino import Asesino
from subterfujio import Subterfujio

class Asesino_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando la clase Asesino")
    
        self.asesinoA = Asesino("Ezio")
        self.asesinoB = Asesino("Altair")
        
    def test_personaje_name(self):
        self.assertEqual(self.asesinoA.nombre, 'Ezio')
        self.assertNotEqual(self.asesinoA.nombre, 'Altair')
        
    def test_comprobar_vida_restante(self):

        self.assertEqual(self.asesinoA.vida_restante, 70)

        self.asesinoA.modificar_vida(-50)
        self.assertEqual(self.asesinoA.vida_restante, 20)
        self.asesinoA.modificar_vida(30)
        self.assertEqual(self.asesinoA.vida_restante, 50)

        self.asesinoA.modificar_vida(30)
        self.assertNotEqual(self.asesinoA.vida_restante, 80)
        
        with self.assertRaises(Exception) as context:
            self.asesinoA.modificar_vida(-200)
        self.assertTrue(context, "El personaje a muerto" )
        self.assertEqual(self.asesinoA.vida_restante, 0)

    def test_comprobar_vida_total(self):
        
        self.assertEqual(self.asesinoA.vida_total, 70)

        self.asesinoA.modificar_vida_total(70)
        self.assertEqual(self.asesinoA.vida_total, 140)
        self.asesinoA.modificar_vida_total(-50)
        self.assertEqual(self.asesinoA.vida_total, 90)

        with self.assertRaises(Exception) as context:
            self.asesinoA.modificar_vida_total(-130)
        self.assertTrue(context, "El personaje a muerto" )

    def test_comprobar_vida_restante_total(self):
        
        with self.assertRaises(Exception) as context:
            self.asesinoA.modificar_vida_total(-130)
        self.assertTrue(context, "El personaje a muerto" )

        self.asesinoA.modificar_vida_total(70)
        self.assertEqual(self.asesinoA.vida_total, 70)
        self.asesinoA.modificar_vida(100)
        self.assertEqual(self.asesinoA.vida_restante, 70)

    def test_comprobar_energia(self):

        self.assertEqual(self.asesinoA.energia_restante, 100)
       
        self.asesinoA.modificar_energia(-15)
        self.assertEqual(self.asesinoA.energia_restante, 85)
        self.asesinoA.modificar_energia(40)
        self.assertEqual(self.asesinoA.energia_restante, 100)

        with self.assertRaises(Exception) as context:
            self.asesinoA.modificar_energia(-130)
        self.assertTrue(context, "No queda energia" )
        self.assertEqual(self.asesinoA.energia_restante, 0)

    def test_comprobar_energia_total(self):

        self.assertEqual(self.asesinoA.energia_total, 100)
        
        self.asesinoA.modificar_energia_total(-10)
        self.assertEqual(self.asesinoA.energia_total, 90)
        self.asesinoA.modificar_energia_total(100)
        self.assertEqual(self.asesinoA.energia_total, 190)

        with self.assertRaises(Exception) as context:
            self.asesinoA.modificar_energia_total(-200)
        self.assertTrue(context, "No queda energia" )
        self.assertEqual(self.asesinoA.energia_total, 0)

    def test_comprobar_energia_restante_total(self):
        
        with self.assertRaises(Exception) as context:
            self.asesinoA.modificar_energia_total(-130)
        self.assertTrue(context, "No queda energia" )

        self.assertEqual(self.asesinoA.energia_total, 0)
        self.assertEqual(self.asesinoA.energia_restante, 0)

        self.asesinoA.modificar_energia_total(70)
        self.asesinoA.modificar_energia(120)
        self.assertEqual(self.asesinoA.energia_restante, 70)


    def test_add_subterfujio(self):
        self.asesinoA.add_habilidad(Subterfujio("Backstab", 50, 15))
        self.assertEqual("Backstab", self.asesinoA.habilidades[0].nombre)
        with self.assertRaises(Exception) as context:
            self.asesinoA.add_habilidad(Magia("Bola de fuego", 50, 15))
        self.assertTrue(context, "La habilidad tiene que ser de tipo subterfujio" )
    
    def test_atacar(self):
        self.asesinoA.add_habilidad(Subterfujio("Backstab", 50, 50))
        
        self.asesinoA.atacar(self.asesinoB, self.asesinoA.habilidades[0])
        self.assertEqual(self.asesinoB.vida_restante,20)
        self.assertEqual(self.asesinoA.energia_restante,50)
        
        with self.assertRaises(Exception) as context:
            self.asesinoA.atacar(self.asesinoB, self.asesinoA.habilidades[0])
        self.assertTrue(context, "El personaje a muerto" )
        
        with self.assertRaises(Exception) as context:
            self.asesinoA.atacar(self.asesinoB, self.asesinoA.habilidades[0])
        self.assertTrue(context, "No tienes suficiente energia" )


if __name__ == '__main__':
    unittest.main()