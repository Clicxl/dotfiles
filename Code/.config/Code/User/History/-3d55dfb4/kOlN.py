from scripts.Settings import *
from scripts.Image import Image
import pygame


load_image = Image()


class NPC(pygame.sprite.Sprite):
    def __init__(self, game, scene, group, pos, z, name, dim: int = 4):
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
        self.hitbox = self.rect.copy().inflate(
            -self.rect.width / 2, -self.rect.height / 2
        )

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

    def get_collision_list(self, group):
        collidable_list = pygame.sprite.spritecollide(self, group, False)
        return collidable_list

    def get_direction(self):
        angle = self.vel.angle_to(vec(0,1))
        angle = (angle + 360) % 360
        if 45 <= angle < 135: return 'right'
        elif 135 <= angle < 225: return 'up'
        elif 225 <= angle < 315: return 'left'
        else: return 'down'

    def collisions(self, axis, group):
        for sprite in self.get_collision_list(group):
            if self.hitbox.colliderect(sprite.hitbox):
                if axis == "x":
                    if self.vel.x >= 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.vel.x <= 0:
                        self.hitbox.left = sprite.hitbox.right
                if axis == "y":
                    if self.vel.y >= 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.vel.y <= 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def physics(self, dt):
        # X Axis
        self.acc.x += self.vel.x * self.fric
        self.vel.x += self.acc.x * dt
        self.hitbox.centerx += self.vel.x * dt + (self.vel.x / 2) * dt
        self.rect.centerx = self.hitbox.centerx
        self.collisions("x", self.scene.block_sprites)

        # Y Axis
        self.acc.y += self.vel.y * self.fric
        self.vel.y += self.acc.y * dt
        self.hitbox.centery += self.vel.y * dt + (self.vel.y / 2) * dt
        self.rect.centery = self.hitbox.centery
        self.collisions("y", self.scene.block_sprites)

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
