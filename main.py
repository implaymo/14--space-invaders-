import pygame 
from spaceship import SpaceShipImg
from projectil import Bullet

pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Space Invaders")
spaceship = SpaceShipImg()
bullet = Bullet(bullet_x_pos=spaceship.spaceship_x_pos + 20, bullet_y_pos= spaceship.spaceship_y_pos + 20)


all_bullets = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(all_bullets)
            running = False
    
    key = pygame.key.get_pressed()
    screen.fill("purple")

    screen.blit(spaceship.spaceship_resized, (spaceship.spaceship_x_pos, spaceship.spaceship_y_pos))
    spaceship.move_spaceship(key=key)

    if key[pygame.K_SPACE]:
        bullet.draw_bullet(screen=screen)
        bullet.update_bullet()
        
    if key[pygame.K_UP]:
        all_bullets.clear()
    
    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()