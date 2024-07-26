import pygame
from sys import exit
from pygame.locals import *

from sprites import *

pygame.init()


display = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
running = True

draw_sprites = pygame.sprite.Group()
update_sprites = pygame.sprite.Group()

border = ChunkBor([draw_sprites,update_sprites])


while running:
    display.fill((100,255,100))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    draw_sprites.draw(display)

    clock.tick()
    pygame.display.flip()



