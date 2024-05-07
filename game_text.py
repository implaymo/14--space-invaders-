import pygame

class Lifes():
    def __init__(self) -> None:
        self.green = 0, 255, 0
        self.blue = (0, 0, 128)
        self.font = pygame.font.Font('freesansbold.ttf', 15)
        self.x_pos = 10
        self.y_pos = 380
    
    
    def display_text(self, screen, spaceship_lifes):
        self.text = self.font.render(f"Lifes: {spaceship_lifes}", True, self.green, self.blue)
        self.text_rect = self.text.get_rect()
        screen.blit(self.text, (self.x_pos, self.y_pos))