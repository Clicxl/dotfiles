import pygame
from pygame.math import Vector2 as vec

from scripts.settings import *

class Chunk:
    def __init__(self):
        self.chunk = []



        for col in range(HEIGHT/TILESIZE*SCALE):
            self.chunk.append([])

            for row in self.chunk:
                row = {
                    "rect" : pygame.get_frect
                }
