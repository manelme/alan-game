# coding: UTF-8

import unittest
from habilidad import Habilidad

class Habilidad_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando test de la clase Habilidad")
    
        self.habilidadA = Habilidad("Habilidad 1",10)
        self.habilidadB = Habilidad("Habilidad 2",20)
        
    def test_habilidad_name(self):
        self.assertEqual(self.habilidadA.nombre, 'Habilidad 1')
        self.assertNotEqual(self.habilidadB.nombre, 'Habilidad 1')
    
    def test_habilidad_danyo(self):
        self.assertEqual(self.habilidadA.danyo, 10)
        self.assertEqual(self.habilidadB.danyo, 20)

if __name__ == '__main__':
    unittest.main()