import pygame
from scripts.Settings import *


class Object(pygame.sprite.Sprite):
    def __init__(self, groups, pos, surf=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)

        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)
        self.hitbox =

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
