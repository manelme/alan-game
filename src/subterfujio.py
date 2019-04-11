# coding: utf-8
from habilidad import Habilidad

class Subterfujio(Habilidad):

    def __init__(self, nombre, danyo, coste_energia):
        super().__init__(nombre, danyo)
        self.coste_energia = coste_energia