import pygame 
import os

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Space Invaders")


image_path = os.path.join("images", "spaceship.png")
spaceship_img = pygame.image.load(image_path).convert_alpha()
spaceshit_rect = spaceship_img.get_rect()

rect_x = 100
rect_y = 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("purple")
    pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, spaceshit_rect.width, spaceshit_rect.height))

    screen.blit(spaceship_img, (rect_x, rect_y))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()