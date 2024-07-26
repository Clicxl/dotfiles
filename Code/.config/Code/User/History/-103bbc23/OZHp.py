import pygame
import os

class Image:
    def images(self,path):
        images = []
        for file in os.listdir(path):
            full_path = os.path.join(path,file)
