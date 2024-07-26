import pygame
import os


class Image:
    def __init__(self):
        pass

    def get_images(self, path):
        images: list = []
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            img = pygame.image.load(full_path).convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width()*3, img.get_height()*3))
            images.append(img)
        return images

    def get_animations(self, path):
        animation: dict = {}
        for file_name in os.listdir(path):
            animation.update({file_name: []})
        return animation
