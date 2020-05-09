import pygame, random
from pygame.locals import *
from Constantes import *
class Juego:
    def __init__(self, listaJugadores, windowSurface, basicFont):
        self.jugadores = listaJugadores
        self.cant_jugadores = len(listaJugadores)
        self.reloj_arena = 60
        self.jugador_actual = 0
        self.dado = -1
        self.plantillaIndex = 0
        self.tablero = self.create_tablero()
        self.tableroJugadores = self.create_tablero_jugadores()
        self.windowSurface = windowSurface
        self.basicFont = basicFont
        self.estado = 0 # 0 tirar el dado, 1 arma el puzzle, 2 recoger gemas
    def create_tablero(self):
        tablero = [[_ for _ in range(12)] for _ in range(6)]
        gemas = []
        for _ in range(12):
            for x in range(6):
                gemas.append(x)
        random.shuffle(gemas)
        k = 0
        for i in range(6):
            for j in range(12):
                tablero[i][j] = gemas[k]
                k += 1
        return tablero
    def create_tablero_jugadores(self):
        tablero = [[], [], [], [], [], []]
        for i in range(self.cant_jugadores):
            pos = self.jugadores[i].posicion_tablero
            tablero[pos].append(i)
        return tablero
    def lanzar_dados(self):
        simbolos = [0, 1, 2, 3, 4, 5]
        self.dado = random.choice(simbolos)
    def jugar(self, pressed):
        if self.estado == 0:
            if pressed[pygame.K_SPACE]:
                self.lanzar_dados()
                self.estado = 1
                self.dibujar()
        return
    def dibujar(self):
        self.windowSurface.fill(WHITE)
        jugador = self.jugadores[self.jugador_actual]
        if self.estado == 0:
            texto = "Le toca el turno al jugador; " + str(self.jugador_actual + 1) + " - " + jugador.nombre
            self.dibujarTexto(self.basicFont, texto, BLACK, 5, 5)
            self.dibujarTexto(self.basicFont, "Presione Espacio para lanzar el dado", BLACK, 5, 15)
        if self.estado == 1:
            texto = "Salieron las figuras número: " + str(self.dado)
            self.dibujarTexto(self.basicFont, texto, BLACK, 5, 5)
            self.dibujarPlantilla()
        self.dibujarTableros()
        pygame.display.update()

    def dibujarTableros(self):
        #dibujar tablero de jugadores
        xjugadores = 30
        yjugadores = YTABLERO
        for i in range(6):
            fila = self.tableroJugadores[i]
            for j in range(len(fila)):
                jugadorPos = fila[j]
                jugador = self.jugadores[jugadorPos]
                pygame.draw.circle(self.windowSurface, jugador.color, (xjugadores, yjugadores), 5)
                self.dibujarTexto(self.basicFont, str(jugadorPos + 1), jugador.color, xjugadores + 5, yjugadores)
                xjugadores += 20
            yjugadores += 30
            xjugadores = 30
        # dibujar gemas 
        xgemas = 200
        ygemas = YTABLERO
        color = BLACK
        for i in range(6):
            for j in range(12):
                gema = self.tablero[i][j]
                if gema == -1:
                    color = WHITE
                if gema == 0:
                    color = RED
                if gema == 1:
                    color = GREEN
                if gema == 2:
                    color = BLUE
                if gema == 3:
                    color = ORANGE
                if gema == 4:
                    color = YELLOW
                if gema == 5:
                    color = PURPLE
                pygame.draw.circle(self.windowSurface, color, (xgemas, ygemas), 5)
                xgemas += 20
            ygemas += 30
            xgemas = 200

    def dibujarPlantilla(self):
        # Obtenemos la plantiila y figuras a utilizar
        plantilla = Plantillas[self.plantillaIndex]
        figuras = Opciones[self.plantillaIndex][self.dado]

        xinicial = 30
        xfiguras = xinicial
        yfiguras = YFIGURAS
        c = [RED, GREEN, BLUE]
        # dibujando figuras a utilizar
        for figura in figuras:
            #print(figura)
            xtemp = xfiguras
            micolor = c.pop()
            for i in range(len(figura)):
                fila = figura[i]
                for j in range(len(fila)):
                    if fila[j] == 1:
                        pygame.draw.rect(self.windowSurface, micolor, (xfiguras, yfiguras, 10, 10))
                    else:
                        pygame.draw.rect(self.windowSurface, WHITE, (xfiguras, yfiguras, 10, 10))
                    xfiguras += 10
                xfiguras = xtemp
                yfiguras += 10
            yfiguras = YFIGURAS
            xfiguras += 4 * 10
        
        xplantilla = xinicial
        yplantilla = YPLANTILLA

        for i in range(len(plantilla)):
            fila = plantilla[i]
            for j in range(len(fila)):
                if fila[j] == 1:
                    pygame.draw.rect(self.windowSurface, RED, (xplantilla, yplantilla, 10, 10))
                else:
                    pygame.draw.rect(self.windowSurface, ORANGE, (xplantilla, yplantilla, 10, 10))
                xplantilla += 10
            xplantilla = xinicial
            yplantilla += 10


    def dibujarTexto(self, font, texto, color, x, y):
        text_surface = font.render(texto, True, color)
        self.windowSurface.blit(text_surface, (x, y))
                
        