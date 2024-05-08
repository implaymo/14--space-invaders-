import pygame 
from spaceship import SpaceShipImg
from projectil import Bullet
from aliens import AlienImg
from check_time import TimeTracker
from game_text import GameText
import time


pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
spaceship = SpaceShipImg(lifes=1)
aliens = AlienImg()
time_tracker = TimeTracker()
game_text = GameText()


aliens.store_aliens()

bullet_hit_target = False


def shot_bullet(element_from_list, direction):
    global bullet_hit_target
    for bullet in element_from_list:
        if bullet_hit_target:
            element_from_list.pop(element_from_list.index(bullet))
            bullet_hit_target = False
        if bullet.bullet_y_pos > 0:
            bullet.bullet_y_pos += direction * bullet.speed
            bullet.create_bullet(screen)
        else:
            element_from_list.pop(element_from_list.index(bullet))


def spawn_alien_bullets():
    random_alien = aliens.choose_alien_shot()
    if random_alien is not None:
        if time_tracker.is_game_live():
            bullet = Bullet(bullet_x_pos=random_alien.alien_x_pos, bullet_y_pos=random_alien.alien_y_pos , number_of_bullets=1000, is_alien=True)
            bullet.add_bullet(aliens.total_aliens_bullets)
            bullet_was_shot = True
            if bullet_was_shot:
                time_tracker.threshold += 2
                bullet_was_shot = False
    else:
        aliens.wiped = True
        level_up()
        
def spawn_spaceship_bullets():
    top_of_spaceship = spaceship.spaceship_y_pos - 10
    mid_of_spaceship = spaceship.spaceship_x_pos + 5
    if key[pygame.K_SPACE]:
        bullet = Bullet(bullet_x_pos=mid_of_spaceship, bullet_y_pos=top_of_spaceship, number_of_bullets=1, is_alien=False)
        bullet.add_bullet(spaceship.total_spaceship_bullets)

        
def level_up():
    aliens.number_rows += 1
    aliens.total_alien_per_row += 1
    aliens.store_aliens()
    game_text.level += 1
    time_tracker.start_game()
    time.sleep(1)
    aliens.wiped = False

time_tracker.start_game()   
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    screen.fill("purple")

    
    game_text.lifes_text(screen=screen, spaceship_lifes=spaceship.lifes, x_pos=10, y_pos=380)
    game_text.level_text(screen=screen, x_pos=10, y_pos=360)
    
    spaceship.create_spaceship(spaceship=spaceship, screen=screen)
    spaceship.move_spaceship(key=key)
    
    aliens.create_aliens(screen=screen)
    aliens.move_aliens()
    
    spawn_alien_bullets()
    spawn_spaceship_bullets()
    
    shot_bullet(spaceship.total_spaceship_bullets, direction=-1)
    shot_bullet(aliens.total_aliens_bullets, direction=1)
    

    # Check Collisions
    if aliens.check_collision_bullets(total_spaceship_bullets=spaceship.total_spaceship_bullets):
        bullet_hit_target = True

    if spaceship.check_collision_bullet(total_aliens_bullets=aliens.total_aliens_bullets):
        bullet_hit_target = True


    
    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()


