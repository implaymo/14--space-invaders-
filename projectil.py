import pygame

class Bullet():
    def __init__(self,screen, bullet_x_pos, bullet_y_pos) -> None:
        self.direction = -1
        self.radius = 5
        self.bullet = pygame.draw.circle(screen, color="black", center=[bullet_x_pos, bullet_y_pos], radius=self.radius)
        self.vel = 8 * self.direction