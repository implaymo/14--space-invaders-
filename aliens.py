import pygame
import os

class AlienImg():
    def __init__(self, x_pos, y_pos) -> None:
        self.image_path = os.path.join("images", "alien.png")
        self.alien_img = pygame.image.load(self.image_path).convert_alpha()
        self.alien_resized = pygame.transform.scale(self.alien_img, (20, 20))

        self.alien_x_pos = x_pos
        self.alien_y_pos = y_pos
        
