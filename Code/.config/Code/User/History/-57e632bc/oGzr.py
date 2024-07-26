import pygame
from scripts.Settings import *


class Object(pygame.sprite.Sprite):
    def __init__(self, groups, pos, surf=pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(groups)
        

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
