import pygame
from pygame.constants import *
from sys import exit
from scripts.States import *
from scripts.utils import *

WIDTH, HEIGHT = 1000, 700
FPS = 60

COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 124, 115),
    "green": (124, 255, 115),
    "blue": (115, 190, 255),
    'yellow': (243, 255, 115)
}
INPUTS = {
    "left": False,
    "right": False,
    "up": False,
    "down": False,
    "scroll_up": False,
    "scroll_down": False,
    "right_click": False,
    "left_click": False,
    "escape": False,
    'space': False,
    'scroll_down': False,
    "scroll_up": False
}
