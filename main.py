import pygame
from Rectangle import Rectangle
from Mob import Mob
from Player import Player
from Enemy import Enemy
#===========================================================

# [Initialize Pygame]
pygame.init() 
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello Pygame")
clock = pygame.time.Clock() #consider using another clockbase for exploint preventation
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
player1 = Player([50,50],[50,50],screen)
enemy = Enemy([250,50],[100,50],.25,screen)

#__________________________________________
#TASK1: SPAWN 4 ENEMIES 
    #   > PACK AN `enemies` List!

    # IN THE GAME LOOP, MOVE THEM ALL!

#TASK2: ADD SIZE SUPPORT FOR THE `Enemy` CLASS!
    #   > SPAWN ENEMIES OF VARIOUS SIZES!

#TASK3: ADD SPEED SUPPORT FOR THE `Enemy`/`Mob`/`Player` CLASS!
    #   > MOVE MOBS BASED ON THEIR `speed` properties!

#__________________________________________

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # - - - - - - - -  -
    screen.fill((0,0,0))
    player1.Move(0,0) #TODO: render handler
    enemy.Move(-1,0)
    collisionDetect()       #detect collissions / damaging TODO: Debounce
    #- - - - - - - - - -
    pygame.display.flip()   #render
    clock.tick(60)          # Limit to 60 FPS

# Quit Pygame 
pygame.quit()