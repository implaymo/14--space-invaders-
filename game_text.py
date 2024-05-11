import pygame

class GameText():
    def __init__(self) -> None:
        self.level = 1
        self.font = 'freesansbold.ttf'

        
    def show_game_info(self, screen, x_pos, y_pos, message, text_color="green", font_size=15):
        font = pygame.font.Font(self.font, font_size)
        self.text = font.render(message, True, text_color)
        self.text_rect = self.text.get_rect()
        screen.blit(self.text, (x_pos, y_pos))

    def delay_message(self, screen, x_pos, y_pos, font_size, message, text_color="green", background_color="blue"):
        font = pygame.font.Font(self.font, font_size)
        self.text = font.render(message, True, text_color, background_color)
        self.text_rect = self.text.get_rect()
        screen.blit(self.text, (x_pos, y_pos))

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        
