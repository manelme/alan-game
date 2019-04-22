# coding: utf-8

class Personaje():
    
    def __init__(self, nombre, vida_total, vida_restante):
        self.nombre = nombre
        self.nivel = 1
        self.porcentaje_de_nivel = 0
        self.vida_restante = vida_restante
        self.vida_total = vida_total
        self.elo = 1200
    