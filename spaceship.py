import pygame
import os

class SpaceShipImg():
    def __init__(self) -> None:
        self.image_path = os.path.join("images", "spaceship.png")
        self.spaceship_img = pygame.image.load(self.image_path).convert_alpha()
        self.spaceship_resized = pygame.transform.scale(self.spaceship_img, (50, 90))
    
        self.spaceship_x_pos = 270
        self.spaceship_y_pos = 300


