import pygame
from pygame.math import Vector2 as vec

class ChunkBor(pygame.sprite.Sprite):
    def __init__(self,groups,pos,size,color):
        super().__init__(groups)

        self.pos = vec(pos)
        self.size = size
        self.color = color

        self.image = pygame.Surface(size)
        self.rect = self.image.get_frect(center=pos)

    def border(self):



    def draw(self,screen):
        pass

    def update(self,dt):
        pass