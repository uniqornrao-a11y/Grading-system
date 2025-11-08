import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Visual Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Black background
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)
    pygame.display.flip()
    pygame.draw.circle(screen, (255, 255, 0), (1000,400), 60)