import pygame
from pygame.math import Vector2 as vec

class ChunkBor(pygame.sprite.Sprite):
    def __init__(self,groups,pos,size,color):
        super().__init__(groups)

        self.pos = vec(pos)
        self.size = size
        self.color = color

        self.image = pygame.image.load("assets/border.png").convert_alpha()
        self.rect = self.image.get_frect(center=pos)


    def draw(self,screen):
        pass

    def update(self,dt):
        pass