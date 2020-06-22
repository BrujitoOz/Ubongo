import pygame
import random
pygame.init()
from Plantillas import template, CodPlantilla, CodPlantillaColission
from Fichas import pieces, pzs
from Tablero import board, brd1, brd2
from Dado import dice
from Gemas import gem
from FlechaSeleccion import arrow, flc
from Jugador1 import player, py2
from Jugador2 import playerCPU, py3
from Seleccion_Fichas import templaterect
from Deteccion_col_plantilla import templatecirclescolission


def redrawGameWindow():
    win.blit(bg, (0,0))
    tablero.draw(win)
    flecha.draw(win)
    jugador.draw(win)
    jugadorcpu.draw(win)
    for gm in gemas:
        gm.draw(win)
    plantilla.draw(win)
    for pz in piezas:
       pz.draw(win)
       pz.draw_rect_col(win)
    cuadrado.draw(win)
    for cl in cualalitos:
       cl.draw(win)
    #pieza.draw(win)
    dado.draw(win)
    if completed:
        text = font.render( 'COMPLETED: '  , 1, (0,255,0))
        win.blit(text, (390, 300))
    text2 = font.render(str(ListComp) , 1, (0,0,0))
    win.blit(text2, (10, 10))
    if dado.throwed:
        text3 = font.render(str(piezas[PieceSelect].x) , 1, (0,0,0))
        win.blit(text3, (10, 300))
        text4 = font.render(str(piezas[PieceSelect].y) , 1, (0,0,0))
        win.blit(text4, (10, 320))
    pygame.display.update()



win = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Ubongo")
bg = pygame.image.load('mesa.jpg')
clock = pygame.time.Clock()
cont = 0
ListComp = CodPlantillaColission
font = pygame.font.SysFont(' comicsans', 50, True)
jugador = player(200, 0 ,0 ,0)
y = random.choice(range(0,6))
jugadorcpu = playerCPU(265,200-(17*y),0,0)
tablero = board(165, 25, 914 , 200)
flecha = arrow(150,200,0,0)
dado = dice(1010, 600, 200,200) 
plantilla = template(250,310, 0,0)
cuadrado = templaterect(plantilla.x + 130, plantilla.y+45, 42,57)
cualalitos = []
for i in range(4):  
    cualalitos.append(templatecirclescolission(plantilla.x + 367 +( 69*i), plantilla.y+128, 20,20))
for i in range(4):  
    cualalitos.append(templatecirclescolission(plantilla.x + 367 +( 69*i), plantilla.y+128 +69 , 20,20))
for i in range(4):  
    cualalitos.append(templatecirclescolission(plantilla.x + 367 +( 69*i), plantilla.y+128 +69+69, 20,20))
for i in range(4):  
    cualalitos.append(templatecirclescolission(plantilla.x + 367 +( 69*i), plantilla.y+128 +69+69+69, 20,20))
piezas = []
#pieza = pieces(594, 412,0,0, 0)
gemas = []
x = 0 
y = 0
for j in range(6):
    for i in range(12):
        num = random.choice(range(0,6))
   
        gemas.append(gem(338 + x, 65 + y, 29 , 27, num))
        x = x +55
    y = y +32
    x = 0
#juego
run = True
ChoosePos = True
press = False
PieceSelect = 0
completed = False
asd = 0;
n = [0,0,0]

def colision():
                for i in range(16):
                    for j in range(3):
                        if piezas[j].number <= 3:
                            if  piezas[j].x < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].x + piezas[j].width:
                                if  piezas[j].y < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].y + piezas[j].height:
                                     plantilla.solv_aux[i] = False
                        elif piezas[j].number < 11:
                            if  piezas[j].rect1[0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].rect1[0]+ piezas[j].rect1[2]:
                                if  piezas[j].rect1[1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].rect1[1] + piezas[j].rect1[3]:
                                     plantilla.solv_aux[i] = False
                            if  piezas[j].rect2[0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].rect2[0]+ piezas[j].rect2[2]:
                                if  piezas[j].rect2[1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].rect2[1] + piezas[j].rect2[3]:
                                     plantilla.solv_aux[i] = False
                        elif piezas[j].number == 11:
                            if  piezas[j].rect1[0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].rect1[0]+ piezas[j].rect1[2]:
                                if  piezas[j].rect1[1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].rect1[1] + piezas[j].rect1[3]:
                                     plantilla.solv_aux[i] = False
                            if  piezas[j].rect2[0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].rect2[0]+ piezas[j].rect2[2]:
                                if  piezas[j].rect2[1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].rect2[1] + piezas[j].rect2[3]:
                                     plantilla.solv_aux[i] = False
                            if  piezas[j].rect3[0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].rect3[0]+ piezas[j].rect3[2]:
                                if  piezas[j].rect3[1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].rect3[1] + piezas[j].rect3[3]:
                                     plantilla.solv_aux[i] = False
                return

def valid_pos(x, y, p):
    if(x > 900 or y > 700):
        return True
    elif(p == 0):
        for i in [2, 3, 7, 11]:
            if piezas[p].number <= 3:
               if  piezas[p].x < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[p].x + piezas[p].width:
                  if  piezas[p].y < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[p].y + piezas[p].height:
                        return True
            elif piezas[0].number < 11:
               if  piezas[p].rect1[0] < cualalitos[i-1].x and cualalitos[i-1].x + cualalitos[i-1].width < piezas[p].rect1[0]+ piezas[p].rect1[2]:
                  if  piezas[p].rect1[1] < cualalitos[i-1].y and cualalitos[i-1].y + cualalitos[i-1].height < piezas[p].rect1[1] + piezas[p].rect1[3]:
                        redrawGameWindow()
                        return True
                #nose porque i-1 sfklndsfhdsjklashdkjgeshejk
               if  piezas[p].rect2[0] < cualalitos[i-1].x and cualalitos[i-1].x + cualalitos[i-1].width < piezas[p].rect2[0]+ piezas[p].rect2[2]:
                  if  piezas[p].rect2[1] < cualalitos[i-1].y and cualalitos[i-1].y + cualalitos[i-1].height < piezas[p].rect2[1] + piezas[p].rect2[3]:
                        redrawGameWindow()
                        return True
            elif piezas[p].number == 11:
                  if  piezas[p].rect1[0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[p].rect1[0]+ piezas[p].rect1[2]:
                      if  piezas[p].rect1[1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[p].rect1[1] + piezas[p].rect1[3]:
                           return True
                  if  piezas[p].rect2[0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[p].rect2[0]+ piezas[p].rect2[2]:
                      if  piezas[p].rect2[1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[p].rect2[1] + piezas[p].rect2[3]:
                           return True
                  if  piezas[p].rect3[0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[p].rect3[0]+ piezas[p].rect3[2]:
                      if  piezas[p].rect3[1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[p].rect3[1] + piezas[p].rect3[3]:
                           return True
    else: return False


def solve(a,b,c):

       pv = ([594,412],[662,412],[730,412],[798,412],[594,480],[662,480],[730,480],[798,480],
       [594,548],[662,548],[730,548],[798,548],[594,616],[662,616],[730,616],[798,616])
       for girf1 in range (a):
           piezas[0].subnumber = girf1
           piezas[0].width = pzs[plantilla.CodPieces[dado.number][0]][girf1].get_width()
           piezas[0].height = pzs[plantilla.CodPieces[dado.number][0]][girf1].get_height()
           for girf2 in range(b):
               piezas[1].subnumber = girf2
               piezas[1].width = pzs[plantilla.CodPieces[dado.number][1]][girf2].get_width()
               piezas[1].height = pzs[plantilla.CodPieces[dado.number][1]][girf2].get_height()
               for girf3 in range(c):
                    piezas[2].subnumber = girf3
                    piezas[2].width = pzs[plantilla.CodPieces[dado.number][2]][girf3].get_width()
                    piezas[2].height = pzs[plantilla.CodPieces[dado.number][2]][girf3].get_height()
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




while ChoosePos:  
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                        
        
#ESCOGER JUGADOR POSISION
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:  
        flecha.y += flecha.vel
    if keys[pygame.K_UP]:
        flecha.y -= flecha.vel
    if keys[pygame.K_RETURN]:
        jugador.y = flecha.y -20
        jugadorcpu.visible = True
        jugador.visible = True
        flecha.visible = False
        ChoosePos = False

    redrawGameWindow()
   

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
                        dado.number = 5
                        #dado.ThrowDice()
                        dado.throwed = True
                        cuadrado.y = cuadrado.yini + ((cuadrado.height * dado.number)+(dado.number* 13.5))
                        for i in range(3):
                           #piezas.append(pieces(594 , 412, 100 , 100, plantilla.CodPieces[dado.number][i]))
                           piezas.append(pieces(594 , 412, pzs[plantilla.CodPieces[dado.number][i]][0].get_width() , pzs[plantilla.CodPieces[dado.number][i]][0].get_height(), plantilla.CodPieces[dado.number][i]))
                           #width = background.get_width() 
                           #height = background.get_height()
                        piezas[0].visible = True
                            


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

    
    



    
                          
                          
                            
    
#Colission piezas plantilla
    if dado.throwed:
       colision()
      
       if plantilla.Is_solved():
           completed = True
# INteligence 
        
        #if not plantilla.Is_solved():

         #   if piezas[PieceSelect].Valid_pos():
          #      piezas[PieceSelect].move_down()
           #     piezas[PieceSelect].move_right()
       if asd == 0:
           for i in range (3):
               if piezas[i].number <=2  or piezas[i].number == 11 or piezas[i].number == 7:
                   n[i] = 2
               elif piezas[i].number == 3:
                   n[i] = 1
               else: 
                   n[i] = 4
           solve(n[0], n[1], n[2])
           asd = 1
      
  
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

    #rotar fichas falta 
    if keys[pygame.K_SPACE]:
       piezas[PieceSelect].subnumber = piezas[PieceSelect].subnumber +1
       if piezas[PieceSelect].subnumber > 3:
           piezas[PieceSelect].subnumber = 0
       piezas[PieceSelect].width = pzs[plantilla.CodPieces[dado.number][PieceSelect]][piezas[PieceSelect].subnumber].get_width()
       piezas[PieceSelect].height = pzs[plantilla.CodPieces[dado.number][PieceSelect]][piezas[PieceSelect].subnumber].get_height()
    redrawGameWindow()
pygame.quit()
