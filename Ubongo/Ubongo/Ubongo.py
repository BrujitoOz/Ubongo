import pygame
import random
import time
import heapq
import math
pygame.init()
from Plantillas import template, CodPlantilla, CodPlantillaColission
from Fichas import pieces, pzs
from Tablero import board, brd1, brd2
from Dado import dice
from Gemas import gem
from FlechaSeleccion import arrow, flc
from Jugador import player, py
from Seleccion_Fichas import templaterect
from Deteccion_col_plantilla import templatecirclescolission
from Reloj import stopwatch

pygame.display.set_caption("Ubongo")
win = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

CurrentPlayer = 0
time_lapsed = 0
plantilla = None
jugadores = [0, 1]
players = []
bg = pygame.image.load('mesa.jpg')
cronometro = stopwatch(30, 300,0,0)
cont = 0
font = pygame.font.SysFont('comicsans', 50, True)
font2 = pygame.font.SysFont('comicsans', 110, True)
tablero = board(65, 25, 914, 200)
flecha = arrow(150, 200, 0, 0)
dado = dice(1010, 600, 200, 200) 
piezas = []
gemas = [[],[],[],[],[],[]]
gemaux = [[],[],[],[],[],[]]
x = 0 
y = 0
for j in range(6):
    for i in range(12):
        num = random.choice(range(0, 6))
        gemas[j].append(gem(238 + x, 65 + y, 29, 27, num))
        gemaux[j].append(num)
        x = x +55
    y = y +32
    x = 0
run = True
ChoosePos = True
press = False
PieceSelect = 0
completed = False
times = [0,0]
podio = []
gempunt = []
x = 40
for i in range (6):
    gempunt.append(gem(1150 + x*i, 80, 29, 27, i))

def redrawGameWindow():
    win.blit(bg, (0, 0))
    tablero.draw(win)
    flecha.draw(win)
    x = 0
    y = 0
    for p in players:
        p.draw(win)
        for i in p.listgems:
            text = font.render( str(i), 1, (0, 0, 0))
            win.blit(text, (1155 + x, 120 +y)) 
            x = x + 40
        x= 0
        y = y +40
    for gm in gemas:
        for g in gm:       
            g.draw(win) 
    if plantilla != None:
        plantilla.draw(win)
        cuadrado.draw(win)
        #for cl in cualalitos:
            #cl.draw(win)
        if CurrentPlayer == 0:
            text = font.render("Player 1 turn", 1, (0, 0, 255))
            win.blit(text, (550, 280))
        elif CurrentPlayer == 1:
            text = font.render("Player 2 turn", 1, (255, 0, 0))
            win.blit(text, (550, 280))
        else:
            text = font.render("Player 3 turn", 1, (0, 255, 50))
            win.blit(text, (550, 280))
    for pz in piezas:
        pz.draw(win)
        pz.draw_rect_col(win)
    dado.draw(win)
    cronometro.draw(win)
    if completed:
        text = font.render( 'COMPLETED: ', 1, (0, 255, 0))
        win.blit(text, (390, 300))
        text = font.render(str(round(times[CurrentPlayer], 2)), 1, (0, 0, 0))
        win.blit(text, (105, 450))
    for g in gempunt:
        g.draw(win)
    text = font.render( 'P1', 1, (0, 0, 255))
    win.blit(text, (1075, 120))
    text = font.render( 'P2', 1, (255, 0, 0))
    win.blit(text, (1075, 160))
    text = font.render( 'P3', 1, (0, 160, 40))
    win.blit(text, (1075, 200))
    pygame.display.update()
def Drawin():
    win.blit(bg, (0, 0))
    tablero.draw(win)
    x = 0
    y = 0
    for p in players:
        p.draw(win)
        for i in p.listgems:
            text = font.render( str(i), 1, (0, 0, 0))
            win.blit(text, (1155 + x, 120 +y)) 
            x = x + 40
        x= 0
        y = y +40
    for gm in gemas:
        for g in gm:       
            g.draw(win) 
    if ganador == 0:
        text = font2.render("Player 1 wins the round", 1, (0, 0, 255))
        win.blit(text, (150, 320))
    elif ganador ==1:
        text = font2.render("Player 2 wins the round", 1, (255, 0, 0))
        win.blit(text, (150, 320))
    else:
        text = font2.render("Player 3 wins the round", 1, (0, 255, 50))
        win.blit(text, (150, 320))
    for g in gempunt:
        g.draw(win)
    text = font.render( 'P1', 1, (0, 0, 255))
    win.blit(text, (1075, 120))
    text = font.render( 'P2', 1, (255, 0, 0))
    win.blit(text, (1075, 160))
    text = font.render( 'P3', 1, (0, 160, 40))
    win.blit(text, (1075, 200))
    pygame.display.update()
def colision():
    for i in range(16):
        for j in range(3):
            for c in range(piezas[j].cantrect):
                if  piezas[j].rect[c][0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].rect[c][0]+ piezas[j].rect[c][2]:
                    if  piezas[j].rect[c][1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].rect[c][1] + piezas[j].rect[c][3]:
                        plantilla.solv_aux[i] = False
    return
#ver si las posiciones de las fichas son validas pra FuerzaBruta
#validar posiciones para BackTacking y Programacion dinamica
def valid_pos_FBT(x, y, j, Cini):
    if(piezas[j].x + piezas[j].width > 900 or piezas[j].y +piezas[j].height > 700):
        return False
    for i in range(16):
        for c in range(piezas[j].cantrect):
            if  piezas[j].rect[c][0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].rect[c][0]+ piezas[j].rect[c][2]:
                 if  piezas[j].rect[c][1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].rect[c][1] + piezas[j].rect[c][3]:
                        if plantilla.solv_aux[i] == False:
                            plantilla.solv_aux = Cini.copy()
                            return False
                        plantilla.solv_aux[i] = False   
    return True
def find_piece_wo_fit():
    completed = True
    for i in range (3):
        if piezas[i].fited == False:
            return i
    return 5
#Crear el cache de Programacion Dinamica
def Create_cache(x, y, j):
    if(piezas[j].x + piezas[j].width > 900 or piezas[j].y +piezas[j].height > 700):
        return False
    for i in range(16):
        for c in range(piezas[j].cantrect):
            if  piezas[j].rect[c][0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].rect[c][0]+ piezas[j].rect[c][2]:
                 if  piezas[j].rect[c][1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].rect[c][1] + piezas[j].rect[c][3]:
                        if plantilla.solv_aux2[i] == False:
                            return False  
    return True
#Encontrar alguna pieza que no esté encajada para moverla 
#Solucion con programacion Dinamica
def solve_w_DP():
    pv = ([594, 412], [662, 412], [730, 412], [798, 412], [594, 480], [662, 480], [730, 480], [798, 480],
          [594, 548], [662, 548], [730, 548], [798, 548], [594, 616], [662, 616], [730, 616], [798, 616])
    cache = [[], [], []]
    for n in range(3):
        for ver in range(piezas[n].cantver):
            for rot in range(piezas[n].numgir):
                cache[n].append([])
    def solveDPR():
        Cini = plantilla.solv_aux.copy()
        piece_act = find_piece_wo_fit()
        if piece_act == 5:
            return True
        for gv in range(piezas[piece_act].cantver):
            piezas[piece_act].version = gv
            for g in range(piezas[piece_act].numgir):
                piezas[piece_act].subnumber = g
                piezas[piece_act].width = pzs[gv][plantilla.CodPieces[dado.number][piece_act]][g].get_width()
                piezas[piece_act].height = pzs[gv][plantilla.CodPieces[dado.number][piece_act]][g].get_height()
                if not cache[piece_act][g+(piezas[piece_act].numgir*gv)]:
                    for i in range(16):
                        piezas[piece_act].x = pv[i][0]
                        piezas[piece_act].y = pv[i][1]
                        redrawGameWindow()
                        if Create_cache(piezas[piece_act].x, piezas[piece_act].y, piece_act):
                            cache[piece_act][g+(piezas[piece_act].numgir*gv)].append(i)
                for i in cache[piece_act][g+ (piezas[piece_act].numgir*gv)]:
                    piezas[piece_act].x = pv[i][0]
                    piezas[piece_act].y = pv[i][1]
                    redrawGameWindow()
                    if valid_pos_FBT(piezas[piece_act].x, piezas[piece_act].y, piece_act, Cini):
                        piezas[piece_act].fited = True
                        if solveDPR():
                            plantilla.solv_aux = plantilla.CodColission.copy()
                            return True
                        plantilla.solv_aux = Cini.copy()
                        piezas[piece_act].fited = False
        return False
    return solveDPR()
#Solucion con Backtracking
def solve_w_BT():
    Cini = plantilla.solv_aux.copy()
    pv = ([594,412],[662,412],[730,412],[798,412],[594,480],[662,480],[730,480],[798,480],
          [594,548],[662,548],[730,548],[798,548],[594,616],[662,616],[730,616],[798,616])
    piece_act = find_piece_wo_fit()
    if piece_act == 5:
        return True
    for gv in range(piezas[piece_act].cantver):
        piezas[piece_act].version = gv
        for g in range(piezas[piece_act].numgir):    
            piezas[piece_act].subnumber = g
            piezas[piece_act].width = pzs[gv][plantilla.CodPieces[dado.number][piece_act]][g].get_width()
            piezas[piece_act].height = pzs[gv][plantilla.CodPieces[dado.number][piece_act]][g].get_height()
            for i in range(16):
                piezas[piece_act].x = pv[i][0]
                piezas[piece_act].y = pv[i][1]
                redrawGameWindow()
                if valid_pos_FBT(piezas[piece_act].x, piezas[piece_act].y, piece_act, Cini):
                    piezas[piece_act].fited = True
                    #redrawGameWindow()
                    if solve_w_BT():
                        plantilla.solv_aux = plantilla.CodColission.copy()
                        return True
                    plantilla.solv_aux = Cini.copy()
                    piezas[piece_act].fited = False
    return False
#Resolver con Fuerza Bruta
def valid_pos(x, y, p):
    if(x > 900 or y > 700):
        return True
    return False
def solve_w_FB():
    pv = ([594,412],[662,412],[730,412],[798,412],[594,480],[662,480],[730,480],[798,480],
       [594,548],[662,548],[730,548],[798,548],[594,616],[662,616],[730,616],[798,616])
    for vp1 in range (piezas[0].cantver): #
        piezas[0].version = vp1
        for vp2 in range (piezas[1].cantver):
            piezas[1].version = vp2
            for vp3 in range (piezas[2].cantver):
                piezas[2].version = vp3
                for girf1 in range (piezas[0].numgir):
                    piezas[0].subnumber = girf1
                    piezas[0].width = pzs[vp1][plantilla.CodPieces[dado.number][0]][girf1].get_width()
                    piezas[0].height = pzs[vp1][plantilla.CodPieces[dado.number][0]][girf1].get_height()
                    for girf2 in range(piezas[1].numgir):
                        piezas[1].subnumber = girf2
                        piezas[1].width = pzs[vp2][plantilla.CodPieces[dado.number][1]][girf2].get_width()
                        piezas[1].height = pzs[vp2][plantilla.CodPieces[dado.number][1]][girf2].get_height()
                        for girf3 in range(piezas[2].numgir):
                                piezas[2].subnumber = girf3
                                piezas[2].width = pzs[vp3][plantilla.CodPieces[dado.number][2]][girf3].get_width()
                                piezas[2].height = pzs[vp3][plantilla.CodPieces[dado.number][2]][girf3].get_height()
                                for f1 in range(16):
                                    piezas[0].x = pv[f1][0]
                                    piezas[0].y = pv[f1][1]
                                    if (valid_pos(piezas[0].x + piezas[0].width , piezas[0].y +  piezas[0].height,0)):
                                        continue
                                    for f2 in range(16):
                                        piezas[1].x = pv[f2][0]
                                        piezas[1].y = pv[f2][1]
                                        if (valid_pos(piezas[1].x + piezas[1].width, piezas[1].y + piezas[1].height,1)):
                                            continue
                                        for f3 in range(16):
                                            piezas[2].x = pv[f3][0]
                                            piezas[2].y = pv[f3][1]
                                            if (valid_pos(piezas[2].x + piezas[2].width, piezas[2].y + piezas[2].height,2)):
                                                continue
                                            redrawGameWindow()
                                            colision()
                                            if plantilla.Is_solved():
                                                completed = True
                                                return True
#Escoger poscion
def winner():
    global times, podio
    #cambiar por numolkayer
    for j in range(2):
        min = math.inf
        for i in range(len(times)):
            if times[i] < min:
                min = times[i]
                ganador = i
        podio.append(ganador)
        times[ganador] = math.inf       
    return podio[0]
def cpumove(np, turno):
    global gemaux
    cont = 0
    aux = players[np].listgems.copy()
    
    if turno == 0:
        return
    for i in range(6):
        gemmax = -1
        index = -1
        pf = -1
        pfindex = -1
        aux2 = [0]*6
        for i in range(6):
            if aux[i] > gemmax:
                gemmax = aux[i]
                index = i
        aux[index] = -1
        for j in range (players[np].minpos, players[np].maxpos + 1):
            if j < 0 or j > 5:
                continue
            players[np].pos = j
            players[np].y = 40 + (30*j)
            Drawin()
            for g in range(2):
                if gemaux[j][g] == index:
                    aux2[j] = aux2[j] + 1
        for k in range (6):
            if aux2[k] > pf:
                pf = aux2[k]
                pfindex = k
        if pf != 0:
            players[np].pos = pfindex
            players[np].y = 40 + (30* players[np].pos)
            Drawin()
            return 
                        
def Start():
    portada = pygame.image.load('Portada.png')
    cont = 0
    non_start = True
    font = pygame.font.SysFont(' comicsans', 50, True)
    while non_start: 
        clock.tick(8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.blit(portada, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return     
        if cont % 5 == 0:
            text = font.render( 'Press enter to start: ', 1, (0, 0, 0))
            win.blit(text, (400, 600))
        if keys[pygame.K_RETURN]:
            return
        pygame.display.update()
        cont = cont + 1
def Config_screen():
    conf = pygame.image.load('Pant_config.jpg')
    flecha = arrow(395, 365, 0, 0)
    dificultad = True
    numplay = False
    numpieces = False
    fpos = [[(395,365), (585,365), (840,365)],[(515,475),(767,475)],[(500,585),(770,585)]]
    flecont = 0
    lvl = 0
    np = 0
    npz = 0
    while True: 
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if dificultad:
            if keys[pygame.K_RIGHT]:
                flecont += 1
                if flecont > 2:
                    flecont = 0
                flecha.x, flecha.y = fpos[0][flecont]
            elif keys[pygame.K_LEFT]:
                flecont -= 1
                if flecont < 0:
                    flecont = 2
                flecha.x, flecha.y = fpos[0][flecont]
            elif keys[pygame.K_RETURN]:
                flecha.x, flecha.y = fpos[1][0]
                dificultad = False
                numplay = True
                lvl = flecont
        elif numplay:
            if keys[pygame.K_RIGHT]:
                flecont += 1
                if flecont > 1:
                    flecont = 0
                flecha.x, flecha.y = fpos[1][flecont]
            elif keys[pygame.K_LEFT]:
                flecont -= 1
                if flecont < 0:
                    flecont = 1
                flecha.x, flecha.y = fpos[1][flecont]
            elif keys[pygame.K_RETURN]:
                flecha.x, flecha.y = fpos[2][0]
                numplay = False
                numpieces = True
                np = flecont
        elif numpieces:
            if keys[pygame.K_RIGHT]:
                flecont += 1
                if flecont > 1:
                    flecont = 0
                flecha.x, flecha.y = fpos[2][flecont]
            elif keys[pygame.K_LEFT]:
                flecont -= 1
                if flecont < 0:
                    flecont = 1
                flecha.x, flecha.y = fpos[2][flecont]
            elif keys[pygame.K_RETURN]:
                npz = flecont
                return lvl, np, npz
        win.blit(conf, (0, 0))
        flecha.draw(win)        
        pygame.display.update()
def ChoosePosition():
    x = 65
    y = random.choice(range(0, 6))
    for i in range(2):
        players.append(player(100 +(x*i) , 40+(30*y), 0, 0, i, y))
    pos = [(50,70),(50,100),(50,130),(50,160),(50,190),(50, 220)]
    global ChoosePos
    while ChoosePos:  
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:  
            flecha.num += 1
            if 5 < flecha.num:
                flecha.num = 0
        if keys[pygame.K_UP]:
            flecha.num -= 1
            if flecha.num < 0:
                flecha.num = 5
        if keys[pygame.K_RETURN]:
            players[0].y = flecha.y - 30
            players[1].visible = True
            players[0].visible = True
            players[0].pos = flecha.num
            flecha.visible = False
            ChoosePos = False
        flecha.x, flecha.y = pos[flecha.num]
        redrawGameWindow()      
def FinalScreen():
    auxarr = [[], []]
    maxarr = [0] * 4
    aux = 0
    winner = -1
    for ply in players:
        auxarr[aux] = ply.listgems.copy()
        aux += 1
    while maxarr[0] == maxarr[1]:
        if len(auxarr[0]) == 0:
            winner = -1
            break
        for i in range (2):
            maxarr[i] = max(auxarr[i])
            auxarr[i].remove(maxarr[i])
        winner = maxarr.index(max(maxarr))
    run = True
    while run:
        clock.tick(27)   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.blit(bg, (0, 0))
        if winner == 0:
            text = font2.render("Player 1 wins", 1, (0, 0, 255))
            win.blit(text, (550, 280))
        elif winner == 1:
            text = font2.render("Player 2 wins", 1, (255, 0, 0))
            win.blit(text, (550, 280))
        elif winner == 2:
            text = font2.render("Player 3 wins", 1, (0, 255, 50))
            win.blit(text, (550, 280))
        else:
            text = font2.render("Draw", 1, (50, 150, 50))
            win.blit(text, (550, 280))
        for g in gempunt:
            g.draw(win)
        text = font.render( 'P1', 1, (0, 0, 255))
        win.blit(text, (1075, 120))
        text = font.render( 'P2', 1, (255, 0, 0))
        win.blit(text, (1075, 160))
        text = font.render( 'P3', 1, (0, 160, 40))
        win.blit(text, (1075, 200))
        x = 0
        y = 0
        for p in players:
            for i in p.listgems:
                text = font.render( str(i), 1, (0, 0, 0))
                win.blit(text, (1155 + x, 120 +y)) 
                x = x + 40
            x= 0
            y = y +40
        pygame.display.update()
#0 == playe 1 == cpu 
def Play():
    global run, PieceSelect, completed, asd, piezas, times, CurrentPlayer, plantilla, cuadrado, cualalitos, ganador, podio
    plantilla = template(250, 310, 0, 0, random.choice(range(0,6)) )
    cuadrado = templaterect(plantilla.x + 130, plantilla.y+45, 42,57)
    cualalitos = []
    for i in range(4):  
        cualalitos.append(templatecirclescolission(plantilla.x + 367 +( 69*i), plantilla.y+128, 20, 20))
    for i in range(4):  
        cualalitos.append(templatecirclescolission(plantilla.x + 367 +( 69*i), plantilla.y+128 +69 , 20, 20))
    for i in range(4):  
        cualalitos.append(templatecirclescolission(plantilla.x + 367 +( 69*i), plantilla.y+128 +69+69, 20, 20))
    for i in range(4):  
        cualalitos.append(templatecirclescolission(plantilla.x + 367 +( 69*i), plantilla.y+128 +69+69+69, 20, 20))
    redrawGameWindow()
    for turnos in range (2):
        plantilla.number = random.choice(range(0,10))
        plantilla.Actualizar()
        run = True
        for pys in range(2):
            CurrentPlayer = pys
            run = True
            completed = False
            if turnos == 0:
                completed = False
            if jugadores[CurrentPlayer] == 0:
                piezas = []
                while run:
                    clock.tick(27)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False
                    #PARA LANZAR EL DADO Y SELECCION DE FICHAS
                        elif event.type == pygame.MOUSEBUTTONUP:
                                    pos = pygame.mouse.get_pos()
                                    if dado.hitbox[0] < pos[0] and pos[0] < dado.hitbox[0] + dado.hitbox[2]:
                                        if dado.hitbox[1] < pos[1] and pos[1] < dado.hitbox[1] + dado.hitbox[3]:
                                            #dado.number = 3
                                            dado.ThrowDice()
                                            start_time = time.time()
                                            dado.throwed = True
                                            cuadrado.y = cuadrado.yini + ((cuadrado.height * dado.number)+(dado.number* 13.5))
                                            for i in range(3):    
                                                piezas.append(pieces(594 , 412, pzs[0][plantilla.CodPieces[dado.number][i]][0].get_width() , pzs[0][plantilla.CodPieces[dado.number][i]][0].get_height(), plantilla.CodPieces[dado.number][i]))
                                            piezas[0].visible = True
                                            piezas[1].visible = False
                                            piezas[2].visible = False
                                            
                                    #Para seleccionar la ficha p
                                    if cuadrado.y < pos[1] and pos[1] < cuadrado.y + cuadrado.height:
                                        if cuadrado.x < pos[0] and pos[0] < cuadrado.x + cuadrado.width:
                                            cuadrado.visible1 = True
                                            cuadrado.visible2 = False
                                            cuadrado.visible3 = False
                                            PieceSelect = 0
                                        if cuadrado.x + cuadrado.width< pos[0] and pos[0] < cuadrado.x + (cuadrado.width*2):
                                            cuadrado.visible2 = True
                                            cuadrado.visible1 = False
                                            cuadrado.visible3 = False
                                            piezas[1].visible = True
                                            PieceSelect = 1
                                        if cuadrado.x + (cuadrado.width*2)< pos[0] and pos[0] < cuadrado.x + (cuadrado.width*3):
                                            cuadrado.visible3 = True
                                            cuadrado.visible2 = False
                                            cuadrado.visible1 = False
                                            piezas[2].visible = True
                                            PieceSelect = 2

                #Colission piezas plantilla y armarse_cpu
                    if dado.throwed:
                        colision()
                        if plantilla.Is_solved():
                            completed = True
                            end_time = time.time()
                            times[CurrentPlayer] =  end_time - start_time
                            run = False
                            dado.throwed = False
                #MIVIMIENTO DE FICHAS
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_DOWN]:
                        piezas[PieceSelect].move_down()
                    if keys[pygame.K_UP]:
                        piezas[PieceSelect].move_up()
                    if keys[pygame.K_RIGHT]:
                        piezas[PieceSelect].move_right()
                    if keys[pygame.K_LEFT]:
                        piezas[PieceSelect].move_left()
                    #rotar fichas
                    if keys[pygame.K_SPACE]:
                        piezas[PieceSelect].subnumber = piezas[PieceSelect].subnumber +1
                        if piezas[PieceSelect].subnumber > 3:
                            piezas[PieceSelect].subnumber = 0
                        piezas[PieceSelect].width = pzs[piezas[PieceSelect].version][plantilla.CodPieces[dado.number][PieceSelect]][piezas[PieceSelect].subnumber].get_width()
                        piezas[PieceSelect].height = pzs[piezas[PieceSelect].version][plantilla.CodPieces[dado.number][PieceSelect]][piezas[PieceSelect].subnumber].get_height()
                    if keys[pygame.K_v]:
                        piezas[PieceSelect].version += 1
                        if piezas[PieceSelect].version > 1:
                            piezas[PieceSelect].version = 0
                    redrawGameWindow()
                acept = True
                while acept:
                    clock.tick(27)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_RETURN]:
                        acept = False
                    redrawGameWindow()
            else:
                run = True
                piezas = []
                plantilla.number = random.choice(range(0,10))
                plantilla.Actualizar()
                while run:
                    clock.tick(27)
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False
                    #PARA LANZAR EL DADO Y SELECCION DE FICHAS
                        
                        elif event.type == pygame.MOUSEBUTTONUP:
                                    pos = pygame.mouse.get_pos()
                                    if dado.hitbox[0] < pos[0] and pos[0] < dado.hitbox[0] + dado.hitbox[2]:
                                        if dado.hitbox[1] < pos[1] and pos[1] < dado.hitbox[1] + dado.hitbox[3]:
                                            #dado.number = 3
                                            dado.ThrowDice()
                                            start_time = time.time()
                                            dado.throwed = True
                                            cuadrado.y = cuadrado.yini + ((cuadrado.height * dado.number)+(dado.number* 13.5))
                                            for i in range(3):    
                                                piezas.append(pieces(594 , 412, pzs[0][plantilla.CodPieces[dado.number][i]][0].get_width() , pzs[0][plantilla.CodPieces[dado.number][i]][0].get_height(), plantilla.CodPieces[dado.number][i]))
                                            piezas[0].visible = True    
                    if dado.throwed:
                        if Dificulty == 0:
                            solve_w_FB()
                        elif Dificulty == 1:
                            solve_w_FB()
                        else:
                            solve_w_DP()
                        completed = True
                        end_time = time.time()
                        times[CurrentPlayer] =  end_time - start_time 
                        dado.throwed = False
                        run = False
                    redrawGameWindow()
                acept = True
                while acept:
                    clock.tick(27)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_RETURN]:
                        acept = False
                    redrawGameWindow()
        completed = False
        podio = []
        ganador = winner()
        aux = 3
        for pys in podio:
            aux = aux -1
            players[pys].maxpos = players[pys].pos + aux
            players[pys].minpos = players[pys].pos - aux
            if jugadores[pys] == 0:
                run = True
                while run:
                    clock.tick(27)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_DOWN]:
                        players[pys].move_down()
                    if keys[pygame.K_UP]:
                        players[pys].move_up()
                    if keys[pygame.K_RETURN]:
                            run = False
                    Drawin()
            else: 
                cpumove(pys, turnos)
                Drawin()
            run = True
            for i in range (2):
                gemaux[players[pys].pos].pop(0)
                for g in gemas[players[pys].pos]:
                    if g.visible == True:
                        g.visible = False
                        players[pys].listgems[g.number] += 1
                        break
                Drawin()  
Start()
Dificulty, NumJugadores, NumPiezas = Config_screen()
win = pygame.display.set_mode((1400, 800))
ChoosePosition()
Play()
FinalScreen()



   