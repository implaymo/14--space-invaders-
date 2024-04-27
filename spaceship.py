import pygame
from projectil import Bullet
import os

class SpaceShipImg():
    def __init__(self) -> None:
        self.image_path = os.path.join("images", "spaceship.png")
        self.spaceship_img = pygame.image.load(self.image_path).convert_alpha()
        self.spaceship_resized = pygame.transform.scale(self.spaceship_img, (40, 70))
    
        self.spaceship_x_pos = 270
        self.spaceship_y_pos = 320



    def move_spaceship(self, screen):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
           self.spaceship_x_pos -= 5
        if key[pygame.K_RIGHT]:
           self.spaceship_x_pos += 5
        if key[pygame.K_SPACE]:
            bullet = Bullet(screen=screen, bullet_x_pos=self.spaceship_x_pos + 20, bullet_y_pos=self.spaceship_y_pos + 20)
            return bullet




