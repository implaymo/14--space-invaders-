import pygame

class Button():
    def __init__(self, width, height, x_pos, y_pos, text, text_color, bg_color, font_size=15) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.button_surface = pygame.Surface((self.width, self.height))
        self.text = text
        self.bg_color = bg_color
        self.text_color = text_color
        self.level = 1
        self.font = pygame.font.Font(None, 24)
        self.font_size = font_size
        
    def create_button(self, screen):
        self.button_rect = pygame.draw.rect(screen, self.bg_color, (self.x_pos, self.y_pos, self.width, self.height))
        text = self.font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=(self.x_pos + self.width / 2, self.y_pos + self.height / 2))
        screen.blit(text, text_rect)
        
