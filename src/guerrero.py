# coding: utf-8
from personaje import Personaje
from fisica import Fisica

class Guerrero(Personaje):

    def __init__(self, nombre):
        super().__init__(nombre, vida_total = 100, vida_restante = 100)
        self.furia_total = 100
        self.furia_restante = 100
        self.habilidades=[]


    def modificar_vida(self, cantidad):
        try:
            self.vida_restante += cantidad
            if self.vida_restante <= 0:
                self.vida_restante = 0
                raise Exception("El personaje a muerto")
        except:
            pass
    
    def modificar_vida_total(self, cantidad):
        self.vida_total += cantidad

    def modificar_furia(self, cantidad):
        self.furia_restante += cantidad
    
    def modificar_furia_total(self, cantidad):
        self.furia_total += cantidad

    def add_habilidad(self, habilidad):
        try:
            if type(habilidad) is not Fisica:
                raise Exception("La habilidad tiene que ser de tipo fisica")
            self.habilidades.append(habilidad)
        except:
            pass
    
    def atacar(personaje, habilidad):
        try:
            if self.furia_restante < hablidad.coste_furia:
                raise Exception("No tienes suficiente furia")
            personaje.modificar_vida(-habilidad.danyo)
            self.modificar_furia(-habilidad.coste_furia)
        except:
            pass
