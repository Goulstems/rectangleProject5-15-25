from Mob import Mob

class Enemy(Mob):
    def __init__(self,pos,size,speed,screen):
        super().__init__(
            pos,
            size,
            [255,0,0],
            speed,
            screen
        )
    
    #consider AI behavior