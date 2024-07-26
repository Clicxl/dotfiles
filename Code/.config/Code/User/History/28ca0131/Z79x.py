import pygame
from scripts.Settings import *


class Camera(pygame.sprite.Group):
    def __init__(self, scene):
        self.offset = vec()
        self.delay = 2

    def update(self,dt,target):
        mouse = pygame.mouse.get_pos()

        self.offset.x = (target.rect.centerx - WIDTH/2) * self.delay * dt
        self.offset.y = (target.rect.centery - HEIGHT/2 ) * self.delay * dt


    def draw(self,screen,group):
        screen.fill(COLORS["red"])
        for sprite in group:
            offset = sprite.rect.topleft - self.offset
            screen.blit(sprite.image,offset)
