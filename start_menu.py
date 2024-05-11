import pygame 

class StartMenu():
    def __init__(self, screen, start_button) -> None:
        self.screen = screen
        self.start_button = start_button
        pygame.display.update()
