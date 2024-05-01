import pygame 
from spaceship import SpaceShipImg
from projectil import Bullet
from aliens import AlienImg
from check_time import TimeTracker

pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Space Invaders")



spaceship = SpaceShipImg()
aliens_ship = AlienImg()
time_tracker = TimeTracker()

aliens_ship.store_aliens()
spaceship_bullets = []
aliens_bullets = []
bullet_speed_multiplier = 2

def shot_bullet(list):
    for bullet in list:
        if bullet.bullet_y_pos > 0:
            bullet.bullet_y_pos += bullet.direction * bullet_speed_multiplier
            bullet.draw_bullet(screen)
        else:
            list.pop(list.index(bullet))
def store_bullet(list, class_):
    if len(list) < 1:
            list.append(class_)

time_tracker.start_game()


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
    

    shot_bullet(spaceship_bullets)
    shot_bullet(aliens_bullets)

    if time_tracker.is_game_live(threshold=10):
        store_bullet(aliens_bullets, Bullet(bullet_x_pos=aliens_ship.alien_x_pos, bullet_y_pos=aliens_ship.alien_x_pos))
        

    if key[pygame.K_SPACE]:
        store_bullet(spaceship_bullets, Bullet(bullet_x_pos=spaceship.spaceship_x_pos + 20, bullet_y_pos=spaceship.spaceship_y_pos + 10))

    
    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()