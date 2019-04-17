# coding: UTF-8

import unittest
from subterfujio import Subterfujio

class Subterfujio_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando test de la clase Subterfujio")
    
        self.subterfujioA = Subterfujio("Backstab",10,15)
        self.subterfujioB = Subterfujio("Jugarreta",20,25)
        
    def test_subterfujio_name(self):
        self.assertEqual(self.subterfujioA.nombre, 'Backstab')
        self.assertNotEqual(self.subterfujioB.nombre, 'Backstab')
    
    def test_subterfujio_danyo(self):
        self.assertEqual(self.subterfujioA.danyo, 10)
        self.assertEqual(self.subterfujioB.danyo, 20)
    
    def test_subterfujio_coste(self):
        self.assertEqual(self.subterfujioA.coste_energia, 15)
        self.assertEqual(self.subterfujioB.coste_energia, 25)

if __name__ == '__main__':
    unittest.main()