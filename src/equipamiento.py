# coding: UTF-8
from objeto import Objeto

class Equipamiento(Objeto):

    def __init_(self, nombre, precio, peso, armadura):
        super().__init__(nombre, precio, peso)
        self.armadura = armadura