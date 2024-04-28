import pygame
import os

class AlienImg():
    def __init__(self) -> None:
        self.image_path = os.path.join("images", "alien.png")
        self.alien_img = pygame.image.load(self.image_path).convert_alpha()
        self.alien_resized = pygame.transform.scale(self.alien_img, (60, 70))

        self.alien_x_pos = 100
        self.alien_y_pos = 100