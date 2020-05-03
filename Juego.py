
import random
import pygame
from pygame.locals import * # el * significa que importe todo
from Constantes import *

class Juego:
  def __init__(self, listaJugadores, figuras,windowSurface,basicFont):
    self.jugadores  = listaJugadores
    self.cant_jugadores = len(listaJugadores)
    self.reloj_arena = 60 # 60 segundos
    self.jugador_actual = 0 # jugador que esta jugando en este momento
    self.dado = 1
    self.tablero = self.create_tablero()
    self.tableroJugadores = self.create_tablero_jugadores()
    self.figuras = figuras
    self.windowSurface = windowSurface
    self.basicFont = basicFont


    # 0 se esta en la parte de tirar el dado, 
    # 1 se esta en la parte del puzzle
    # 2 se esta en la parte de recoger gemas
    self.estado = 0 

  def create_tablero(self):
    # se inicializa el tablero  
    tablero = [[_ for _ in range(12)] for _ in range(6)]

    # 0rojo, 1verde, 2azul, 3naranaja, 4amarillo, 5morado
    gemas = []

    # genero 12 gemas por cada tipo
    for _ in range(12):
      for x in range(6):
        gemas.append(x)

    # se ordenan aleatoriamente las gemas
    random.shuffle(gemas)

    # se coloca las gemas en las filas del tablero
    k = 0
    for i in range(6):
      for j in range(12):
        tablero[i][j] = gemas[k]
        k= k + 1

    return tablero

  def create_tablero_jugadores(self):
    tablero = [[],[],[],[],[],[]]
    # se van a iniciar todos los jugadores en la posicion
    # que deseen (deberia definirse a la hora de crear los jugadores)
    for i in range(self.cant_jugadores):
      pos = self.jugadores[i].posicion_tablero
      # guardo en el tablero la posicion del jugador que se encuentra ahi
      tablero[pos].append(i)

    return tablero  

  def lanzar_dados(self):
    simbolos = [1,2,3,4,5,6]
    self.dado = random.choice(simbolos)#elige al azar

  def jugar(self, pressed):
    # Si se esta en la fase de tirar el dado
    if (self.estado == 0):
        if (pressed[pygame.K_SPACE]):
          self.lanzar_dados()
          self.estado = 2 # pasa el estado a resolver el puzzle 
          self.dibujar()   
    
    
    return

  def dibujar(self):
    #Draw the white background onto the surface
    self.windowSurface.fill(WHITE)

    # ponermos el nombre del jugador que le toca tirar los dados
    jugador = self.jugadores[self.jugador_actual]

    if( self.estado == 0):
      texto = "Le toca el turno al jugador: " + str(self.jugador_actual + 1) + "-" +  jugador.nombre
      self.dibujarTexto(self.basicFont, texto, BLACK,5,5)
      self.dibujarTexto(self.basicFont, "Presione Espacio para lanzar el dado", BLACK,5,15)

    if(self.estado == 2):
      texto = "Salieron las figuras número: " + str(self.dado)
      self.dibujarTexto( self.basicFont, texto, BLACK,5,5)

    self.dibujarTableros()
    pygame.display.update()

  def dibujarTableros(self):
    
    # jugadores
    xjugadores = 30
    yjugadores = YTABLERO 

    for i in range(6):
      fila = self.tableroJugadores[i]  
      for j in range(len(fila)):
        jugadorPos = fila[j]
        jugador = self.jugadores[jugadorPos]
        pygame.draw.circle(self.windowSurface, jugador.color, (xjugadores,yjugadores), 5)
        self.dibujarTexto(self.basicFont, str(jugadorPos + 1), jugador.color,xjugadores + 5,yjugadores)
        xjugadores = xjugadores + 20

      yjugadores = yjugadores + 30   
      xjugadores = 30
               

    #gemas
    xgemas = 200
    ygemas = YTABLERO 
    color =  BLACK
    # se dibujan as gemas  
    for i in range(6):
      for j in range(12):
        gema = self.tablero[i][j];

        if (gema == -1): # si ya la tiene un jugador
          color = WHITE
        if (gema == 0):  # 0rojo, 1verde, 2azul, 3naranaja, 4amarillo, 5morado 
          color = RED
        if (gema == 1):
          color = GREEN
        if (gema == 2):
          color = BLUE
        if (gema == 3):
          color = ORANGE 
        if (gema == 4):
          color = YELLOW  
        if (gema == 5):
          color = PURPLE                               
          
    
        pygame.draw.circle(self.windowSurface, color, (xgemas,ygemas), 5)  
        xgemas = xgemas + 20
      ygemas = ygemas + 30
      xgemas = 200      

  def dibujarTexto(self, font, texto, color,x,y):
    text_surface = font.render(texto, True, color)
    self.windowSurface.blit(text_surface, (x, y))  