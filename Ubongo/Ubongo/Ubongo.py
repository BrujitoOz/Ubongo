import pygame
import random
pygame.init()


#Imagenes 
win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Ubongo")
bg = pygame.image.load('mesa.jpg')
brd1 = pygame.image.load('tablero1.png')
brd2 = pygame.image.load('tablero2.png')
brd = pygame.image.load('tablero.jfif')
gema = pygame.image.load('gema2.png')
py2 = pygame.image.load('p2.png')
py3 = pygame.image.load('p3.png')
flc = pygame.image.load('flecha.png')
pzs =  [pygame.image.load('ficha1.png') , pygame.image.load('ficha2.png'), pygame.image.load('ficha3.png'), pygame.image.load('ficha4.png'), pygame.image.load('ficha5.png'), pygame.image.load('ficha6.png'),pygame.image.load('ficha7.png'), pygame.image.load('ficha8.png'), pygame.image.load('ficha9.png'), pygame.image.load('ficha10.png'), pygame.image.load('ficha11.png'), pygame.image.load('ficha12.png')]
clock = pygame.time.Clock()
#Codigos de las fichas de la platinlla y sobre espacios en blanco
CodPlantilla = [[(8,6,4),(11,0,7),(0,8,6),(3,0,10),(0,10,6),(6,7,3)],[(8,6,4),(11,0,7),(0,8,6),(3,0,10),(0,10,6),(6,7,3)]]
CodPlantillaColission = [True, True, True ,False, True, True, True,True, True, True,True, True, True,False,False,False]

#tablero
class board(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, win):
        win.blit(brd1, (self.x , self.y))
        win.blit(brd2, (self.x +475, self.y))

#dado
class dice(object):
    dd = [pygame.image.load('dado5.png'), pygame.image.load('dado4.png'), pygame.image.load('dado6.png') , pygame.image.load('dado3.png') , pygame.image.load('dado2.png') , pygame.image.load('dado1.png')]
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = 0
        self.hitbox = (self.x,self.y, 65,57)
        self.throwed = False




    def ThrowDice(self):
        self.number = random.choice(range(0,6))
  

    def draw(self, win):
        pygame.draw.circle(win, (0,0,0), (self.x +32, self.y +29),65)
        win.blit(self.dd[self.number], (self.x , self.y))
        pygame.draw.rect(win, (0,255,0), self.hitbox,2)
    
#gemas
class gem(object):
    gema = [pygame.image.load('gema1.png'), pygame.image.load('gema2.png'), pygame.image.load('gema3.png'), pygame.image.load('gema4.png'), pygame.image.load('gema5.png'), pygame.image.load('gema6.png')]
    def __init__(self,x,y,width,height, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = number
    def draw(self, win):
        win.blit(self.gema[self.number], (self.x, self.y))

#plantillas
class template(object):
    pnt = [pygame.image.load('plantilla1.png'), pygame.image.load('plantilla2.png') ]
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = 0
        self.CodPieces = CodPlantilla[self.number] 
        self.CodColission = CodPlantillaColission[self.number]
        self.completed = False
        self.solv_aux = [True, True, True ,False, True, True, True,True, True, True,True, True, True,False,False,False]
       
    def draw(self, win):
        win.blit(self.pnt[self.number], (self.x, self.y))
    def Is_solved (self):
        cont_solv = 0
        
        
        for i in self.solv_aux:
            if i == False:
                cont_solv += 1
            if cont_solv >= 16:
                return True
        self.solv_aux = [True, True, True ,False, True, True, True,True, True, True,True, True, True,False,False,False]
        return False

 
        
#Cuadraditos para la cilission de las plantilals
class templatecirclescolission(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = 20

    def draw(self, win):
         pygame.draw.rect(win, (0,255,0), (self.x, self.y, self.width, self.height) ,2)
       
#cuadraditos de seleccions de ficha
class templaterect(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.yini = self.y
        self.visible1 = True
        self.visible2 = False
        self.visible3 = False
 
    def draw(self, win):
        if self.visible1:
            pygame.draw.rect(win, (0,255,0), (self.x, self.y, self.width, self.height) ,2)
        if self.visible2:
            pygame.draw.rect(win, (0,255,0), (self.x + self.width, self.y, self.width , self.height) ,2)
        if self.visible3:
            pygame.draw.rect(win, (0,255,0), (self.x +self.width+self.width, self.y, self.width, self.height) ,2)
    



#piezas 
class pieces(object):
    
    #pzs1 = [pygame.image.load('ficha1.png') , pygame.image.load('ficha1_1.png')]
    
    def __init__(self,x,y,width,height, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 34
        self.number = number
        self.subnumber = 0
        self.visible = True
        self.rect1 = []
        self.rect2 = []
        self.rect3 = []
        self.create_rect_col()
    def draw(self, win):
        if self.visible:
            win.blit(pzs[self.number], (self.x, self.y))

    def move_down(self):
        self.y += self.vel
    def move_up(self):
        self.y -= self.vel
    def move_right(self):
        self.x += self.vel
    def move_left(self):
        self.x -= self.vel
    def Puzzle_Assemble(self):
        pass
    def Valid_pos(self):
        if self.x <= 764 and self.y <= 611:
            return True
        return False
    def create_rect_col(self):     
            if self.number == 4:
                self.rect1 = [self.x , self.y, (self.width/2), self.height]
                self.rect2 = [self.x + (self.width/2) , self.y + (self.height/2), (self.width/2), (self.height /2 )]  
            elif self.number == 5:
                self.rect1 = [self.x , self.y, (self.width/2), (self.height)]
                self.rect2 = [(self.x + (self.width/2)) , self.y + (self.height/3), (self.width/2), (self.height /3 )]
            elif self.number == 6:
                self.rect1 = [self.x , self.y, (self.width/3), (self.height/2)]
                self.rect2 = [(self.x ) , self.y + (self.height/2), (self.width), (self.height /2 )]
            elif self.number == 7:
                self.rect1 = [self.x , self.y, (self.width/2), (self.height/3)*2]
                self.rect2 = [self.x + (self.width/2), self.y + (self.height/3),   (self.width/2), (self.height /3 )*2]
            elif self.number == 8:
                self.rect1 = [self.x , self.y, (self.width/2), self.height]
                self.rect2 = [self.x +(self.width/2)  , self.y , (self.width/2), (self.height /4 )]
            elif self.number == 9:
                self.rect1 = [self.x , self.y, (self.width/2), self.height]
                self.rect2 = [self.x +(self.width/2)  , self.y , (self.width/2), (self.height /4 )]
            elif self.number == 11:
                self.rect1 = [self.x , self.y, (self.width/3), (self.height/3)]
                self.rect2 = [self.x +(self.width/3)  , self.y , (self.width/3), (self.height)]
                self.rect3 = [self.x +((self.width/3)*2)  , self.y + ((self.width/3)*2) , (self.width/3), (self.height /3 )]


    def draw_rect_col(self, win):
        if self.number <= 3:
            pygame.draw.rect(win, (0,0,255), (self.x, self.y, self.width, self.height) ,2)
        else:
            if self.number == 4:
                self.rect1 = [self.x , self.y, (self.width/2), self.height]
                self.rect2 = [self.x + (self.width/2) , self.y + (self.height/2), (self.width/2), (self.height /2 )] 
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255),(self.rect2) ,2)
            elif self.number == 6:
                self.rect1 = [self.x , self.y, (self.width/3), (self.height/2)]
                self.rect2 = (self.x  , self.y + (self.height/2), (self.width), (self.height /2 ))
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255), (self.rect2) ,2)
            elif self.number == 7:
                self.rect1 = [self.x , self.y, (self.width/2), (self.height/3)*2]
                self.rect2 = (self.x + (self.width/2), self.y + (self.height/3),   (self.width/2), (self.height /3 )*2)
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255), (self.rect2) ,2)
            elif self.number == 8:
                self.rect1 = [self.x , self.y, (self.width/2), self.height]
                self.rect2 = [self.x +(self.width/2)  , self.y , (self.width/2), (self.height /4 )]
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255), (self.rect2) ,2)
            elif self.number == 11:
                self.rect1 = [self.x , self.y, (self.width/3), (self.height/3)]
                self.rect2 = [self.x +(self.width/3)  , self.y , (self.width/3), (self.height)]
                self.rect3 = [self.x +((self.width/3)*2)  , self.y + ((self.width/3)*2) , (self.width/3), (self.height /3 )]
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255), (self.rect2) ,2)
                pygame.draw.rect(win, (0,0,255), (self.rect3) ,2)
            

#jUGADOR
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = False
    def draw(self, win):
        if self.visible:
            win.blit(py2, (self.x , self.y))

#JUGADOR CPU
class playerCPU(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = False
    def draw(self, win):
        if self.visible:
            win.blit(py3, (self.x , self.y))

#FELCHITA DE SELECION
class arrow(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.visible = True
    def draw(self, win):
        if self.visible:
            win.blit(flc, (self.x , self.y))


#PARA DIBUJAR TODO
def redrawGameWindow():
    

    win.blit(bg, (0,0))
    
    tablero.draw(win)
    flecha.draw(win)
    jugador.draw(win)
    jugadorcpu.draw(win)
    win.blit(gema, (420,208))
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
        text = font.render('COMPLETED: '  , 1, (0,255,0))
        win.blit(text, (390, 300))
    text2 = font.render(str(ListComp) , 1, (0,0,0))
    win.blit(text2, (10, 10))
    if dado.throwed:
        text3 = font.render(str(piezas[PieceSelect].x) , 1, (0,0,0))
        win.blit(text3, (10, 300))
        text4 = font.render(str(piezas[PieceSelect].y) , 1, (0,0,0))
        win.blit(text4, (10, 320))
    pygame.display.update()


#cREACION DE OBJETOS
cont = 0
ListComp = CodPlantillaColission
font = pygame.font.SysFont('comicsans', 50, True )
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
                        dado.number = 2
                        #dado.ThrowDice()
                        dado.throwed = True
                        cuadrado.y = cuadrado.yini + ((cuadrado.height * dado.number)+(dado.number* 13.5))
                        for i in range(3):
                           #piezas.append(pieces(594 , 412, 100 , 100, plantilla.CodPieces[dado.number][i]))
                           piezas.append(pieces(594 , 412, pzs[plantilla.CodPieces[dado.number][i]].get_width() , pzs[plantilla.CodPieces[dado.number][i]].get_height(), plantilla.CodPieces[dado.number][i]))
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

    
    def colision():
                for i in range(16):
                    for j in range(3):
                        if piezas[j].number <= 3:
                            if  piezas[j].x < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].x + piezas[j].width:
                                if  piezas[j].y < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].y + piezas[j].height:
                                     plantilla.solv_aux[i] = False
                        elif piezas[j].number == 4 or piezas[j].number == 6 or piezas[j].number == 8 or piezas[j].number == 7:
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



    def solve():
        pv = ([594,412],[662,412],[730,412],[798,412],[594,480],[662,480],[730,480],[798,480],
        [594,548],[662,548],[730,548],[798,548],[594,616],[662,616],[730,616],[798,616])

        for f1 in range(16):
             piezas[0].x = pv[f1][0]
             piezas[0].y = pv[f1][1]
             for f2 in range(16):
                  piezas[1].x = pv[f2][0]
                  piezas[1].y = pv[f2][1]
                  for f3 in range(16):
                       piezas[2].x = pv[f3][0]
                       piezas[2].y = pv[f3][1]
                       redrawGameWindow()
                       colision()
                       if plantilla.Is_solved():
                           completed = True
                           return True
                          
                          
                            
    
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
           solve()
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
    #if keys[pygame.K_SPACE]:
      # pieza.subnumber += 1
       #if pieza.subnumber > 1:
        #   pieza.subnumber = 0
    redrawGameWindow()


pygame.quit()