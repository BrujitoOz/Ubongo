class Plantilla:
  def __init__(self, matriz, opciones):
    self.matriz = matriz #matriz de la plantilla
    self.opciones = opciones #figuras para armarla

import random
class Jugador:
  def __init__(self, nombre, es_humano):
    self.nombre = nombre #string
    self.es_humano = es_humano #booleano
    self.cant_gemas = [0,0,0,0,0,0]
    # 0rojo, 1verde, 2azul, 3naranaja, 4amarillo, 5morado
  def SetPlantilla(self, PlantillaAct):
    #self.PlantillaAct = PlantillaAct #Obj plantilla
    return 0

        
class Juego:
  def __init__(self, ListaJugadores, figuras):
    self.cant_jugadores = len(ListaJugadores)
    self.reloj_arena = 60
    self.jugador_actual = 0 # jugador que esta jugando en este momento
    self.dado = self.lanzar_dados()
    self.tablero = self.create_tablero()
    self.figuras = figuras
  

  def create_tablero(self):
    TABLERO = [[_ for _ in range(12)] for _ in range(6)]
    return TABLERO #Falta aniadir las gemas aleatoriamente

  def lanzar_dados(self):
    simbolos = [1,2,3,4,5,6]#opciones para armar,podemos poner char
    return random.choice(simbolos)#elige al azar

  def jugar(self):
    # se lanza el dado y se activa el tiempo
    # el jugador arma la plantilla que le toco con las figuras que indico el dado
    # cuando acabe, mueve su ficha si quiere, y agarra 2 gemas
    # la ronda acaba cuando termine de hacer eso
    # o cuando el tiempo acabe
    # asi termina la primera ronda, el juego dura 9 rondas
    return 0 
    


LasPiezas = [
  [
    [1,1], #cuadrado
    [1,1]
  ],
  [
    [1,0,0,0], #palote(4)
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0]
  ],
  [
    [1,0,0], #palo(3)
    [1,0,0],
    [1,0,0]
  ],
  [
    [1,0], #palito(2)
    [1,0]
  ],
  [
    [0,0,0,1], #L grande(4)
    [0,0,0,1],
    [0,0,0,1],
    [0,0,1,1]
  ],
  [
    [0,0,1], #L(3)
    [0,0,1],
    [0,1,1]
  ],
  [
    [0,1], #L chiquita(2)
    [1,1]
  ],
  [
    [0,0,0], # Tetris1
    [0,1,0],
    [1,1,1]
  ],
  [
    [0,0,0,0], # Tetris2
    [0,0,0,0],
    [0,0,1,0],
    [1,1,1,1]
  ],
  [
    [0,0,0], # gusano1
    [0,1,1],
    [1,1,0]
  ],
  [
    [0,1,1], # gusano2
    [0,1,0],
    [1,1,0]
  ],
  [
    [0,0,0], # deforme
    [0,1,1],
    [1,1,1]
  ]
]

j1 = Jugador("Pepe", True)
j2 = Jugador("Maria", False)
ListaJugadores = [j1, j2]
juego = Juego(ListaJugadores, LasPiezas)
juego.jugar()





LasPlantillas = [
  [
    [1,1,1,1,0],#plantilla 1
    [1,1,1,0,0],
    [0,1,1,1,1]
    #opcion1:palito, deforme, L
    #opcion2:L, palote, palo
    #opcion3:tetris2, gusano, palito
    #opcion4:gusano1, palo, tetris1
    #opcion5: L grande, tetris1, palito
    #opcion6: palo, L, gusano1
  ],
  [
    [0,0,1,1],#plantilla 2
    [1,1,1,1],
    [1,1,1,1],
    [0,1,1,0]
    #opcion1:tetris1,deforme,L chiquita
    #opcion2:L chiquita, gusano2, L
    #opcion3:cuadrado, palo, L grande
    #opcion4:gusano1, L chiquita, deforme
    #opcion5:L, deforme, palo
    #opcion6:gusano1, palo, tetris2
  ]
]



#Instrucciones
# 2 - 4 jugadores 
# el jugador con mas gemas de un mismo color gana
# 1 tablero, hasta 4 fichas de jugador, reloj de arena, un dado con simbolos
# 36 plantillas, si son 2 jugadores juegan 18 plantillas, con 3 27, con 4 36: o sea siempre se juegan 9 rondas
# y para el final del juego cada jugador habra jugado con 9 plantillas
# 72 piezas de gemas(rojo,verde,azul,naranja,amarillo,morado), 
# 12 figuras parecidas a las de tetris con formas diferentes
# El tablero es matriz 6x12 y debe inicializarce con las 72 gemas distribuidas al azar
# cada jugador posiciona su ficha a la altura de unas de las filas del tablero
# se decide el jugador que tira el dado y activa el reloj
# cada jugador agarra una plantilla y lo arma segun las fichas que indica el dado
# el 1er jugador que termine de armar su plantilla puede mover su ficha hasta 3 casillas y agarrar las 2 primeras gemas de la tabla
# el 2do en terminar puede mover su ficha hasta 2 posiciones si quiere, el 3ero 1, el 4to ninguna
# todos los jugadores pueden encontrarse en una misma fila a la vez
# la primera ronda acaba cuando todos hayan jugado o acabe el tiempo
# el siguiente jugador tirara el dado y activara el reloj 
# asi hasta que acaben las plantillas que dan para 9 rondas
# si hay empate se desempata por medio de ver quien tiene mas gemas del siguiente color obtenido
