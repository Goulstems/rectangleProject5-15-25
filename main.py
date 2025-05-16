import pygame
from Rectangle import Rectangle

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
def collisionDetect():
    if player1.obj.colliderect(enemy.obj):
        print("the player has been damaged!")

#===========================================================

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))

    # [Initialize players]
    player1 = Rectangle(
        [100, 50],  #size
        [playerPos["x"], playerPos["y"]],   #pos
        (0,0,255),  #color
        0,          #lineThickness
        screen
    )
    enemy = Rectangle(
        [100, 50],  #size
        [enemyPos["x"], enemyPos["y"]],   #pos
        (255,0,0),  #color
        0,          #lineThickness
        screen
    )
    enemyPos["x"]-=.1
    collisionDetect()       #detect collissions / damaging TODO: Debounce
    pygame.display.flip()   #render
    clock.tick(60)          # Limit to 60 FPS

# Quit Pygame 
pygame.quit()