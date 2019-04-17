# coding: utf-8
from personaje import Personaje
from magia import Magia

class Mago(Personaje):

    def __init__(self, nombre):
        super().__init__(nombre, vida_total = 70, vida_restante = 70)
        self.mana_total = 100
        self.mana_restante = 100
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

    def modificar_mana(self, cantidad):
        try:
            self.mana_restante += cantidad
            if self.mana_restante <= 0:
                self.mana_restante = 0
                raise Exception()
            if self.mana_restante > self.mana_total:
                self.mana_restante = self.mana_total
        except Exception:
            raise Exception("No queda mana")
            pass

    def modificar_mana_total(self, cantidad):
        try:
            self.mana_total += cantidad
            if self.mana_total <= 0:
                self.mana_total = 0
                self.mana_restante = 0
                raise Exception()
        except:
            raise Exception("No queda mana")
            pass

    def add_habilidad(self, habilidad):
        try:
            if type(habilidad) is not Magia:
                raise Exception("La habilidad tiene que ser de tipo magia")
            self.habilidades.append(habilidad)
        except:
            raise Exception("La habilidad tiene que ser de tipo magia")
            pass

    def atacar(self, personaje, habilidad):
        try:
            if self.mana_restante < habilidad.coste_mana:
                raise Exception("No tienes suficiente mana")
            personaje.modificar_vida(-habilidad.danyo)
            self.modificar_mana(-habilidad.coste_mana)
        except Exception as e:
            raise Exception(e.args)
            pass
