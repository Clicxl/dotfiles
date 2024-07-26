import pygame
from pygame.math import Vector2 as vec

from scripts.settings import *

class Chunk:
    def __init__(self):
        self.chunk = []

        self.image = pygame.Surface((TILESIZE*SCALE, TILESIZE*SCALE))
        self.gen_chunk()
        print(self.chunk)


    def gen_chunk(self):
        for col in range(int(HEIGHT/TILESIZE*SCALE)):
            self.chunk.append([])

            for row,row_no in enumerate(self.chunk):
                row = {
                    "rect" : self.image.get_frect(center=(
                        (col*TILESIZE*SCALE) + (TILESIZE /), (row_no*TILESIZE*SCALE) + (TILESIZE /)
                    )),
                    "bordered" : False
                }
