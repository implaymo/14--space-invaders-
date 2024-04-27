import pygame 
from spaceship import SpaceShipImg

pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Space Invaders")
spaceship = SpaceShipImg()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("purple")

    screen.blit(spaceship.spaceship_resized, (spaceship.spaceship_x_pos, spaceship.spaceship_y_pos))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()