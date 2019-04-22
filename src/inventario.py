# coding: UTF-8
from objeto import Objeto
class Inventario():

    def __init__(self, huecos, peso_maximo):
        self.huecos =huecos
        self.peso_maximo = peso_maximo
        self.objetos = []

    def introducir_objeto(self, objeto):
        self.objetos.append(objeto)
            