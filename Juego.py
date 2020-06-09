import pygame, random, sys
from pygame.locals import *
from Constantes import *
class Juego:
    def __init__(self, listaJugadores, windowSurface, basicFont):
        self.jugadores = listaJugadores
        self.cant_jugadores = len(listaJugadores)
        self.reloj_arena = 60
        self.jugador_actual = 0
        self.dado = 1
        self.plantillaIndex = 0
        self.tablero = self.create_tablero()
        self.tableroJugadores = self.create_tablero_jugadores()
        self.windowSurface = windowSurface
        self.basicFont = basicFont
        # si el juego esta en estado 1, aqui se guardara una ficha si
        # el mouse esta sobre ella
        self.figura_seleccionada = None
        self.mouse_btn_one_pressed = False
        # 0 se esta en la parte de tirar el dado
        # 1 se esta en la parte del puzzle
        # 2 se esta en la parte de recoger gemas
        self.estado = 0 # 0 tirar el dado, 1 arma el puzzle, 2 recoger gemas
    def create_tablero(self):
        # se inicializa el tablero
        tablero = [[_ for _ in range(12)] for _ in range(6)]
        # 0 rojo, 1 verde, 2 azul, 3 naranja, 4 amarillo, 5 morado
        gemas = []
        # genero 12 gemas por cada tiipo
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
                k += 1
        return tablero
    def create_tablero_jugadores(self):
        tablero = [[], [], [], [], [], []]
        # se van a iniciar todos los jugadorres en la posicion
        # que deseen (deberia definirse a la hora de crear los jugadores)
        for i in range(self.cant_jugadores):
            pos = self.jugadores[i].posicion_tablero
            # guardo en el tablero la posicion del jugadroe
            tablero[pos].append(i)
        return tablero
    def lanzar_dados(self):
        simbolos = [0, 1, 2, 3, 4, 5]
        self.dado = 0 # random.choice(simbolos)
    def jugar(self, pressed, event):
        # Si se esta en la fase de tirar el dado
        if self.estado == 0:
            if pressed[pygame.K_SPACE]:
                self.lanzar_dados()
                self.estado = 1 # pasa el estado a resolver el puzzle
                self.dibujar(True)
        if self.estado == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
                if button == 1:
                    position = event.pos
                    self.set_figura_seleccionada(position)
                    self.mouse_btn_one_pressed = True
                if button == 3 and self.figura_seleccionada != None:
                    self.figura_seleccionada.change_estado()
                    self.dibujar(False)
            if event.type == pygame.MOUSEBUTTONUP:
                button = event.button
                position = event.pos
                if button == 1:
                    self.mouse_btn_one_pressed = False
                    if(self.figura_seleccionada != None):
                      self.soltar_figura_seleccionada(position)
            if event.type == pygame.MOUSEMOTION:
                if self.mouse_btn_one_pressed and self.figura_seleccionada != None:
                    position = event.pos
                    self.mover_figura_seleccionada(position)

    def dibujar(self, reset_position_figuras = False):
        #Draw the white background onto the surface
        self.windowSurface.fill(WHITE)
        # ponemos el nombre del jugador que le toca tirar los dados
        jugador = self.jugadores[self.jugador_actual]
        if self.estado == 0:
            texto = "Le toca el turno al jugador; " + str(self.jugador_actual + 1) + " - " + jugador.nombre
            self.dibujarTexto(self.basicFont, texto, BLACK, 5, 5)
            self.dibujarTexto(self.basicFont, "Presione Espacio para lanzar el dado", BLACK, 5, 15)
        if self.estado == 1:
            texto = "Salieron las figuras número: " + str(self.dado)
            self.dibujarTexto(self.basicFont, texto, BLACK, 5, 5)
            self.dibujar_plantilla()
            if reset_position_figuras:
                self.init_pos_figuras()
            self.dibujar_figuras()

        self.dibujar_tableros()
        pygame.display.update()

    def dibujar_tableros(self):

        # jugadores
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
        # gemas 
        xgemas = 200
        ygemas = YTABLERO
        color = BLACK
        for i in range(6):
            for j in range(12):
                gema = self.tablero[i][j]
                if gema == -1: # si ya la tiene un jugador
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

    def dibujar_plantilla(self):
        # Obtenemos la plantiila y figuras a utilizar
        plantilla = Plantillas[self.plantillaIndex]

        xplantilla = XINICIAL
        yplantilla = YPLANTILLA

        plantilla.x = xplantilla
        plantilla.y = yplantilla

        tamanio_figura = TAMANIOFIGURA

        #dibujamos las plantillas
        plantilla_matriz = plantilla.matriz
        for i in range(len(plantilla.matriz)):
            fila = plantilla_matriz[i]
            for j in range(len(fila)):
                if fila[j] == 1:
                    pygame.draw.rect(self.windowSurface, BLACK, (xplantilla, yplantilla, tamanio_figura, tamanio_figura))
                else:
                    pygame.draw.rect(self.windowSurface, ORANGE, (xplantilla, yplantilla, tamanio_figura, tamanio_figura))
                xplantilla += tamanio_figura
            xplantilla = XINICIAL
            yplantilla += tamanio_figura
    def init_pos_figuras(self):

        # plantilla a utilizar
        plantilla = Plantillas[self.plantillaIndex]

        # figuras a utilizar
        figuras = plantilla.opciones[self.dado]

        xfiguras = XINICIAL
        yfiguras = YFIGURAS

        #seteo las posiciones de las figras a utilizar
        for figura in figuras:
            figura.x = xfiguras
            figura.y = yfiguras
            yfiguras = YFIGURAS
            xfiguras += 4 * TAMANIOFIGURA
    def dibujar_figuras(self):
        # plantilla a utilizar
        plantilla = Plantillas[self.plantillaIndex]

        #figuras a utilizar
        figuras = plantilla.opciones[self.dado]
        c = [RED, GREEN, BLUE]
        for figura in figuras:
            self.dibujar_figura(figura, figura.estado_actual, c)
    def dibujar_figura(self, figura, estado, c):
        estados = figura.estados
        estado_actual = estados[estado]
        xtemp = figura.x
        x_figura = figura.x
        y_figura = figura.y
        tamanio_figura = TAMANIOFIGURA
        micolor = c.pop()
        for i in range(len(estado_actual)):
            fila = estado_actual[i]
            for j in range(len(fila)):
                if fila[j] == 1:
                    pygame.draw.rect(self.windowSurface, micolor, (x_figura, y_figura, tamanio_figura, tamanio_figura))
                x_figura += tamanio_figura
            x_figura = xtemp
            y_figura += tamanio_figura
    def set_figura_seleccionada(self, position):
        figuras = Plantillas[self.plantillaIndex].opciones[0] #self.dado
        mouseX = position[0]
        mouseY = position[1]

        figura_seleccionada = None

        for figura in figuras:
            x = figura.x
            y = figura.y
            if mouseX > x and mouseX < x + 20 and mouseY > y and mouseY < y + 20:
                figura_seleccionada = figura
                break

        # si hay una figura seleccionada veo si no estaba en la plantilla
        # si la figura esta en la plantilla tengo que sacarla de la plantilla
        #if figura_seleccionada !=None and figura_seleccionada.en_plantilla :


        self.figura_seleccionada = figura_seleccionada

    def mover_figura_seleccionada(self, position):
        figura = self.figura_seleccionada
        figura.x = position[0]
        figura.y = position[1]
        self.dibujar(False)

    def soltar_figura_seleccionada(self, position):
        x = position[0]
        y =  position[1]

       
        figura = self.figura_seleccionada
       
        plantilla = Plantillas[self.plantillaIndex]
        matriz = plantilla.matriz
        xp = plantilla.x
        yp = plantilla.y

        xpfinal = xp + len(matriz[0])* TAMANIOFIGURA
        ypfinal = yp + len(matriz)* TAMANIOFIGURA

        if(x >= xp and x <= xpfinal and y >= yp and y <= ypfinal   ):
          cuadrantex = (x-xp)//TAMANIOFIGURA
          cuadrantey = (y-yp)//TAMANIOFIGURA

          print("cx",cuadrantex)
          print("cy",cuadrantey)
          
          fitfigura = self.validar_figura_en_plantilla(matriz, figura.get_figura_actual(),cuadrantey,cuadrantex)

          # si nuestra figura encaja en la plantilla entonces la acomodamos
          # y actualizamos la plantilla
          if (fitfigura):
              self.colocar_figura_en_plantilla(plantilla,figura,cuadrantey,cuadrantex)


        self.figura_seleccionada = None
        self.dibujar(False)        

    def validar_figura_en_plantilla(self,plantilla, figura,fila_p,columna_p):
        for i in range(len(figura)):
            filaF = figura[i]
            for j in range(len(filaF)):
                columnaF = filaF[j]

                if(fila_p+i >= len(plantilla) or columna_p + j >= len(plantilla[0])  ):
                  return False

                vP =plantilla[fila_p+i][columna_p + j ]

                if(columnaF == 1 and vP != 0):
                  return False

        return True

    def colocar_figura_en_plantilla(self,plantilla,figura,fila_p,columna_p):
        figuraActual = figura.get_figura_actual()
        matriz = plantilla.matriz

        figura.x = plantilla.x + TAMANIOFIGURA*columna_p
        figura.y = plantilla.y + TAMANIOFIGURA*fila_p
        figura.en_plantilla = True

        for i in range(len(figuraActual)):
            filaF = figuraActual[i]
            for j in range(len(filaF)):
                columnaF = filaF[j]

                if(columnaF == 1):
                  matriz[fila_p+i][columna_p + j ] = 2

    

    def dibujarTexto(self, font, texto, color, x, y):
        text_surface = font.render(texto, True, color)
        self.windowSurface.blit(text_surface, (x, y))
                
        
