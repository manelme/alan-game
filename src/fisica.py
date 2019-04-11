# coding: utf-8
from habilidad import Habilidad

class Fisica(Habilidad):

    def __init__(self, nombre, danyo, coste_furia):
        super().__init__(nombre, danyo)
        self.coste_furia = coste_furia