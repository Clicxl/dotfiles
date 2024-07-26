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
        outer = pygame.Surface((*self.size))
        pygame.draw.rect(self.image,(255,255,255),(self.size[0]-1,self.size[1]-1,*self.pos))

    def draw(self,screen):
        pass

    def update(self,dt):
        pass