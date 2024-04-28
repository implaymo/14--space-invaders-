import pygame

class Bullet():
    def __init__(self,  bullet_x_pos, bullet_y_pos) -> None:
        self.direction = -1
        self.bullet_x_pos = bullet_x_pos
        self.bullet_y_pos = bullet_y_pos
        self.radius = 5
        self.color = "black"
        self.vel = self.direction
    
    def draw_bullet(self, screen):
        self.bullet = pygame.draw.circle(screen, self.color, center=[self.bullet_x_pos, self.bullet_y_pos ], radius=self.radius)

    def update_bullet(self):
        self.bullet_y_pos *= self.vel
