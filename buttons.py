import pygame
import os

class Button():
    def __init__(self, width, height, x_pos, y_pos) -> None:
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def image_button(self, screen, path):
        self.image_path = os.path.join("images", path)
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image_resized = pygame.transform.scale(self.image, (self.width, self.height))
        self.image_rect = self.image_resized.get_rect(center=(self.x_pos + self.width / 2, self.y_pos + self.height / 2))
        self.image_rect.topleft = (self.x_pos, self.y_pos)
        screen.blit(self.image_resized, (self.x_pos, self.y_pos))
        
    def create_button(self, screen, text_color, bg_color, text, font_size=15):
        self.font = pygame.font.Font(None, font_size)
        self.button_rect = pygame.draw.rect(screen, bg_color, (self.x_pos, self.y_pos, self.width, self.height))
        text = self.font.render(text, True, text_color)
        text_rect = text.get_rect(center=(self.x_pos + self.width / 2, self.y_pos + self.height / 2))
        screen.blit(text, text_rect)