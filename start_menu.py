import pygame 

class StartMenu():
    def __init__(self, screen, background_image, start_button) -> None:
        screen.fill((0, 0, 0))                       
        screen.blit(background_image, (0,0))
        start_button = start_button
        pygame.display.update()
