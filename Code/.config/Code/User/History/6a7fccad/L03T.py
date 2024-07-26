import pygame as pg
from sys import exit
from random import randint
from pygame.constants import *

#Dev Imports
from icecream import ic



class Game:
    def __init__(self,SIZE,FPS=60):
        pg.init()
        pg.mixer.init()

        # CONST
        self.SIZE = SIZE
        self.FPS  = FPS
        self.RUNNING = True

        self.screen = pg.display.set_mode(self.SIZE)
        self.clock = pg.time.Clock()


    def run(self):
        while self.RUNNING:
            self.update()

    def keyboard_inputs(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.key.get_pressed()[K_ESCAPE]:
                ic(event.type,)
                pg.quit()
                exit()

    def update(self):

        self.keyboard_inputs()

        self.clock.tick(self.FPS)
        pg.display.flip()


if __name__ == "__main__":
    game = Game((900,700))
    game.run()
