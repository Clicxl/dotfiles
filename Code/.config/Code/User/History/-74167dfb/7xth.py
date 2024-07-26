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
        for col_no in range(1,int(HEIGHT/TILESIZE*SCALE)):
            self.chunk.append([])

            for row,row_no in enumerate(self.chunk):
                row = {
                    "rect" : self.image.get_frect(center=(
                        int((col_no*TILESIZE*SCALE) + (TILESIZE / 2)), int((row_no*TILESIZE*SCALE) + (TILESIZE / 2))
                    )),
                    "bordered" : False
                }
