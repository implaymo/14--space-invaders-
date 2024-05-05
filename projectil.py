import pygame
import os

class Bullet():
    def __init__(self,  bullet_x_pos, bullet_y_pos, is_alien=False) -> None:
        self.direction = -1
        self.bullet_x_pos = bullet_x_pos
        self.bullet_y_pos = bullet_y_pos
        self.radius = 3
        self.color = "black"
        self.vel = self.direction
        self.width = 30
        self.height = 30
        self.image_path = os.path.join("images", "bullet.png")
        self.bullet_img = pygame.image.load(self.image_path).convert_alpha()
        self.bullet_resized = pygame.transform.scale(self.bullet_img, (self.width, self.height))
        self.bullet_rect = self.bullet_resized.get_rect()
        
        if is_alien: 
            self.bullet_resized = pygame.transform.rotate(self.bullet_resized, 180)

    def draw_bullet(self, screen):
        screen.blit(self.bullet_resized, (self.bullet_x_pos - 15, self.bullet_y_pos - 20))
        self.bullet_rect.topleft = (self.bullet_x_pos, self.bullet_y_pos)







    