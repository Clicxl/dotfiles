import pygame

def font(filename,text:str,size:int):
    Font = pygame.Font(filename,size)
    font_surf = Font.