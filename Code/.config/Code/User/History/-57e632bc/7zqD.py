import pygame
from scripts.Settings import *


class Object(pygame.sprite.Sprite):
    def __init__(self, groups, pos, surf=pygame.Surface((TILESIZE, TILESIZE)),alpha=225):
        super().__init__(groups)

        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)
        self.hitbox = self.rect.copy().inflate(0, 0)

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
