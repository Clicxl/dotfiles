import pygame,csv
from scripts.Settings import *


class Camera(pygame.sprite.Group):
    def __init__(self, scene):
        self.offset = vec()
        self.visible_window = pygame.FRect(0,0,WIDTH,HEIGHT)
        self.scene_size = self.get_scene_size(scene)
        self.delay = 2

    def get_scene_size(self,scene):
        with open("assets/Scenes/0/0.csv", newline='') as file:
            reader = csv.reader(file,delimiter=',')
            for row in reader:
                rows = (sum(1 for row in reader) + 1)
                cols = len(row)
        return (cols*TILESIZE,rows*TILESIZE)

    def update(self,dt,target):
        mouse = pygame.mouse.get_pos()

        self.offset.x += (target.rect.centerx - WIDTH/2 - (WIDTH/2 - mouse[0])/4 - self.offset.x) * (dt * self.delay)
        self.offset.y += (target.rect.centery - HEIGHT/2 - (HEIGHT/2 - mouse[1])/4 - self.offset.y) * (dt * self.delay)

        self.offset.x = max(0, min(self.offset.x, self.scene_size[0] - WIDTH))
        self.offset.y = max(0, min(self.offset.y, self.scene_size[1] - HEIGHT))


        self.visible_window.x = self.offset.x
        self.visible_window.y = self.offset.y


    def draw(self,screen,group):
        screen.fill(COLORS["red"])
        for layer in LAYERS:
            for sprite in group:
                if self.visible_window.colliderect(sprite.rect) and sprite.z_index == layer:
                    offset = sprite.rect.topleft - self.offset
                    screen.blit(sprite.image,offset)
