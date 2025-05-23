import pygame
from Rectangle import Rectangle

class Mob(Rectangle):
    def __init__(self,pos,size,color,speed,screen):
        super().__init__(
            size, #size
            pos,
            color,
            0,
            screen
        )
        self.speed = speed
    
    def Move(self,dx,dy):
        before = self.pos[0]
        self.pos[0]+=dx*self.speed
        self.pos[1]+=dy*self.speed
        # print("bx: "+str(before)+" | ax: "+str(self.pos[0]))
        self.obj = pygame.draw.rect(self.window, self.color, [self.pos[0], self.pos[1], self.size[0], self.size[1]])
        # consider collisionDetect()