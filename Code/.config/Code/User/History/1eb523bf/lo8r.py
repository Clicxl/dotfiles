import pygame
from pygame.math import Vector2 as vec

class ChunkBor(pygame.sprite.Sprite):
    def __init__(self,groups,scale):
        super().__init__(groups)

        self.image = (pygame.image.load("assets/border.png").convert_alpha())
        self.rect = self.image.get_frect()


    def draw(self,screen):
        pass

    def update(self,dt):
        mos_pos = pygame.mouse.get_pos()
        self.rect.center = mos_pos
