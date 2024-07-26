import pygame
from sys import exit
from pygame.locals import *

from scripts.sprites import *
from scripts.settings import *

pygame.init()


display = pygame.display.set_mode(HEIGHT,WIDTH)
clock = pygame.time.Clock()
running = True
TILESIZE = 100

draw_sprites = pygame.sprite.Group()
update_sprites = pygame.sprite.Group()

border = ChunkBor([draw_sprites,update_sprites],TILESIZE)


while running:
    dt = clock.tick() / 1000
    display.fill((100,255,100))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    draw_sprites.draw(display)
    update_sprites.update(dt)

    pygame.display.flip()



