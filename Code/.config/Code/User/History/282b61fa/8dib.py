import pygame
from pygame.constants import *
from random import randint


class Entity(pygame.sprite.Sprite):
    def __init__(
        self,
        size: list[int],
        color: list[int],
        vel: list[int],
        pos: list[int],
        group: pygame.sprite.Group
    ):
        super.__init__()
        self.image: pygame.Surface = pygame.Surface(size=size)
        self.rect = self.image.get_rect(center=pos)


    def update(self,dt):
        self.group.add(self)
