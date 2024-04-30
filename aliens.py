import pygame
import os

class AlienImg():
    def __init__(self) -> None:
        self.image_path = os.path.join("images", "alien.png")
        self.alien_img = pygame.image.load(self.image_path).convert_alpha()
        self.alien_resized = pygame.transform.scale(self.alien_img, (20, 20))

        self.alien_x_pos = None
        self.alien_y_pos = 50
        self.all_aliens = []
        self.number_rows = 5
        self.total_alien_per_row = 3
        self.row_gap_between_aliens =20
        self.next_alien_x_pos = 30
        
    def store_aliens(self):
        for row in range(self.number_rows):
            self.all_aliens.append([]) 
            for i in range(self.total_alien_per_row):
                new_alien = AlienImg()
                next_row_pos = (row * self.row_gap_between_aliens)
                new_alien.alien_x_pos = i * self.next_alien_x_pos
                new_alien.alien_y_pos = self.alien_y_pos + next_row_pos
                self.all_aliens[row].append(new_alien)
        
    def create_aliens(self,screen):
        for row in range(len(self.all_aliens)):
            for alien in self.all_aliens[row]:
                screen.blit(alien.alien_resized, (alien.alien_x_pos, alien.alien_y_pos))
                
    def move_aliens(self):
        speed = 1
        for row in self.all_aliens:
            rightmost_alien = row[-1]
            leftmost_alien = row[0]
            for alien in row:
                alien.alien_x_pos += speed
                if rightmost_alien.alien_x_pos > 580 or leftmost_alien.alien_x_pos < 0:
                    speed *= -1