import pygame as p
from sys import exit
from icecream import ic
from pygame.locals import *
from numpy import array

p.init()

WIDTH, HEIGHT = 1280 , 720
MAXFPS = 60
CLOCK = p.time.Clock()

screen = p.display.set_mode((WIDTH, HEIGHT))
running = True


while running:
    
    screen.fill('black')
    
    for e in p.events.get():
        if e.type == QUIT:
            running = False
            exit()
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False
                exit()
    
    CLOCK.tick(MAXFPS)
    p.display.flip()
