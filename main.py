import pygame 
from spaceship import SpaceShipImg
from projectil import Bullet
from aliens import AlienImg
from check_time import TimeTracker
from game_text import Lifes


pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Space Invaders")

spaceship = SpaceShipImg(lifes=3)
aliens = AlienImg()
time_tracker = TimeTracker()
lifes = Lifes()


aliens.store_aliens()

total_spaceship_bullets = []
total_aliens_bullets = []
bullet_speed_multiplier = 2
bullet_was_shot = False
bullet_hit_target = False


def shot_bullet(game_elements_list, direction):
    global bullet_hit_target
    for bullet in game_elements_list:
        if bullet_hit_target:
            game_elements_list.pop(game_elements_list.index(bullet))
            bullet_hit_target = False
        if bullet.bullet_y_pos > 0:
            bullet.bullet_y_pos += direction * bullet_speed_multiplier
            bullet.move_bullet(screen)
        else:
            game_elements_list.pop(game_elements_list.index(bullet))
                       
def store_bullet(game_elements_list, class_, number_of_bullets):
    if len(game_elements_list) < number_of_bullets:
            game_elements_list.append(class_)

def spawn_alien_bullets():
    total_bullets = 10
    random_alien = aliens.choose_alien_shot()
    mid_of_alien = random_alien.alien_x_pos + (aliens.width /2)
    bottom_of_alien = random_alien.alien_y_pos + aliens.height
    if random_alien.alien_x_pos > 0 and time_tracker.is_game_live():
        bullet = Bullet(bullet_x_pos=mid_of_alien, bullet_y_pos=bottom_of_alien, is_alien=True)
        store_bullet(total_aliens_bullets, bullet, number_of_bullets=total_bullets)
        bullet_was_shot = True
        if bullet_was_shot:
            time_tracker.threshold = time_tracker.threshold + 5
            total_bullets = total_bullets + 5

def spawn_spaceship_bullets():
    total_bullets = 1
    top_of_spaceship = spaceship.spaceship_y_pos - 10
    mid_of_spaceship = spaceship.spaceship_x_pos + 5
    if key[pygame.K_SPACE]:
        bullet = Bullet(bullet_x_pos=mid_of_spaceship, bullet_y_pos=top_of_spaceship, is_alien=False)
        store_bullet(total_spaceship_bullets, bullet, number_of_bullets=total_bullets)
        
def level_up():
    pass

def game_over():
    pass

time_tracker.start_game()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    screen.fill("purple")

    lifes.display_text(screen=screen, spaceship_lifes=spaceship.lifes)
    
    spaceship.create_spaceship(spaceship=spaceship, screen=screen)
    spaceship.move_spaceship(key=key)
    
    aliens.create_aliens(screen=screen)
    aliens.move_aliens()
    
    spaceship_shooted = shot_bullet(total_spaceship_bullets, direction=-1)
    aliens_shooted = shot_bullet(total_aliens_bullets, direction=1)
    

    spawn_alien_bullets()
    spawn_spaceship_bullets()

    # Check Collision Bullet with Aliens
    if aliens.check_collision_bullets(total_spaceship_bullets=total_spaceship_bullets):
        bullet_hit_target = True
    if spaceship.check_collision_bullet(total_aliens_bullets=total_aliens_bullets):
        bullet_hit_target = True

    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
