# coding: utf-8
import unittest
from juego import Juego

class Juego_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando la clase Juego")
    
        self.juegoEjemplo = Juego("diablo 3", 65)
        
    def test_juego_inicio(self):
        self.assertEqual(self.juegoEjemplo.nombre, 'diablo 3')
        self.assertEqual(self.juegoEjemplo.precio, 65)
        self.assertEqual(self.juegoEjemplo.precioRebajado, 32.5)

    def test_comprobar_nombre(self):
        with self.assertRaises(Exception) as context:
            self.juegoEjemplo.cambiar_nombre(43)
        self.assertTrue(context, "El nombre no puede ser un numero")
        self.juegoEjemplo.cambiar_nombre("Zelda")

    def test_comprobar_precio_total(self):
        with self.assertRaises(Exception) as context:
            self.juegoEjemplo.cambiar_precio_final(-200)
        self.assertTrue(context, "El precio no puede ser menor que 0" )
    
    def test_comprobar_precio_rebajado(self):
        with self.assertRaises(Exception) as context:
            self.juegoEjemplo.cambiar_precio_rebajado(0)
        self.assertTrue(context, "El precio rebajado no puede ser menor que 0")

    def test_comprobar_precios(self):
        with self.assertRaises(Exception) as context:
            self.juegoEjemplo.cambiar_precios(0, 0.15)
        self.assertTrue(context, "El precio no puede ser menor que 0" )
        with self.assertRaises(Exception) as context:
            self.juegoEjemplo.cambiar_precios(15, 0)
        self.assertTrue(context, "El precio rebajado no puede ser menor que 0")


if __name__ == '__main__':
    unittest.main()