import pygame

CodPlantilla = [[(8, 6, 4), (11, 0, 7), (0, 8, 6), (3, 0, 10), (0, 10, 6), (6, 7, 3)],
                [(5, 10, 4), (4, 6, 8), (0, 10, 6), (4, 9, 6), (6, 4, 10), (6, 7, 3)],
                [(0, 6, 10), (9, 7, 0), (8, 4, 5), (4, 10, 6), (3, 11, 0), (1, 9, 10)],
                [(8, 0, 10), (6, 9, 5), (2, 6, 10), (7, 10, 2), (8, 5, 6), (6, 8, 7)],
                [(1, 6, 10), (4, 7, 5), (11, 0, 4), (1, 11, 6), (2, 1, 8), (0, 8, 4)],
                [(6, 5, 7), (0, 7, 10), (8, 10, 1), (6, 4, 10), (0, 9, 7), (8, 0, 6)]]
CodPlantillaColission = [[True, True, True, False, True, True, True, True, True, True, True, True, True, False, False, False],
                         [False, True, True, True, False, True, True, True, True, True, True, True, False, False, True, True],
                         [True, True, False, False, True, True, True, False, True, True, True, False, True, True, True, True],
                         [True, True, False ,False, True , True ,True, True, True, True, True, False, True, True, True, True],
                         [False, True, True, False, False, True, True, False, False, True, True, True, True, True, True, True],
                         [True, True, True, False, True, True, True, True, True, True, True, True, False, True, False, False]]

class template(object):
   
    pnt = [pygame.image.load('plantilla1.png'), pygame.image.load('plantilla2.png'), pygame.image.load('plantilla3.png'), pygame.image.load('plantilla4.png'), pygame.image.load('plantilla5.png'), pygame.image.load('plantilla6.png') ]
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = 4
        self.CodPieces = CodPlantilla[self.number]
        self.CodColission = CodPlantillaColission[self.number].copy()
        self.completed = False
        self.solv_aux = self.CodColission.copy()
        self.solv_aux2 = self.CodColission.copy()
        self.solv_aux3 = CodPlantillaColission[self.number] 
       
    def draw(self, win):
        win.blit(self.pnt[self.number], (self.x, self.y),)
    def Is_solved (self):
        
        cont_solv = 0
        for i in self.solv_aux:
            if i == False:
                cont_solv += 1
            if cont_solv >= 16:
                return True
        self.solv_aux = self.CodColission.copy()
        return False
