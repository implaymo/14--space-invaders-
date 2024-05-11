import pygame

class GameText():
    def __init__(self) -> None:
        self.level = 1
        self.font = 'freesansbold.ttf'
        
    def show_game_info(self, screen, x_pos, y_pos, message, text_color, font_size=15):
        self.text_color = text_color
        font = pygame.font.Font(self.font, font_size)
        self.text = font.render(message, True, self.text_color)
        self.text_rect = self.text.get_rect()
        screen.blit(self.text, (x_pos, y_pos))

    def delay_message(self, screen, x_pos, y_pos, font_size, message):
        self.show_game_info(screen=screen, x_pos=x_pos, y_pos=y_pos, text_color=self.text_color, font_size=font_size, message=message)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        
