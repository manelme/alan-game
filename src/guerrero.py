# coding: utf-8
from personaje import Personaje
from fisica import Fisica

class Guerrero(Personaje):

    def __init__(self, nombre):
        super().__init__(nombre, vida_total = 70, vida_restante = 70)
        self.furia_total = 100
        self.furia_restante = 100
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

    def modificar_furia(self, cantidad):
        try:
            self.furia_restante += cantidad
            if self.furia_restante <= 0:
                self.furia_restante = 0
                raise Exception()
            if self.furia_restante > self.furia_total:
                self.furia_restante = self.furia_total
        except Exception:
            raise Exception("No queda furia")
            pass

    def modificar_furia_total(self, cantidad):
        try:
            self.furia_total += cantidad
            if self.furia_total <= 0:
                self.furia_total = 0
                self.furia_restante = 0
                raise Exception()
        except:
            raise Exception("No queda furia")
            pass

    def add_habilidad(self, habilidad):
        try:
            if type(habilidad) is not Fisica:
                raise Exception("La habilidad tiene que ser de tipo fisica")
            self.habilidades.append(habilidad)
        except:
            raise Exception("La habilidad tiene que ser de tipo fisica")
            pass

    def atacar(self, personaje, habilidad):
        try:
            if self.furia_restante < habilidad.coste_furia:
                raise Exception("No tienes suficiente furia")
            personaje.modificar_vida(-habilidad.danyo)
            self.modificar_furia(-habilidad.coste_furia)
        except Exception as e:
            raise Exception(e.args)
            pass
