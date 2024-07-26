import pygame


def font(text: str, color: tuple, font: pygame.Font, pos: pygame.Vector2, screen:pygame.Surface,centerlized: bool = True):

    surf = font.render(str(text), False, color)
    rect = surf.get_rect(
        center=pos) if centerlized else surf.get_rect(topleft=pos)

    screen.blit(surf,rect)
