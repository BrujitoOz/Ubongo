import pygame
import random
pygame.init()


#Imagenes 
win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Ubongo")
bg = pygame.image.load('mesa.jpg')
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
        win.blit(brd, (self.x , self.y))

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
       
    def draw(self, win):
        win.blit(self.pnt[self.number], (self.x, self.y))
 
        
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
    
    pzs1 = [pygame.image.load('ficha1.png') , pygame.image.load('ficha1_1.png')]
    def __init__(self,x,y,width,height, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 34
        self.number = number
        self.subnumber = 0
        self.visible = False
    def draw(self, win):
        if self.visible:
            win.blit(pzs[self.number], (self.x, self.y))

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
    text3 = font.render(str(cont) , 1, (0,0,0))
    win.blit(text3, (10, 300))
    pygame.display.update()


#cREACION DE OBJETOS
cont = 0
ListComp = CodPlantillaColission
font = pygame.font.SysFont('comicsans', 50, True )
jugador = player(200, 0 ,0 ,0)
y = random.choice(range(0,6))
jugadorcpu = playerCPU(265,200-(17*y),0,0)
tablero = board(165, 100, 914 , 200)
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
for i in range(12):
    num = random.choice(range(0,6))
   
    gemas.append(gem(326 + x, 208 + y, 29 , 27, num))
    x = x +47

#juego
run = True
ChoosePos = True
press = False
PieceSelect = 0
completed = False

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
    
    
    

    cont = 0
    ListComp = [] 
    #Con este no funciona no se porque 
    #ListComp = CodPlantillaColission
    ListComp = [True, True, True ,False, True, True, True,True, True, True,True, True, True,False,False,False]

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            run = False
#PARA LANZAR EL DADO Y SELECCION DE FICHAS
       elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if dado.hitbox[0] < pos[0] and pos[0] < dado.hitbox[0] + dado.hitbox[2]:
                    if dado.hitbox[1] < pos[1] and pos[1] < dado.hitbox[1] + dado.hitbox[3]:
                        dado.ThrowDice()
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

#Colission piezas plantilla
    if dado.throwed:
        for i in range(16):
            for j in range(3):
                if  piezas[j].x < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].x + piezas[j].width:
                    if  piezas[j].y < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].y + piezas[j].height:
                         ListComp[i] = False
        for i in ListComp:
            if i == False:
                cont += 1
            if cont == 16:
                completed = True
                    
   

               
   
    cont = 0
    ListComp = [] 
    ListComp = CodPlantillaColission
  
#MIVIMIENTO DE FICHAS
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:

       piezas[PieceSelect].y += piezas[PieceSelect].vel
    if keys[pygame.K_UP]:
       piezas[PieceSelect].y -= piezas[PieceSelect].vel
    if keys[pygame.K_RIGHT]:
       piezas[PieceSelect].x += piezas[PieceSelect].vel
    if keys[pygame.K_LEFT]:
       piezas[PieceSelect].x -= piezas[PieceSelect].vel
    if keys[pygame.K_SPACE]:
       pieza.subnumber += 1
       if pieza.subnumber > 1:
           pieza.subnumber = 0
 

    redrawGameWindow()


pygame.quit()