from Mob import Mob

class Player(Mob):
    def __init__(self,screen):
        super().__init__(
            [50,50],
            [0,0,255],
            screen
        )
    
    #consider arrow key / WASD methods?