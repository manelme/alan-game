# coding: utf-8

from habilidad import Habilidad

class Magia(Habilidad):
    def __init__(self, nombre, danyo, coste_mana):
        super().__init__(nombre, danyo)
        self.coste_mana=coste_mana

    