import pygame
from sys import exit
from pygame.locals import *

from scripts.sprites import *
from scripts.settings import *

pygame.init()


display = pygame.display.set_mode(HEIGHT,WIDTH)
clock = pygame.time.Clock()



draw_sprites = pygame.sprite.Group()
update_sprites = pygame.sprite.Group()

border = ChunkBor([draw_sprites,update_sprites],10)


while RUNNING:
    dt = clock.tick() / 1000
    display.fill((100,255,100))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False
        elif event.type == QUIT:
            RUNNING = False

    draw_sprites.draw(display)
    update_sprites.update(dt)

    pygame.display.flip()



