# coding: UTF-8
from objeto import Objeto

class Arma(Objeto):

    def __init_(self, nombre, precio, peso, danyo):
        super().__init__(nombre, precio, peso)
        self.danyo = danyo