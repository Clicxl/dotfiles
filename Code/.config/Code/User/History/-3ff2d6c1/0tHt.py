from pygame.math import Vector2 as vec

WIDTH, HEIGHT = 300, 300
FPS = 60
TILESIZE = 16
FONT = "assets/Fonts/font.ttf"
SCALE = 1

COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (158, 50, 43),
    "green": (43, 255, 135),
    "blue": (89, 43, 255),
    "yellow": (216, 255, 43),
}
INPUTS = {
    "left_click": False,
    "space": False,
    "escape": False,
}

LAYERS = ["background", "objects", "blocks",
          "characters", "particles", "foreground"]
