import pygame
from sys import exit
from pygame.locals import *

pygame.init()


display = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
running = True

def chunk():
    mos_pos = pygame.mouse.get_pos()
    pygame.draw.rect(display,(255,255,255),(16,16,*mos_pos))



while running:
    display.fill((100,255,100))
    chunk()
    for event in pygame.event.get():
        if event.type == pygame.key.get_pressed()[K_ESCAPE]:
            pygame.quit
            exit()
        elif event.type == QUIT:
            pygame.quit
            exit()

    clock.tick()
    pygame.display.flip()



