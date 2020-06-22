import pygame

py2 = pygame.image.load('p2.png')

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