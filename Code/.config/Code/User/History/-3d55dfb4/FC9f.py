from scripts.Settings import *
from scripts.Image import Image
import pygame


load_image = Image()


class NPC(pygame.sprite.Sprite):
    def __init__(self, game, scene, group, pos, z ,name, dim: int = 4):
        super().__init__(group)

        self.game = game
        self.scene = scene
        self.z_index = z
        self.name = name
        self.pos = pos
        self.frame_index = 0

        self.import_images(f"assets/Images/character/{self.name}/")
        self.image = self.animations["idle"][0]
        self.rect = self.image.get_frect(center=self.pos)

        self.speed = 60
        self.force = 2000 * SCALE
        self.acc = vec()
        self.vel = vec()
        self.fric = -15

    def import_images(self, path):
        self.animations = load_image.get_animations(path)

        for animation in self.animations.keys():
            full_path = path + animation
            self.animations[animation] += load_image.get_images(full_path)

    def animate(self, state, fps: int, loop: bool = True):
        self.frame_index += fps

        if self.frame_index >= len(self.animations[state]) - 1:
            if loop:
                self.frame_index = 0
            else:
                self.frame_index = len(self.animations[state]) - 1

        self.image = self.animations[state][int(self.frame_index)]

    def get_collision_list(self):


    def physics(self, dt):
        # X Axis
        self.acc.x += self.vel.x * self.fric
        self.vel.x += self.acc.x * dt
        self.rect.centerx += self.vel.x * dt + (self.vel.x / 2) * dt

        # Y Axis
        self.acc.y += self.vel.y * self.fric
        self.vel.y += self.acc.y * dt
        self.rect.centery += self.vel.y * dt + (self.vel.y / 2) * dt

        if self.vel.magnitude() >= self.speed:
            self.vel = self.vel.normalize() * self.speed

    def update(self, dt):
        self.physics(dt)
        self.animate("idle", 15 * dt)

    def draw(self, screen):
        pass


class Player(NPC):
    def __init__(self, game, scene, group, pos, z, name):
        super().__init__(game, scene, group, pos, z, name)

    def movement(self):
        if INPUTS["left"]:
            self.acc.x = -self.force
        elif INPUTS["right"]:
            self.acc.x = self.force
        else:
            self.acc.x = 0

        if INPUTS["up"]:
            self.acc.y = -self.force
        elif INPUTS["down"]:
            self.acc.y = self.force
        else:
            self.acc.y = 0

    def update(self, dt):
        self.physics(dt)
        self.movement()

        if self.vel.magnitude() < 1:
            self.animate("idle", 15 * dt)
        else:
            self.animate("run", 15 * dt)

    def draw(self, screen):
        pass
