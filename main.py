import pygame
from Rectangle import Rectangle
from Mob import Mob
#===========================================================

# [Initialize Pygame]
pygame.init() 
screen = pygame.display.set_mode((400, 300))
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

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))

    # [Initialize players]
    # player1 = Rectangle(
    #     [100, 50],  #size
    #     [playerPos["x"], playerPos["y"]],   #pos
    #     (0,0,255),  #color
    #     0,          #lineThickness
    #     screen
    # )
    # enemy = Rectangle(
    #     [100, 50],  #size
    #     [enemyPos["x"], enemyPos["y"]],   #pos
    #     (255,0,0),  #color
    #     0,          #lineThickness
    #     screen
    # )


    # enemyPos["x"]-=.1

    player1 = Mob([50,50],(255,0,0),screen)
    enemy = Mob([250,50],(0,0,255),screen)
    enemy.Move(1,0)
    collisionDetect()       #detect collissions / damaging TODO: Debounce
    pygame.display.flip()   #render
    clock.tick(60)          # Limit to 60 FPS

# Quit Pygame 
pygame.quit()