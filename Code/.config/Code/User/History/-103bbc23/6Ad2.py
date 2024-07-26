import pygame
from os import listdir

class Image:
    def images(self,path):
        images = []
        for file in listdir(path):
            
