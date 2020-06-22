import pygame

CodPlantilla = [[(8, 6, 4), (11, 0, 7), (0, 8, 6), (3, 0, 10), (0, 10, 6), (6, 7, 3)],
                [(5, 10, 4), (4, 6, 8), (0, 10, 6), (4, 9, 6), (6, 4, 10), (6, 7, 3)],
                [(0, 6, 10), (9, 7, 0), (8, 4, 5), (4, 10, 6), (3, 11, 0), (1, 9, 10)]]
CodPlantillaColission = [[True, True, True, False, True, True, True, True, True, True, True, True, True, False, False, False],
                         [False, True, True, True, False, True, True, True, True, True, True, True, False, False, True, True],
                         [True, True, False, False, True, True, True, False, True, True, True, False, True, True, True, True]]

class template(object):
   
    pnt = [pygame.image.load('plantilla1.png'), pygame.image.load('plantilla2.png'), pygame.image.load('plantilla3.png') ]
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = 2
        self.CodPieces = CodPlantilla[self.number] 
        self.CodColission = CodPlantillaColission[self.number]
        self.completed = False
        self.solv_aux = CodPlantillaColission[self.number]
        self.solv_aux2 = CodPlantillaColission[self.number]
       
    def draw(self, win):
        win.blit(self.pnt[self.number], (self.x, self.y))
    def Is_solved (self):
        cont_solv = 0
        
        
        for i in self.solv_aux:
            if i == False:
                cont_solv += 1
            if cont_solv >= 16:
                return True
        auxi = [[True, True, True, False, True, True, True, True, True, True, True, True, True, False, False, False],
                [False, True, True, True, False, True, True, True, True, True, True, True, False, False, True, True],
                [True, True, False, False, True, True, True, False, True, True, True, False, True, True, True, True]]
        self.solv_aux = auxi[self.number]
        return False
