import pygame
from pygame.math import Vector2 as vec

from scripts.settings import *

class ChunkBor(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)

        self.image = pygame.transform.scale(pygame.image.load("assets/border.png").convert_alpha(),(TILESIZE* SCALE, TILESIZE*SCALE))
        self.rect = self.image.get_frect()


    def draw(self,screen):
        pass

    def update(self,dt):
        mos_pos = pygame.mouse.get_pos()
        self.rect.center = mos_pos
