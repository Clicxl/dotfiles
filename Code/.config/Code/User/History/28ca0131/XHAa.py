import pygame
from scripts.Settings import *


class Camera(pygame.sprite.Group):
    def __init__(self, scene):
        self.offset = vec()
        self.delay = 1.5
        self.visible_window = pygame.FRect(0,0,WIDTH,HEIGHT)

    def update(self,dt,target):
        mouse = pygame.mouse.get_pos()

        self.offset.x += (target.rect.centerx - WIDTH/2 - (WIDTH/2 - mouse[0])/4 - self.offset.x) * (dt * self.delay)
        self.offset.y += (target.rect.centery - HEIGHT/2 - (HEIGHT/2 - mouse[1])/4 - self.offset.y) * (dt * self.delay)

        self.visible_window.x = self.offset.x
        self.visible_window.y = self.offset.y


    def draw(self,screen,group):
        screen.fill(COLORS["red"])
        for sprite in group:
            if self.visible_window.colliderect(sprite.rect):
                offset = sprite.rect.topleft - self.offset
                screen.blit(sprite.image,offset)
