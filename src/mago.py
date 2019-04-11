# coding: utf-8
from personaje import Personaje

class Mago(Personaje):

    def __init__(self, nombre):
        super().__init__(nombre, vida=80, vida_restante = 80, armadura=40)
        self.mana_total=100
        self.mana_restante=100
    
    def modificar_vida(self, cantidad):
        self.vida_restante+=cantidad
    
    def modificar_vida_total(self, cantidad):
        self.vida_total+=cantidad
    
    def modificar_mana(self, cantidad):
        self.mana_restante+=cantidad
    
    def modificar_mana_total(self, cantidad):
        self.mana_total+=cantidad
