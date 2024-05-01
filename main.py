import pygame 
from spaceship import SpaceShipImg
from projectil import Bullet
from aliens import AlienImg

pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Space Invaders")



spaceship = SpaceShipImg()
aliens_ship = AlienImg()

aliens_ship.store_aliens()
all_bullets = []
bullet_speed_multiplier = 2



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    key = pygame.key.get_pressed()
    screen.fill("purple")

    spaceship.create_spaceship(spaceship=spaceship, screen=screen)
    spaceship.move_spaceship(key=key)

    
    aliens_ship.create_aliens(screen=screen)
    aliens_ship.move_aliens()
    

    for bullet in all_bullets:
        if bullet.bullet_y_pos > 0:
            bullet.bullet_y_pos += bullet.direction * bullet_speed_multiplier
            bullet.draw_bullet(screen)
        else:
            all_bullets.pop(all_bullets.index(bullet))

    if key[pygame.K_SPACE]:
        if len(all_bullets) < 1:
            all_bullets.append(Bullet(bullet_x_pos=spaceship.spaceship_x_pos + 20, bullet_y_pos=spaceship.spaceship_y_pos + 10))

    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()