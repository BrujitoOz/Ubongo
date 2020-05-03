
class Jugador:
  def __init__(self, nombre, es_humano, posicion_tablero,color):
    self.nombre = nombre #string
    self.es_humano = es_humano #booleano
    self.cant_gemas = [0,0,0,0,0,0]# 0rojo, 1verde, 2azul, 3naranaja, 4amarillo, 5morado
    self.posicion_tablero = posicion_tablero
    self.color = color#color ficha

  def SetPlantilla(self, PlantillaAct):
    #self.PlantillaAct = PlantillaAct #Obj plantilla # el jugador guardara su plantilla actual
    return 0