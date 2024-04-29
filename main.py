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

all_aliens = []
number_rows = 5
total_alien_per_row = 3
alien_start_y_pos = 50
y_gap_between_aliens = 20
x_gap_between_aliens = 30


def store_aliens():
    for row in range(number_rows):
        if row < number_rows:
            all_aliens.append([]) 
        for i in range(total_alien_per_row):
            x_pos = i * x_gap_between_aliens
            y_next_row_pos = (row * y_gap_between_aliens)
            y_pos = alien_start_y_pos + y_next_row_pos
            new_alien = AlienImg(x_pos=x_pos, y_pos=y_pos)
            all_aliens[row].append(new_alien)
            
def create_aliens():
     for row in range(len(all_aliens)):
        for alien in all_aliens[row]:
            screen.blit(alien.alien_resized, (alien.alien_x_pos, alien.alien_y_pos))



store_aliens()
all_bullets = []
bullet_speed_multiplier = 10



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    key = pygame.key.get_pressed()
    screen.fill("purple")

    spaceship.create_spaceship(spaceship=spaceship, screen=screen)
    spaceship.move_spaceship(key=key)

    create_aliens()
    

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