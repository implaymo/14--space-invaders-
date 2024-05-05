import pygame
import os

class AlienImg():
    def __init__(self) -> None:
        
        self.height = 20
        self.width = 20
        self.image_path = os.path.join("images", "alien.png")
        self.alien_img = pygame.image.load(self.image_path).convert_alpha()
        self.alien_resized = pygame.transform.scale(self.alien_img, (self.width, self.height))
        self.alien_rect = self.alien_resized.get_rect()

        self.alien_x_pos = 20
        self.alien_y_pos = 20
        self.all_aliens = []
        self.number_rows = 3
        self.total_alien_per_row = 5
        self.col_gap_between_aliens = 25
        self.row_gap_between_aliens = 20
        self.speed = 1
        self.hit_wall = False
        
    def store_aliens(self):
        for row in range(self.number_rows):
            self.all_aliens.append([]) 
            for i in range(self.total_alien_per_row):
                new_alien = AlienImg()
                next_col_pos = i * self.col_gap_between_aliens
                new_alien.alien_x_pos = self.alien_x_pos + next_col_pos

                next_row_pos = row * self.row_gap_between_aliens
                new_alien.alien_y_pos = self.alien_y_pos + next_row_pos

                new_alien.alien_rect = new_alien.alien_resized.get_rect(topleft=(new_alien.alien_x_pos, new_alien.alien_y_pos))
                self.all_aliens[row].append(new_alien)
        
    def create_aliens(self, screen):
        for row in range(len(self.all_aliens)):
            for alien in self.all_aliens[row]:
                screen.blit(alien.alien_resized, (alien.alien_x_pos, alien.alien_y_pos))

                
    def move_aliens(self):
        for row in self.all_aliens:
            for alien in row:
                alien.alien_x_pos += self.speed
                for new_row in self.all_aliens:
                    for new_alien in row:
                        new_alien.alien_rect.topleft = (alien.alien_x_pos, alien.alien_y_pos)
                if alien.alien_x_pos >= 580 or alien.alien_x_pos <= 0:
                    self.hit_wall = True
        if self.hit_wall:           
            self.speed *= -1
            self.hit_wall = False
    