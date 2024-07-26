import pygame
from pygame.constants import *
from random import randint


class Entity(pygame.sprite.Sprite):
    def __init__(
        self,
        size: list[int],
        color: list[int],
        vel: pygame.Vector2,
        pos: list[int],
        group: pygame.sprite.Group
    ):

        super.__init__()
        self.size = size
        self.color = color
        self.vel = vel
        self.pos = pos
        self.group = group


        self.image: pygame.Surface = pygame.Surface(size=self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self,dt):
        self.group.add(self)
