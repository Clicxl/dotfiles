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
        self.clock = pg.time.Clock()

    

    def keyboard_inputs(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.key.get_pressed()[pg.K_ESCAPE]:
                pg.quit()
                exit()

    def update(self):

        self.keyboard_inputs()

        self.clock.tick(self.FPS)
        pg.display.flip()


if __name__ == "__main__":
    game = Game((900,700))
    game.update()
