import pygame, csv
from scripts.Settings import *


class Camera(pygame.sprite.Group):
    def __init__(self, scene):
        self.offset = vec()
        self.visible_window = pygame.FRect(0, 0, WIDTH, HEIGHT)
        self.delay = 2

    def update(self, dt):
        mouse = pygame.mouse.get_pos()


        self.offset.x = max(0, min(self.offset.x, self.scene_size[0] - WIDTH))
        self.offset.y = max(0, min(self.offset.y, self.scene_size[1] - HEIGHT))

        self.visible_window.x = self.offset.x
        self.visible_window.y = self.offset.y

    def draw(self, screen, group):
        screen.fill(COLORS["red"])
        for layer in LAYERS:
            for sprite in sorted(group, key=lambda sprite: sprite.rect.centery):
                if (
                    self.visible_window.colliderect(sprite.rect)
                    and sprite.z_index == layer
                ):
                    offset = sprite.rect.topleft - self.offset
                    screen.blit(sprite.image, offset)
