import pygame
from sys import exit
from pygame.locals import *

pygame.init()


display = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
running = True

while running:
    display.fill((100,255,100))

    for event in pygame.event.get():
        if event == pygame.key.get_pressed()[K_ESCAPE]:
            pygame.quit
            exit()
        elif event.type == QUIT:
            pygame.quit
            exit()

    clock.tick()
    pygame.display.flip()



