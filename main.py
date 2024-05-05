import pygame 
from spaceship import SpaceShipImg
from projectil import Bullet
from aliens import AlienImg
from check_time import TimeTracker
import random

pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Space Invaders")



spaceship = SpaceShipImg(5)
aliens = AlienImg()
time_tracker = TimeTracker()


aliens.store_aliens()

total_spaceship_bullets = []
total_aliens_bullets = []
bullet_speed_multiplier = 2
bullet_was_shot = False
bullet_collide = False


def shot_bullet(game_elements_list, direction, is_alien=False):
    for bullet in game_elements_list:
        if bullet.bullet_y_pos > 0:
            bullet.bullet_y_pos += direction * bullet_speed_multiplier
            bullet.draw_bullet(screen)
        else:
            game_elements_list.pop(game_elements_list.index(bullet))
            
def store_bullet(game_elements_list, class_, number_of_bullets):
    if len(game_elements_list) < number_of_bullets:
            game_elements_list.append(class_)

def alien_shooting():
    total_bullets_aliens = 10
    last_row_aliens = aliens.all_aliens[aliens.number_rows - 1]
    random_alien = random.choice(last_row_aliens)

    if random_alien.alien_x_pos > 0 and time_tracker.is_game_live():
        bullet_for_aliens = Bullet(bullet_x_pos=random_alien.alien_x_pos + (aliens.width /2), bullet_y_pos=random_alien.alien_y_pos + aliens.height, is_alien=True)
        store_bullet(total_aliens_bullets, bullet_for_aliens, number_of_bullets=total_bullets_aliens)
        bullet_was_shot = True
        if bullet_was_shot:
            time_tracker.threshold = time_tracker.threshold + 5
            total_bullets_aliens = total_bullets_aliens + 5

def spaceship_shooting():
    total_bullets_spaceship = 1
    top_of_spaceship = 10
    mid_of_spaceship = 20
    if key[pygame.K_SPACE]:
        bullet_for_spaceship = Bullet(bullet_x_pos=spaceship.spaceship_x_pos + mid_of_spaceship, bullet_y_pos=spaceship.spaceship_y_pos + top_of_spaceship, is_alien=False)
        store_bullet(total_spaceship_bullets, bullet_for_spaceship, number_of_bullets=total_bullets_spaceship)


def check_collision_bullet_and_alien():
       for bullet in total_spaceship_bullets:
        for row in aliens.all_aliens:
            for alien in row:
                if bullet.bullet_rect.colliderect(alien.alien_rect):
                    row.pop(row.index(alien))

def check_collision_bullet_and_spaceship():
       for bullet in total_aliens_bullets:
            if bullet.bullet_rect.colliderect(spaceship.spaceship_rect):
                spaceship.got_hit = True
                spaceship.lose_life()



time_tracker.start_game()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    screen.fill("purple")

    spaceship.create_spaceship(spaceship=spaceship, screen=screen)
    spaceship.move_spaceship(key=key)
    
    aliens.create_aliens(screen=screen)
    aliens.move_aliens()
    
    spaceship_shooted = shot_bullet(total_spaceship_bullets, direction=-1, is_alien=False)
    aliens_shooted = shot_bullet(total_aliens_bullets, direction=1, is_alien=True)
    

    alien_shooting()
    spaceship_shooting()

    # Check Collision Bullet with Aliens
    check_collision_bullet_and_alien()
    check_collision_bullet_and_spaceship()


    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
