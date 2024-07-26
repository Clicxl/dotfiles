import pygame
import os


class Image:
    def __init__(self):
        pass

    def get_images(self, path):
        images: list = []
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            img = pygame.transform.scale(pygame.image.load(full_path).convert_alpha(),())
            images.append(img)
        return images

    def get_animations(self, path):
        animation: dict = {}
        for file_name in os.listdir(path):
            animation.update({file_name: []})
        return animation
