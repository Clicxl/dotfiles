import pygame
from scripts.Settings import *
from scripts.Utils import Image


class Tile(pygame.sprite.Sprite):
    img_util = Image()

    def __init__(self, groups, row, col, surfs):
        super().__init__(groups)
        self.col = col
        self.row = row
        self.value = 00
        self.surfs = surfs
        self.clicked = False
        self.frame_index = 0

        self.image = self.surfs[str(self.value)]
        self.rect = self.image.get_frect()

    def get_pos(self):
        return self.col, self.row

    def draw(self, screen):
        pass

    def update(self, dt):
        self.image = self.surfs[str(self.value)]

    def __repr__(self):
        return f"Tile {self.col}x{self.row} value: {self.value}"

    def get_clicked(
        self,
    ):
        mouse = pygame.mouse.get_pos()
        if (
            self.rect.collidepoint(mouse)
            and INPUTS["left_click"]
            and self.clicked == False
        ):
            return True

        elif INPUTS["left_click"] == False:
            return False
