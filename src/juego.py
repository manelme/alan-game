# coding: utf-8
class Juego():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.precioRebajado = precio * 0.5
    
    def cambiar_nombre(self, nuevoNombre):
        try:
            if type(nuevoNombre) is not str:
                raise Exception()
            else:
                self.nombre = nuevoNombre
        except:
            raise Exception("El nombre no puede ser un numero")
            pass

    def cambiar_precio_final(self, nuevoPrecio):
        try:
            self.precio = nuevoPrecio
            if self.precio <= 0:
                self.precio = 0
                raise Exception()
        except:
            raise Exception("El precio no puede ser menor que 0")
            pass
    
    def cambiar_precio_rebajado(self, porcentaje):
        try:
            self.precioRebajado = self.precio * porcentaje
            if self.precioRebajado <= 0:
                self.precio = 0
                raise Exception()
        except:
            raise Exception("El precio rebajado no puede ser menor que 0")
            pass
    
    def cambiar_precios(self, nuevoPrecio, porcentaje):
        try:
            self.cambiar_precio_final(self, nuevoPrecio)
            self.cambiar_precio_rebajado(self, porcentaje)
        except Exception as e:
            raise Exception(e.arg)
            pass

    