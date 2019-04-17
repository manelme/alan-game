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
                raise Exception()
            if self.vida_restante > self.vida_total:
                self.vida_restante = self.vida_total
        except:
            raise Exception("El personaje a muerto")
            pass
    
    def modificar_vida_total(self, cantidad):
        try:
            self.vida_total += cantidad
            if self.vida_total <= 0:
                self.vida_total = 0
                self.vida_restante = 0
                raise Exception()
        except:
            raise Exception("El personaje a muerto")
            pass

    def modificar_energia(self, cantidad):
        try:
            self.energia_restante += cantidad
            if self.energia_restante <= 0:
                self.energia_restante = 0
                raise Exception()
            if self.energia_restante > self.energia_total:
                self.energia_restante = self.energia_total
        except Exception:
            raise Exception("No queda energia")
            pass

    def modificar_energia_total(self, cantidad):
        try:
            self.energia_total += cantidad
            if self.energia_total <= 0:
                self.energia_total = 0
                self.energia_restante = 0
                raise Exception()
        except:
            raise Exception("No queda energia")
            pass

    def add_habilidad(self, habilidad):
        try:
            if type(habilidad) is not Subterfujio:
                raise Exception("La habilidad tiene que ser de tipo subterfujio")
            self.habilidades.append(habilidad)
        except:
            raise Exception("La habilidad tiene que ser de tipo subterfujio")
            pass

    def atacar(self, personaje, habilidad):
        try:
            if self.energia_restante < habilidad.coste_energia:
                raise Exception("No tienes suficiente energia")
            personaje.modificar_vida(-habilidad.danyo)
            self.modificar_energia(-habilidad.coste_energia)
        except Exception as e:
            raise Exception(e.args)
            pass
