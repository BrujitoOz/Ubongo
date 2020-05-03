import pygame, sys
from pygame.locals import *
import random
from Juego import Juego
from Jugador import Jugador
from Constantes import *

LasFiguras = [
  [
    [1,1], #cuadrado       0
    [1,1]
  ],
  [
    [1,0,0,0], #palote(4)  1
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0]
  ],
  [
    [1,0,0], #palo(3)      2
    [1,0,0],
    [1,0,0]
  ],
  [
    [1,0], #palito(2)      3
    [1,0]
  ],
  [
    [0,0,0,1], #L grande(4) 4
    [0,0,0,1],
    [0,0,0,1],
    [0,0,1,1]
  ],
  [
    [0,0,1], #L(3)         5
    [0,0,1],
    [0,1,1]
  ],
  [
    [0,1], #L chiquita(2)   6
    [1,1]
  ],
  [
    [0,0,0], # Tetris1      7
    [0,1,0],
    [1,1,1]
  ],
  [
    [0,0,0,0], # Tetris2     8
    [0,0,0,0],
    [0,0,1,0],
    [1,1,1,1]
  ],
  [
    [0,0,0], # gusano1      9
    [0,1,1],
    [1,1,0]
  ],
  [
    [0,1,1], # gusano2    10
    [0,1,0],
    [1,1,0]
  ],
  [
    [0,0,0], # p            11
    [0,1,1],
    [1,1,1]
  ]
]

LasPlantillas = [
  [
    [1,1,1,1,0],#plantilla 1
    [1,1,1,0,0],
    [0,1,1,1,1]
  ],
  [
    [0,0,1,1],#plantilla 2
    [1,1,1,1],
    [1,1,1,1],
    [0,1,1,0]

  ]
]
Opciones = [
    # para la plantilla 0
    [
        [LasFiguras[3], LasFiguras[11], LasFiguras[5]],#opcion 0: palito, P, L
        [LasFiguras[5], LasFiguras[1], LasFiguras[2]],#opcion 1: L, palote, palo
        [LasFiguras[8], LasFiguras[9], LasFiguras[3]],#opcion 2: tetris2, gusano, palito
        [LasFiguras[9], LasFiguras[2], LasFiguras[7]],#opcion 3: gusano1, palo, tetris1
        [LasFiguras[4], LasFiguras[7], LasFiguras[3]],#opcion 4: L grande, tetris1, palito
        [LasFiguras[2], LasFiguras[5], LasFiguras[9]]#opcion 5: palo, L, gusano1
    ],
    # para la plantilla 1
    [
        [LasFiguras[9], LasFiguras[2], LasFiguras[8]],#opcion 0: gusano1, palo, tetris2
        [LasFiguras[5], LasFiguras[11], LasFiguras[2]],#opcion 1: L, P, palo
        [LasFiguras[9], LasFiguras[6], LasFiguras[11]],#opcion 2: gusano1, L chiquita, P
        [LasFiguras[0], LasFiguras[2], LasFiguras[4]],#opcion 3: cuadrado, palo, L grande
        [LasFiguras[6], LasFiguras[10], LasFiguras[5]],#opcion 4: L chiquita, gusnano2, L
        [LasFiguras[7], LasFiguras[11], LasFiguras[6]]#opcion 5: tetris1, P, L chiquita
    ]
]

class Plantilla:
  def __init__(self, matriz, opciones):
    self.matriz = matriz #matriz de la plantilla
    self.opciones = opciones #figuras para armarla


    #print(self.tablero)
    # se lanza el dado y se activa el tiempo
    # el jugador arma la plantilla que le toco con las figuras que indico el dado
    # cuando acabe, mueve su ficha si quiere, y agarra 2 gemas
    # la ronda acaba cuando termine de hacer eso
    # o cuando el tiempo acabe
    # asi termina la primera ronda, el juego dura 9 rondas
    
P0 = Plantilla(LasPlantillas[0], Opciones[0])
P1 = Plantilla(LasPlantillas[1], Opciones[1])
ArrayDePlantilla = [P0, P1]

def main():
    #nombre, humano o maquina, posicion, color
    j1 = Jugador("Pepe", True,3,BLUE)
    j2 = Jugador("Maria", False,3,BLACK)
    j3 = Jugador("Jose", False,0,GREEN)
    ListaJugadores = [j1, j2,j3]

    pygame.init()

    # set up fonts
    basicFont = pygame.font.SysFont(None, 16)#fuente para la letra
    windowSurface = pygame.display.set_mode((500, 400), 0 , 32)#esto viene a ser como el g graphics de windows form
    juego = Juego(ListaJugadores, LasFiguras,windowSurface,basicFont)
    juego.dibujar()

    while True:
        event = pygame.event.wait()

        if event.type == QUIT:
          pygame.quit()
          sys.exit()  

        pressed = pygame.key.get_pressed()
        juego.jugar(pressed)
          

if __name__ == "__main__":
    main()


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