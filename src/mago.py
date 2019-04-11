# coding: utf-8
from personaje import Personaje
from magia import Magia

class Mago(Personaje):

    def __init__(self, nombre):
        super().__init__(nombre, vida_total=80, vida_restante = 80)
        self.mana_total=100
        self.mana_restante=100
        self.habilidades=[]
    
    def modificar_vida(self, cantidad):
        try:
            self.vida_restante+=cantidad
            if self.vida_restante <= 0:
                self.vida_restante = 0
                raise Exception("El personaje a muerto")
        except:
            pass
    
    def modificar_vida_total(self, cantidad):
        self.vida_total+=cantidad
    
    def modificar_mana(self, cantidad):
        self.mana_restante+=cantidad
    
    def modificar_mana_total(self, cantidad):
        self.mana_total+=cantidad

    def add_habilidad(self, habilidad):
        try:
            if type(habilidad) is not Magia:
                raise Exception("La habilidad tiene que ser una magia")
            self.habilidades.append(habilidad)
        except:
            pass
    
    def atacar(personaje, habilidad):
        try:
            if self.mana_restante < habilidad.mana:
                raise Exception("No tienes suficiente mana")
            personaje.modificar_vida(-habilidad.danyo)
            self.modificar_mana(-habilidad.coste_mana)
        except:
            pass
    

