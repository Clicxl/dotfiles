import pygame
import os

class Image:
    def images(self,path):
        images:list = []
        for file in os.listdir(path):
            full_path = os.path.join(path,file)
            image = pygame.image.load(full_path).convert_alpha()
            images.append(image)

        return image

    def animation(self,path):
        animation:dict = {}
        for file_name in os.listdir(path):
            animation.update({file_name:[]})

        return animation

