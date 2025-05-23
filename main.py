import pygame
from Rectangle import Rectangle
from Mob import Mob
from Player import Player
#===========================================================

# [Initialize Pygame]
pygame.init() 
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello Pygame")
clock = pygame.time.Clock()
running = True

playerPos = {"x":50,"y":50}
enemyPos = {"x":250,"y":50}

#future TODO: Have Rectangle objects initialized outside of the loop
        #Have a "Mob" class which inherits Rectangle, but adds more methods such as Mob.Move()

#===========================================================

# [collission callback]
lastHit = pygame.time.get_ticks()
def collisionDetect():
    global lastHit
    currentHit = pygame.time.get_ticks()
    if currentHit - lastHit < 1000:
        return
    if player1.obj.colliderect(enemy.obj):
        print("the player has been damaged!")
        lastHit=currentHit
#===========================================================

    # [Initialize players]
player1 = Player(screen)
enemy = Mob([250,50],(255,0,0),screen)

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # - - - - - - - -  -
    screen.fill((0,0,0))
    player1.Move(0,0)
    enemy.Move(-1,0)
    collisionDetect()       #detect collissions / damaging TODO: Debounce
    #- - - - - - - - - -
    pygame.display.flip()   #render
    clock.tick(60)          # Limit to 60 FPS

# Quit Pygame 
pygame.quit()