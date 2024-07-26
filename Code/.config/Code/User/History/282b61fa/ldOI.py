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
        group: pygame.sprite.Group,
        screen:pygame.Surface
    ):

        super().__init__()
        self.size = size
        self.color = color
        self.vel = vel
        self.pos = pos
        self.group = group
        self.screen = screen


        self.image: pygame.Surface = pygame.Surface(size=self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.group.draw()
        self.group.add(self)

    def update(self,dt):
        pass
