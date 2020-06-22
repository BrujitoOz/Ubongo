import pygame

pzs =  [[(pygame.image.load('ficha1.png')), (pygame.image.load('ficha1_1.png')),(pygame.image.load('ficha1.png')), (pygame.image.load('ficha1_1.png'))],
       [(pygame.image.load('ficha2.png')), (pygame.image.load('ficha2_1.png')),(pygame.image.load('ficha2.png')), (pygame.image.load('ficha2_1.png'))],
       [(pygame.image.load('ficha3.png')), (pygame.image.load('ficha3_1.png')),(pygame.image.load('ficha3.png')), (pygame.image.load('ficha3_1.png'))], 
       [(pygame.image.load('ficha4.png')), (pygame.image.load('ficha4.png')),(pygame.image.load('ficha4.png')), (pygame.image.load('ficha4.png'))],
       [(pygame.image.load('ficha5.png')), (pygame.image.load('ficha5_1.png')),(pygame.image.load('ficha5_2.png')), (pygame.image.load('ficha5_3.png'))],
       [(pygame.image.load('ficha6.png')), (pygame.image.load('ficha6_1.png')),(pygame.image.load('ficha6_2.png')), (pygame.image.load('ficha6_3.png'))], 
       [(pygame.image.load('ficha7_0_1.png')), (pygame.image.load('ficha7_1_1.png')),(pygame.image.load('ficha7_2_1.png')), (pygame.image.load('ficha7_3_1.png'))],
       [(pygame.image.load('ficha8.png')), (pygame.image.load('ficha8_1.png')),(pygame.image.load('ficha8.png')), (pygame.image.load('ficha8_1.png'))],
       [(pygame.image.load('ficha9.png')), (pygame.image.load('ficha9_1.png')),(pygame.image.load('ficha9_2.png')), (pygame.image.load('ficha9_3.png'))], 
       [(pygame.image.load('ficha10.png')), (pygame.image.load('ficha10_1.png')),(pygame.image.load('ficha10_2.png')), (pygame.image.load('ficha10_3.png'))],
       [(pygame.image.load('ficha11.png')), (pygame.image.load('ficha11_1.png')),(pygame.image.load('ficha11_2.png')), (pygame.image.load('ficha11_3.png'))],
       [(pygame.image.load('ficha12.png')), (pygame.image.load('ficha12_1.png')),(pygame.image.load('ficha12.png')), (pygame.image.load('ficha12_1.png'))]]


class pieces(object):
    
   # pzs1 = [pygame.image.load('ficha1.png') , pygame.image.load('ficha1_1.png')]
    
    def __init__(self, x, y, width, height, number):
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
            win.blit(pzs[self.number][self.subnumber], (self.x, self.y))

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
            elif self.number == 10:
                self.rect1 = [self.x , self.y, (self.width*2/3), self.height/2]
                self.rect2 = [self.x   , self.y +(self.height /2 ), (self.width), (self.height /2 )]
            elif self.number == 11:
                self.rect1 = [self.x , self.y, (self.width/3), (self.height/3)]
                self.rect2 = [self.x +(self.width/3)  , self.y , (self.width/3), (self.height)]
                self.rect3 = [self.x +((self.width/3)*2)  , self.y + ((self.width/3)*2) , (self.width/3), (self.height /3 )]


    def draw_rect_col(self, win):
        if self.number <= 3:
            pygame.draw.rect(win, (0,0,255), (self.x, self.y, self.width, self.height) ,2)
        else:
            if self.number == 4:
                if self.subnumber == 0:
                    self.rect1 = [self.x , self.y, (self.width/2), self.height]
                    self.rect2 = [self.x + (self.width/2) , self.y + (self.height/2), (self.width/2), (self.height /2 )]    
                elif self.subnumber == 1:
                    self.rect1 = [self.x , self.y, (self.width), self.height/2]
                    self.rect2 = [self.x , self.y + (self.height/2), (self.width/2), (self.height /2 )] 
                elif self.subnumber == 2:
                    self.rect1 = [self.x , self.y, (self.width), self.height/2]
                    self.rect2 = [self.x + (self.width/2) , self.y + (self.height/2), (self.width/2), (self.height /2 )]    
                elif self.subnumber == 3:
                    self.rect1 = [self.x + (self.width/2), self.y, (self.width/2), self.height/2 ]
                    self.rect2 = [self.x  , self.y + (self.height/2), (self.width), (self.height /2 )]
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255),(self.rect2) ,2)
            elif self.number == 5:
                if self.subnumber == 0:
                    self.rect1 = [self.x , self.y, (self.width/2), self.height]
                    self.rect2 = [self.x + (self.width/2) , self.y + (self.height/3), (self.width/2), (self.height /3 )]    
                elif self.subnumber == 1:
                    self.rect1 = [self.x , self.y, (self.width), self.height/2]
                    self.rect2 = [self.x + (self.width/3), self.y + (self.height/2), (self.width/3), (self.height /2 )] 
                elif self.subnumber == 2:
                    self.rect1 = [self.x , self.y + (self.height/3), (self.width/2), self.height/3]
                    self.rect2 = [self.x + (self.width/2) , self.y , (self.width/2), (self.height)]    
                elif self.subnumber == 3:
                    self.rect1 = [self.x + (self.width/3), self.y, (self.width/3), self.height/2 ]
                    self.rect2 = [self.x  , self.y + (self.height/2), (self.width), (self.height /2 )]
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255),(self.rect2) ,2)
            elif self.number == 6:
                if self.subnumber == 0:
                    self.rect1 = [self.x , self.y, (self.width), (self.height/2)]
                    self.rect2 = (self.x  , self.y + (self.height/2), (self.width/3), (self.height /2 ))
                elif self.subnumber == 1:
                    self.rect1 = [self.x , self.y, (self.width/2), (self.height/3)]
                    self.rect2 = (self.x +(self.width/2) , self.y , (self.width/2), (self.height ))
                elif self.subnumber == 2:
                    self.rect1 = [self.x + ((self.width/3)*2) , self.y, (self.width/3), (self.height/2)]
                    self.rect2 = (self.x  , self.y + (self.height/2), (self.width), (self.height/2 ))
                elif self.subnumber == 3:
                    self.rect1 = [self.x , self.y, (self.width/2), (self.height)]
                    self.rect2 = (self.x +(self.width/2) , self.y + (self.height*2/3), (self.width/2), (self.height /3 ))
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255), (self.rect2) ,2)
            elif self.number == 7:
                if self.subnumber == 0 or self.subnumber == 2 :
                    self.rect1 = [self.x , self.y, (self.width/2), (self.height/3)*2]
                    self.rect2 = (self.x + (self.width/2), self.y + (self.height/3),   (self.width/2), (self.height /3 )*2)
                elif self.subnumber == 1 or self.subnumber == 3:
                    self.rect1 = [self.x+(self.width/3) , self.y, (self.width*2/3), (self.height/2)]
                    self.rect2 = (self.x , self.y + (self.height/2),   (self.width*2/3), (self.height /2 ))
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255), (self.rect2) ,2)
            elif self.number == 8:
                if self.subnumber == 0:
                    self.rect1 = [self.x , self.y, (self.width/2), self.height]
                    self.rect2 = [self.x +(self.width/2)  , self.y , (self.width/2), (self.height /4 )]
                elif self.subnumber == 1:
                    self.rect1 = [self.x , self.y, (self.width), self.height/2]
                    self.rect2 = [self.x +((self.width/4)*3)  , self.y + (self.height /2 ) , (self.width/4), (self.height /2 )]
                elif self.subnumber == 2:
                    self.rect1 = [self.x , self.y + (self.height*3/4), (self.width/2), self.height/4]
                    self.rect2 = [self.x +(self.width/2)  , self.y  , (self.width/2), (self.height )]
                elif self.subnumber == 3:
                    self.rect1 = [self.x , self.y, (self.width/4), self.height/2]
                    self.rect2 = [self.x   , self.y + (self.height /2 ) , (self.width), (self.height /2 )]
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255), (self.rect2) ,2)
            elif self.number == 9:
                if self.subnumber == 0:
                    self.rect1 = [self.x , self.y, (self.width/2), self.height]
                    self.rect2 = [self.x +(self.width/2)  , self.y + (self.height /4 ), (self.width/2), (self.height /4 )]
                elif self.subnumber == 1:
                    self.rect1 = [self.x , self.y, (self.width), self.height/2]
                    self.rect2 = [self.x +((self.width/4)*2)  , self.y + (self.height /2 ) , (self.width/4), (self.height /2 )]
                elif self.subnumber == 2:
                    self.rect1 = [self.x , self.y + (self.height*2/4), (self.width/2), self.height/4]
                    self.rect2 = [self.x +(self.width/2)  , self.y  , (self.width/2), (self.height )]
                elif self.subnumber == 3:
                    self.rect1 = [self.x + (self.width/4), self.y, (self.width/4), self.height/2]
                    self.rect2 = [self.x   , self.y + (self.height /2 ) , (self.width), (self.height /2 )]
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255), (self.rect2) ,2)
            elif self.number == 10:
                if self.subnumber == 0:
                    self.rect1 = [self.x , self.y, (self.width*2/3), self.height/2]
                    self.rect2 = [self.x   , self.y +(self.height /2 ), (self.width), (self.height /2 )]
                elif self.subnumber == 1:
                    self.rect1 = [self.x , self.y, (self.width), self.height*2/3]
                    self.rect2 = [self.x   , self.y + (self.height *2/3 ) , (self.width/2), (self.height /3 )]
                elif self.subnumber == 2:
                    self.rect1 = [self.x , self.y, (self.width), self.height/2]
                    self.rect2 = [self.x +((self.width/3))  , self.y + (self.height /2 ) , (self.width*2/3), (self.height /2 )]
                elif self.subnumber == 3:
                    self.rect1 = [self.x +(self.width/2) , self.y, (self.width/2), self.height/3]
                    self.rect2 = [self.x   , self.y + (self.height /3 ) , (self.width), (self.height*2/3 )]
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255), (self.rect2) ,2)
            elif self.number == 11:
                if self.subnumber == 0 or  self.subnumber == 2:
                    self.rect1 = [self.x , self.y, (self.width/3), (self.height/3)]
                    self.rect2 = [self.x +(self.width/3)  , self.y , (self.width/3), (self.height)]
                    self.rect3 = [self.x +((self.width/3)*2)  , self.y + ((self.width/3)*2) , (self.width/3), (self.height /3 )]
                elif self.subnumber == 1 or  self.subnumber == 3:
                    self.rect1 = [self.x , self.y + (self.height/3), (self.width/3), (self.height*2/3)]
                    self.rect2 = [self.x +(self.width/3)  , self.y + (self.height/3), (self.width/3), (self.height/3)]
                    self.rect3 = [self.x +((self.width/3)*2)  , self.y , (self.width/3), (self.height*2/3 )]
        
                pygame.draw.rect(win, (0,0,255), (self.rect1) ,2)
                pygame.draw.rect(win, (0,0,255), (self.rect2) ,2)
                pygame.draw.rect(win, (0,0,255), (self.rect3) ,2)