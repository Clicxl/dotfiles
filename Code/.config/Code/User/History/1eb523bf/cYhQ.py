import pygame
from pygame.sprite import _Group

class ChunkBor(pygame.sprite.Sprite):
    def __init__(self, *groups: AbstractGroup[_SpriteSupportsGroup]) -> None:
        super().__init__(*groups)