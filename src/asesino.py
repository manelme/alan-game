# coding: utf-8
from personaje import Personaje
from subterfujio import Subterfujio

class Asesino(Personaje):

    def __init__(self, nombre):
        super().__init__(nombre, vida_total = 70, vida_restante = 70)
        self.energia_total = 100
        self.energia_restante = 100
        self.habilidades = []
    
    def modificar_vida(self, cantidad):
        try:
            self.vida_restante += cantidad
            if self.vida_restante <= 0:
                self.vida_restante = 0
                raise Exception("El personaje a muerto")
            if self.vida_restante > self.vida_total:
                self.vida_restante = self.vida_total
        except:
            pass
    
    def modificar_vida_total(self, cantidad):
        try:
            self.vida_total += cantidad
            if self.vida_total <= 0:
                self.vida_total = 0
                raise Exception("El personaje a muerto")
        except:
            pass

    def modificar_energia(self, cantidad):
        try:
            self.energia_restante += cantidad
            if self.energia_restante <= 0:
                self.energia_restante = 0
                raise Exception("No queda energia")
            if self.energia_restante > self.energia_total:
                self.energia_restante = self.energia_total
        except:
            pass

    def modificar_energia_total(self, cantidad):
        try:
            self.energia_total += cantidad
            if self.energia_total <= 0:
                self.energia_total = 0
                raise Exception("No queda energia")
        except:
            pass

    def add_habilidad(self, habilidad):
        try:
            if type(habilidad) is not Subterfujio:
                raise Exception("La habilidad tiene que ser de tipo subterfujio")
            self.habilidades.append(habilidad)
        except:
            pass

    def atacar(self, personaje, habilidad):
        try:
            if self.energia_restante < hablidad.coste_energia:
                raise Exception("No tienes suficiente energia")
            personaje.modificar_vida(-habilidad.danyo)
            self.modificar_furia(-habilidad.coste_furia)
        except:
            pass
