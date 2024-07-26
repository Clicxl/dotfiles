import pygame

class ChunkBor(pygame.sprite.Sprite):
    def __init__(self,groups,pos,size,color):
        super().__init__(groups)

        self.image = pygame.Surface(size)
        self.rect = self.image.get_frect(center=pos)

    def border(self,size,color):
        pygame.draw.rect(self.image,(255,255,255),(*size,*))

    def draw(self,screen):
        pass

    def update(self,dt):
        pass