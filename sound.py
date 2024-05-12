import pygame

class GameSounds():
    def __init__(self, path) -> None:
        self.game_sound = pygame.mixer.Sound(path)
        self.game_sound.set_volume(0.2)