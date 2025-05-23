from Mob import Mob

class Player(Mob):
    def __init__(self,pos,size,screen):
        super().__init__(
            pos,
            size,
            [0,0,255],
            1,
            screen
        )
    
    #consider arrow key / WASD methods?