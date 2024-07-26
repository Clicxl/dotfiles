import pygame
from pygame.constants import *
from random import randint


class Entity(pygame.sprite.Sprite):
    def __init__(
        self,
        size: list[int], c
        olor: list[int], vel: list[int], pos: list[int]
    ):
        super.__init__()
        self.image: pygame.Surface = pygame.Surface(size=size)
        self.rect = self.image.get_rect(center=pos)
