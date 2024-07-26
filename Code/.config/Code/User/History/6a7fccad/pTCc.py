import pygame as pg
from sys import exit
from random import randint


class Game:
    def __init__(self,SIZE,FPS=60):
        pg.init()
        pg.mixer.init()

        # CONST
        self.SIZE = SIZE
        self.FPS  = FPS


        self.screen = pg.display.set_mode(self.SIZE)
        self.clock = self.time.Clock()

    def update(self):
        self.clock.tick(self.FPS)
        self.screen.update()


if __name__ == "__main__":
    game = Game((900,700))
    game.update()
