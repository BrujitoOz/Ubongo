class Jugador:
    def __init__(self, nombre, es_humano, posicion_tablero, color):
        self.nombre = nombre
        self.es_humano = es_humano
        self.cant_gemas = [0, 0, 0, 0, 0, 0]
        self.posicion_tablero = posicion_tablero
        self.color = color
    def SetPlantilla(self):
        return 0
