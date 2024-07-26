import pygame
from pygame.constants import *
from random import randint

class Entity(pygame.sprite.Sprite):
    def __init__(self,size:list[int],color:list[int],vel:list[int]):
        super.__init__()
