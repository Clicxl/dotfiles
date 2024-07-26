import pygame
import os
from random import randint


class Image:
    def __init__(self):
        pass

    def get_images(self, path, scale=1):
        images: dict = {}
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            img = pygame.image.load(full_path).convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * scale, img.get_height() * scale)
            )
            images[str(file.split(".")[0])] = img
        return images

    def get_animations(self, path):
        animation: dict = {}
        for file_name in os.listdir(path):
            animation.update({file_name: []})
        return animation


def play(file, **kwargs):
    # **kwargs => vol,fade=0,loop=0
    mixer = pygame.mixer.Sound(file)
    mixer.set_volume(kwargs["vol"])
    mixer.fadeout(kwargs["fade"])
    mixer.play(kwargs["loop"], kwargs["fade"])


class Particles:
    particles = []

    def __init__(self, pos: pygame.Vector2, vel: pygame.Vector2, timer: int,screen:pygame.Surface):
        self.pos = pos
        self.vel = vel
        self.timer = timer

        self.draw(screen)
        self.update()

    def update(self):
        self.particles.append(self)
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.timer -= 0.1

        if self.timer <= 0:
            self.particles.remove(self)

    def draw(self,screen):
        pygame.draw.circle(self.image, (0, 0, 0), (0, 0), self.timer)
