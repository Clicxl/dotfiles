import pygame
from pygame.constants import *
from random import randint


class Entity(pygame.sprite.Sprite):
    def __init__(
        self,
        size: tuple[int],
        color: list[int],
        vel: pygame.Vector2,
        pos: pygame.Vector2 ,
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
        self.rect:pygame.Rect = self.image.get_rect()

        self.image.fill(self.color)
        self.rect.center = self.pos

        self.group.add(self)

    def update(self,dt):
        self.group.draw(self.screen)
