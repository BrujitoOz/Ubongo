import pygame, sys
from Juego import Juego
from Jugador import Jugador
from Constantes import BLUE, BLACK, GREEN, WHITE, ORANGE
from pygame.locals import *

def game_intro():
    windowSurface = pygame.display.set_mode((600, 600), 0, 32)
    windowSurface.fill(WHITE)
    titleFont = pygame.font.SysFont(None, 50)
    text_surface = titleFont.render("Ubongo", True, ORANGE)
    windowSurface.blit(text_surface, (230, 250))

    SubTitleFont = pygame.font.SysFont(None, 20)
    text_sub = SubTitleFont.render("Presione espacio para continuar", True, BLACK)
    windowSurface.blit(text_sub, (195, 300))

    pygame.display.update()
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            play_game()
def play_game():
    j1 = Jugador("Pepe", True, 3, BLUE)
    j2 = Jugador("Maria", False, 3, BLACK)
    j3 = Jugador("Jose", False, 0, GREEN)
    ListaJugadores = [j1, j2, j3]
    basicFont = pygame.font.SysFont(None, 16)
    windowSurface = pygame.display.set_mode((600, 600), 0, 32)
    juego = Juego(ListaJugadores, windowSurface, basicFont)
    juego.dibujar()
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pressed = pygame.key.get_pressed()
        juego.jugar(pressed)

def main():
    pygame.init()
    game_intro()
    

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