import pygame
import os
import random 

class AlienImg():
    def __init__(self) -> None:
        
        self.height = 20
        self.width = 20
        self.image_path = os.path.join("images", "alien.png")
        self.alien_img = pygame.image.load(self.image_path).convert_alpha()
        self.alien_resized = pygame.transform.scale(self.alien_img, (self.width, self.height))

        self.alien_x_pos = 20
        self.alien_y_pos = 20
        self.all_aliens = []
        self.total_aliens_bullets = []
        self.number_rows = 1
        self.total_alien_per_row = 1
        self.col_gap_between_aliens = 25
        self.row_gap_between_aliens = 20
        self.speed = 1
        self.hit_wall = False
        self.wiped = False
        
    def store_aliens(self):
        for row in range(self.number_rows):
            self.all_aliens.append([]) 
            for i in range(self.total_alien_per_row):
                new_alien = AlienImg()
                col_pos = i * self.col_gap_between_aliens
                new_alien.alien_x_pos = self.alien_x_pos + col_pos

                row_pos = row * self.row_gap_between_aliens
                new_alien.alien_y_pos = self.alien_y_pos + row_pos

                new_alien.alien_rect = new_alien.alien_resized.get_rect(topleft=(new_alien.alien_x_pos, new_alien.alien_y_pos))
                new_alien.alien_rect.inflate_ip(-10, -5)
                self.all_aliens[row].append(new_alien)
        
    def create_aliens(self, screen):
        for row in range(len(self.all_aliens)):
            for alien in self.all_aliens[row]:
                screen.blit(alien.alien_resized, (alien.alien_x_pos, alien.alien_y_pos))

                
    def move_aliens(self):
        for row in self.all_aliens:
            for alien in row:
                alien.alien_x_pos += self.speed
                alien.alien_rect.topleft = (alien.alien_x_pos, alien.alien_y_pos - 5)
                if alien.alien_x_pos >= 580 or alien.alien_x_pos <= 0:
                    self.hit_wall = True

        if self.hit_wall:
            self.speed *= -1
            self.hit_wall = False
    
    def check_collision_bullets(self, total_spaceship_bullets):
        for bullet in total_spaceship_bullets:
            for row in self.all_aliens:
                for alien in row:
                    if bullet.bullet_rect.colliderect(alien.alien_rect):
                        row.pop(row.index(alien))
                        return True
    
    def choose_alien_shot(self):  
        try:    
            not_empty_rows = [row for row in self.all_aliens if row != []]
            random_row = random.choice(not_empty_rows)
            if not_empty_rows != []:
                random_alien = random.choice(random_row)
                return random_alien
        except IndexError:
            self.wiped = True

    def reset_aliens(self):
        self.max_aliens()
        self.max_rows()
        self.max_y_pos()
        self.store_aliens()
        
    def max_aliens(self):
        if self.total_alien_per_row < 15:
            self.total_alien_per_row += 1
        else:
            self.total_alien_per_row = 15
    
    def max_rows(self):
        if self.number_rows < 5:
            self.number_rows += 1
        else:
            self.number_rows = 5
        
    def max_y_pos(self):
        if self.alien_y_pos == 160:
            self.alien_y_pos = 160
        else:
            self.alien_y_pos += 20
        
    def clear_bullets(self):
        self.total_aliens_bullets = []
    
    def clear_aliens(self):
        self.all_aliens = []
