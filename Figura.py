class Figura:
    def __init__(self, nombre, estados):
        self.nombre = nombre
        self.estados = estados # array
        self.cantidad_estados = len(estados)
        self.estado_actual = 0
        self.x = 0
        self.y = 0
    def change_estado(self):
        self.estado_actual = self.estado_actual + 1
        if self.estado_actual == self.cantidad_estados:
            self.estado_actual = 0