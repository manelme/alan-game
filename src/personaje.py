# coding: utf-8

class Personaje():
    
    def __init__(self, nombre, vida_total, vida_restante):
        self.nombre = nombre
        self.nivel = 0
        self.porcentaje_de_nivel = 0
        self.elo = 0
        self.vida_total = vida_total
        self.vida_restante = vida_restante
    