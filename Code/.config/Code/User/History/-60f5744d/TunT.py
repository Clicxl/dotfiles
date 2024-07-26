from pygame.math import Vector2 as vec

WIDTH, HEIGHT = 440, 224
FPS = 60
TILESIZE = 16
FONT = "assets/Fonts/font.ttf"

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
