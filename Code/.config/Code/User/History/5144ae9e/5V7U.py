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

def time_taken(vel,distance,times=1):
    time = times(distance/vel)
    return time

class Runner:
    def __init__(self,vel,distance) -> None:
        self.vel = vel
        self.distance = distance
        self.time = time_taken(vel,distance)
        self.x = 0
        self.y = 0
        self.width = 100
        self.height = 100
        self.rect = p.Rect(self.x,self.y,self.width,self.height)
        self.image = p.Surface((self.width,self.height))
        self.image.fill('white')
        self.image.set_colorkey('white')
        self.image.set_alpha(255)
        self.image.set_colorkey((255,255,255))
        



while running:
    
    screen.fill('black')
    
    for e in p.event.get():
        if e.type == QUIT:
            running = False
            exit()
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False
                exit()
    
    CLOCK.tick(MAXFPS)
    p.display.flip()
