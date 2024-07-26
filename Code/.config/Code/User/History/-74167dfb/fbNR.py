import pygame
from pygame.math import Vector2 as vec

from scripts.settings import *

class Chunk:
    def __init__(self):
        self.chunk = []

        self.image = pygame.Surface((TILESIZE*SCALE, TILESIZE*SCALE))


    def gen_chunk(self):
        for col in range(HEIGHT/TILESIZE*SCALE):
            self.chunk.append([])

            for row,row_no in self.chunk:
                row = {
                    "rect" : self.image.get_frect(topleft=())
                }
