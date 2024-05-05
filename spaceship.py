import pygame
import os

class SpaceShipImg():
    def __init__(self, lifes) -> None:
        self.image_path = os.path.join("images", "spaceship.png")
        self.spaceship_img = pygame.image.load(self.image_path).convert_alpha()
        self.spaceship_resized = pygame.transform.scale(self.spaceship_img, (40, 70))
        self.spaceship_rect = self.spaceship_resized.get_rect()
    
        self.spaceship_x_pos = 270
        self.spaceship_y_pos = 320

        self.lifes = lifes
        self.got_hit = False




    def move_spaceship(self, key):
        if key[pygame.K_LEFT]:
            self.spaceship_x_pos -= 5
            if self.spaceship_x_pos < 0:
                self.spaceship_x_pos = 0
        if key[pygame.K_RIGHT]:
            self.spaceship_x_pos += 5
            if self.spaceship_x_pos > 560:
                self.spaceship_x_pos = 560
        self.spaceship_rect.topleft = (self.spaceship_x_pos, self.spaceship_y_pos)
        
                
    def create_spaceship(self, screen, spaceship):
        screen.blit(spaceship.spaceship_resized, (spaceship.spaceship_x_pos, spaceship.spaceship_y_pos))
    

    def lose_life(self):
        if self.got_hit:
            self.lifes = self.lifes - 1
            self.got_hit = False


    def check_collision_bullet(self, total_aliens_bullets):
        for bullet in total_aliens_bullets:
            if bullet.bullet_rect.colliderect(self.spaceship_rect):
                self.got_hit = True
                self.lose_life()
                print("SPACESHIP GOT SHOT")