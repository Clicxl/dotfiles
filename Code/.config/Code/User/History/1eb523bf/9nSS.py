import pygame

class ChunkBor(pygame.sprite.Sprite):
    def __init__(self,groups,pos,size):
        super().__init__(groups)

        self.image = pygame.Surface(size)
        self.rect = self.image.get_frect(center=pos)

    def draw(self,screen)