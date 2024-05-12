import pygame 
from spaceship import SpaceShipImg
from projectil import Bullet
from aliens import AlienImg
from check_time import TimeTracker
from game_text import GameText
from buttons import Button
from start_menu import StartMenu
from level import Level
from game_over_menu import GameOverMenu
import sys
import random
from sound import GameSounds

def move_bullet(total_bullets_list, direction):
    global bullet_hit_target
    for bullet in total_bullets_list:
        if bullet_hit_target:
            total_bullets_list.pop(total_bullets_list.index(bullet))
            bullet_hit_target = False
        if bullet.bullet_y_pos > 0 and bullet.bullet_y_pos < 400:
            bullet.bullet_y_pos += direction * bullet_speed
            bullet.create_bullet(screen)
        else:
            try:
                total_bullets_list.pop(total_bullets_list.index(bullet))
            except ValueError:
                print("Bullet missing")
            else:
                continue


def spawn_alien_bullets():
    """Choses a random alien to shot/Checks if aliens got wiped"""
    random_alien = aliens.choose_alien_shot()
    if random_alien is not None:
        if time_tracker.is_game_live():
            bullet = Bullet(bullet_x_pos=random_alien.alien_x_pos, bullet_y_pos=random_alien.alien_y_pos , number_of_bullets=5, is_alien=True)
            bullet.add_bullet(aliens.total_aliens_bullets)
            alien_gun = GameSounds("./sounds/aliens_shoting_sound.wav")
            alien_gun.game_sound.play()
            time_tracker.threshold += random.uniform(0.2, 3.0)

    else:
        aliens.wiped = True
        if aliens.wiped:
            level_up()

def spawn_spaceship_bullets():
    top_of_spaceship = spaceship.spaceship_y_pos - 10
    mid_of_spaceship = spaceship.spaceship_x_pos + 5
    if key[pygame.K_SPACE]:
        bullet = Bullet(bullet_x_pos=mid_of_spaceship, bullet_y_pos=top_of_spaceship, number_of_bullets=1, is_alien=False)
        bullet.add_bullet(spaceship.total_spaceship_bullets)
        spaceship_gun = GameSounds("./sounds/spaceship_shoting_sound.wav")
        spaceship_gun.game_sound.play()


        


def increase_bullet_speed():
    global bullet_speed
    bullet_speed += 1

def level_up():
    """Resets variables and increases some variables to make game harder"""
    game_text.delay_message(screen=screen, x_pos=190, y_pos=180,font_size=40, message=f"LEVEL UP {level.level + 1}!")
    aliens.next_level_aliens()
    increase_bullet_speed()
    spaceship.reset_spaceship()
    time_tracker.start_game()
    time_tracker.reset_threshold()
    level.increase_level()
    aliens.wiped = False


def restart_same_level():
    """Resets variables and keeps the game at the same level the user was playing"""
    game_text.delay_message(screen=screen, x_pos=220, y_pos=60, font_size=25, message=f"Lifes left: {spaceship.lifes}")
    aliens.restart_level_aliens()
    spaceship.reset_spaceship()
    time_tracker.start_game()
    time_tracker.reset_threshold()
    aliens.wiped = False
    
def reset_game():
    """Reset all game variables"""
    global game_state, bullet_speed
    game_text.delay_message(screen=screen, x_pos=30, y_pos=70, font_size=30, background_color=None, message=f"Level: {level.level}")
    bullet_speed = 2
    level.level = 1
    spaceship.lifes = 1
    aliens.reset_game_aliens(screen=screen)
    spaceship.reset_spaceship()
    time_tracker.start_game()
    time_tracker.reset_threshold()
    aliens.wiped = False
    game_state = "game"

def game_over():
    """End Game Message"""
    game_text.delay_message(screen=screen, x_pos=180, y_pos=100, font_size=40, message="GAME OVER")
    GameOverMenu(screen=screen, restart_button=restart_button.create_button(screen=screen,font_size=25, text_color="green", bg_color="blue", text="Try Again"), 
                                      quit_button=quit_button.create_button(screen=screen, font_size=25, text_color="black", bg_color="red", text="Quit Game"))
    

  
# GAME SETUP   
pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
background_image = pygame.image.load('images/space_background.jpg')
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")

spaceship = SpaceShipImg(lifes=3)
aliens = AlienImg()
time_tracker = TimeTracker()
game_text = GameText()
level = Level()

start_button = Button(width=150, height=70, x_pos=225, y_pos=150)
quit_button = Button(width=100, height=30, x_pos=250, y_pos=170)
restart_button =  Button(width=100, height=30, x_pos=250, y_pos=220)

aliens.store_aliens()
bullet_hit_target = False
bullet_speed = 2
time_tracker.start_game()
game_state = "start_menu"
spaceship_gun = GameSounds("./sounds/game_music.mp3")
spaceship_gun.game_sound.play(loops=-1)   


# GAME MAINLOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if game_state == "start_menu" or game_state == "game_over":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if game_state == "start_menu":
                    if start_button.button_rect.collidepoint(event.pos):
                        game_state = "game"
                elif game_state == "game_over":
                    if restart_button.button_rect.collidepoint(event.pos):
                        reset_game()
                    elif quit_button.button_rect.collidepoint(event.pos):
                        sys.exit()
                
    if game_state == "start_menu":
        StartMenu(screen=screen, start_button=start_button.image_button(screen, path="start_button.png"))
        
    elif game_state == "game":  
        key = pygame.key.get_pressed()
        screen.fill((0, 0, 0))                       
        screen.blit(background_image, (0,0))
        
        game_text.show_game_info(screen=screen, x_pos=10, y_pos=380, font_size=15, message=f"Lifes: {spaceship.lifes}")
        game_text.show_game_info(screen=screen, x_pos=10, y_pos=360, font_size=15, message=f"Level: {level.level}")
        
        spaceship.create_spaceship(spaceship=spaceship, screen=screen)
        spaceship.move_spaceship(key=key)
        
        aliens.create_aliens(screen=screen)
        aliens.move_aliens()
        
        move_bullet(spaceship.total_spaceship_bullets, direction=-1)
        move_bullet(aliens.total_aliens_bullets, direction=1)
        
        spawn_alien_bullets()
        spawn_spaceship_bullets()
        
        # Check Collisions
        if aliens.check_collision_bullets(total_spaceship_bullets=spaceship.total_spaceship_bullets):
            bullet_hit_target = True

        if spaceship.check_collision_bullet(total_aliens_bullets=aliens.total_aliens_bullets):
            bullet_hit_target = True
            if spaceship.lifes < 1:
                game_state = "game_over"
            else:
                restart_same_level()

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
    
    elif game_state == "game_over":
        game_over()

pygame.quit()
