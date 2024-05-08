import pygame
import os

class Bullet():
    def __init__(self,  bullet_x_pos, bullet_y_pos, number_of_bullets, is_alien=False) -> None:
        self.bullet_collide = False
        self.direction = -1
        self.bullet_x_pos = bullet_x_pos
        self.bullet_y_pos = bullet_y_pos
        self.number_of_bullets = number_of_bullets
        self.width = 30
        self.height = 30
        self.image_path = os.path.join("images", "bullet.png")
        self.bullet_img = pygame.image.load(self.image_path).convert_alpha()
        self.bullet_resized = pygame.transform.scale(self.bullet_img, (self.width, self.height))
        self.bullet_rect = self.bullet_resized.get_rect()
        self.bullet_rect.inflate_ip(-15, -10)
        
        
        if is_alien: 
            self.bullet_resized = pygame.transform.rotate(self.bullet_resized, 180)

    def create_bullet(self, screen):
        screen.blit(self.bullet_resized, (self.bullet_x_pos, self.bullet_y_pos))
        self.bullet_rect.topleft = (self.bullet_x_pos, self.bullet_y_pos + 15)
        

    def add_bullet(self, game_elements_list):
        if len(game_elements_list) < self.number_of_bullets:
            game_elements_list.append(self)
            
            
    




    