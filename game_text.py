import pygame

class GameText():
    def __init__(self) -> None:
        self.green = 0, 255, 0
        self.blue = (0, 0, 128)
        self.level = 1
        
    
    def lifes_text(self, screen, spaceship_lifes, x_pos, y_pos):
        font = pygame.font.Font('freesansbold.ttf', 15)
        self.text = font.render(f"Lifes: {spaceship_lifes}", True, self.green, self.blue)
        self.text_rect = self.text.get_rect()
        screen.blit(self.text, (x_pos, y_pos))
        
    def level_text(self, screen, x_pos, y_pos):
        font = pygame.font.Font('freesansbold.ttf', 15)
        self.text = font.render(f"Level: {self.level}", True, self.green, self.blue)
        self.text_rect = self.text.get_rect()
        screen.blit(self.text, (x_pos, y_pos))

    def level_up_text(self, screen, x_pos, y_pos):
        font = pygame.font.Font('freesansbold.ttf', 40)
        self.text = font.render(f"LEVEL {self.level}! MORE SPEED!", True, self.green, self.blue)
        self.text_rect = self.text.get_rect()
        screen.blit(self.text, (x_pos, y_pos))
        
        
    def game_over_text(self, screen, x_pos, y_pos):
        font = pygame.font.Font('freesansbold.ttf', 40)
        self.text = font.render("GAME OVER", True, self.green, self.blue)
        self.text_rect = self.text.get_rect()
        screen.blit(self.text, (x_pos, y_pos))
    
    def restart_text(self, screen, x_pos, y_pos):
        font = pygame.font.Font('freesansbold.ttf', 20)
        self.text = font.render("RESTART?", True, self.green, self.blue)
        self.text_rect = self.text.get_rect()
        screen.blit(self.text, (x_pos, y_pos))