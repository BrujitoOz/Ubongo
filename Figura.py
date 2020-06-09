class Figura:
    def __init__(self, nombre, estados):
        self.nombre = nombre
        self.estados = estados # array
        self.cantidad_estados = len(estados)
        self.estado_actual = 0
        self.x = 0
        self.y = 0
        self.en_plantilla = False
    def change_estado(self):
        self.estado_actual = self.estado_actual + 1
        if self.estado_actual == self.cantidad_estados:
            self.estado_actual = 0
    def get_figura_actual(self):
        return self.estados[self.estado_actual]        
