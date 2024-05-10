import pygame 
from spaceship import SpaceShipImg
from projectil import Bullet
from aliens import AlienImg
from check_time import TimeTracker
from game_text import GameText

pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
spaceship = SpaceShipImg(lifes=2)
aliens = AlienImg()
time_tracker = TimeTracker()
game_text = GameText()


aliens.store_aliens()

bullet_hit_target = False
bullet_speed = 2

def shot_bullet(total_bullets_list, direction):
    global bullet_hit_target
    for bullet in total_bullets_list:
        if bullet_hit_target:
            total_bullets_list.pop(total_bullets_list.index(bullet))
            bullet_hit_target = False
        if bullet.bullet_y_pos > 0:
            bullet.bullet_y_pos += direction * bullet_speed
            bullet.create_bullet(screen)
        else:
            total_bullets_list.pop(total_bullets_list.index(bullet))


def spawn_alien_bullets():
    random_alien = aliens.choose_alien_shot()
    if random_alien is not None:
        if time_tracker.is_game_live():
            bullet = Bullet(bullet_x_pos=random_alien.alien_x_pos, bullet_y_pos=random_alien.alien_y_pos , number_of_bullets=1000, is_alien=True)
            bullet.add_bullet(aliens.total_aliens_bullets)
            bullet_was_shot = True
            if bullet_was_shot:
                time_tracker.threshold += time_tracker.random_shooting_timing
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



def show_total_lifes_message():
    pass

def level_up():
    """Resets variables and increases some variables to make game harder"""
    game_text.show_info_delay(screen=screen, x_pos=70, y_pos=200, font_size=40, message=f"LEVEL {game_text.level}! MORE SPEED!")
    time_tracker.reset_threshold()
    aliens.clear_aliens()
    aliens.clear_bullets()
    aliens.reset_aliens()
    increase_bullet_speed()
    spaceship.reset_spaceship_pos()
    game_text.increase_level()
    time_tracker.start_game()
    aliens.wiped = False

def increase_bullet_speed():
    global bullet_speed
    bullet_speed += 1
    

def restart_same_level():
    game_text.show_info_delay(screen=screen, x_pos=150, y_pos=200, font_size=25, message=f"You lost 1 life! Lifes left: {spaceship.lifes}")
    time_tracker.reset_threshold()
    aliens.clear_aliens()
    aliens.clear_bullets()
    aliens.store_aliens()
    aliens.create_aliens(screen=screen)
    aliens.move_aliens()
    spaceship.reset_spaceship_pos()
    time_tracker.start_game()
    aliens.wiped = False

def game_over():
    game_text.show_info_delay(screen=screen, x_pos=150, y_pos=200, font_size=40, message="GAME OVER")
    


time_tracker.start_game()   
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    screen.fill("purple")

    
    game_text.show_info_current(screen=screen, x_pos=10, y_pos=380, font_size=15, message=f"Lifes: {spaceship.lifes}")
    game_text.show_info_current(screen=screen, x_pos=10, y_pos=360, font_size=15, message=f"Level: {game_text.level}")
    
    spaceship.create_spaceship(spaceship=spaceship, screen=screen)
    spaceship.move_spaceship(key=key)
    
    aliens.create_aliens(screen=screen)
    aliens.move_aliens()
    

    shot_bullet(spaceship.total_spaceship_bullets, direction=-1)
    shot_bullet(aliens.total_aliens_bullets, direction=1)
    
    spawn_alien_bullets()
    spawn_spaceship_bullets()
    


    # Check Collisions
    if aliens.check_collision_bullets(total_spaceship_bullets=spaceship.total_spaceship_bullets):
        bullet_hit_target = True

    if spaceship.check_collision_bullet(total_aliens_bullets=aliens.total_aliens_bullets):
        bullet_hit_target = True
        if spaceship.lifes < 1:
            game_over()
        else:
            restart_same_level()



    
    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()


