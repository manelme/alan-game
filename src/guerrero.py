# coding: utf-8
from personaje import Personaje

class Guerrero(Personaje):

    def __init__(self, nombre):
        super().__init__(nombre, vida_total = 100, vida_restante = 100, armadura = 100)
        self.furia_total = 100
        self.furia_restante = 100


    def modificar_vida(self, cantidad):
        self.vida_restante += cantidad
    
    def modificar_vida_total(self, cantidad):
        self.vida_total += cantidad

    def modificar_furia(self, cantidad):
        self.furia_restante += cantidad
    
    def modificar_furia_total(self, cantidad):
        self.furia_total += cantidad