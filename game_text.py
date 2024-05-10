import pygame

class GameText():
    def __init__(self) -> None:
        self.green = 0, 255, 0
        self.blue = (0, 0, 128)
        self.level = 1
        self.font = 'freesansbold.ttf'
        
    def show_info_current(self, screen, x_pos, y_pos, message, font_size=15):
        font = pygame.font.Font(self.font, font_size)
        self.text = font.render(message, True, self.green, self.blue)
        self.text_rect = self.text.get_rect()
        screen.blit(self.text, (x_pos, y_pos))

    def show_info_delay(self, screen, x_pos, y_pos, font_size, message):
        self.show_info_current(screen=screen, x_pos=x_pos, y_pos=y_pos, font_size=font_size, message=message)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        
    def increase_level(self):
        self.level += 1
