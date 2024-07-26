import pygame as p
from sys import exit
from icecream import ic
from pygame.locals import *
from math import pi

p.init()

WIDTH, HEIGHT = 1280 , 720
MAXFPS = 60
CLOCK = p.time.Clock()
CIRCUMFERENCE = 6378.1  * pi * 2 

screen = p.display.set_mode((WIDTH, HEIGHT))
running = True


class Runner:
    def __init__(self,vel,distance,times=1) -> None:
        self.vel = vel
        self.distance = distance
        self.time = self.time_taken(vel,distance,times)
        
    def time_taken(self,vel,distance,times):
        time = times(distance/vel)
        return time

snail = Runner(0.002,CIRCUMFERENCE)
cheeta = Runner(40,CIRCUMFERENCE,100000)
        
ic(snail.time,cheeta.time)



# while running:
    
#     screen.fill('black')
    
#     for e in p.event.get():
#         if e.type == QUIT:
#             running = False
#             exit()
#         if e.type == KEYDOWN:
#             if e.key == K_ESCAPE:
#                 running = False
#                 exit()
    
#     CLOCK.tick(MAXFPS)
#     p.display.flip()
