import pygame
from pygame.constants import *
from sys import exit
from scripts.Settings import *
from scripts.States import *
from scripts.Characters import *


class Game:
    def __init__(self):

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(FONT, 3 * TILESIZE)
        self.states = []

        # State Classes
        self.splash_screen = SplashScreen(self)

        self.states.append(self.splash_screen)

    def user_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                exit()

            if event.type == pygame.KEYDOWN:
                # KEYDOWN

                # Space & Escape
                if event.key == K_ESCAPE:
                    INPUTS["escape"] = True
                    self.running = False
                elif event.key == K_SPACE:
                    INPUTS["space"] = True

                # Keyboard wasd or arrow
                elif event.key in (K_s, K_DOWN):
                    INPUTS["down"] = True
                elif event.key in (K_w, K_UP):
                    INPUTS["up"] = True
                elif event.key in (K_d, K_RIGHT):
                    INPUTS["right"] = True
                elif event.key in (K_a, K_LEFT):
                    INPUTS["left"] = True

            if event.type == pygame.KEYUP:
                # KEYUP
                # Space & Escape
                if event.key == K_ESCAPE:
                    INPUTS["escape"] = False
                elif event.key == K_SPACE:
                    INPUTS["space"] = False

                # Keyboard wasd or arrow
                if event.key in (K_DOWN, K_s):
                    INPUTS["down"] = False
                elif event.key in (K_UP, K_w):
                    INPUTS["up"] = False
                elif event.key in (K_RIGHT, K_d):
                    INPUTS["right"] = False
                elif event.key in (K_LEFT, K_a):
                    INPUTS["left"] = False

            # MOOUSEDOWN
            # Mouse Wheel - Scroll
            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    INPUTS["scroll_up"] = True
                elif event.y == -1:
                    INPUTS["scroll_down"] = True

            # Mouse Button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    INPUTS["left_click"] = True
                elif event.button == 3:
                    INPUTS["right_click"] = True
                elif event.button == 2:
                    INPUTS["scroll_down"] = True
                elif event.button == 4:
                    INPUTS["scroll_up"] = True

            # Mouse Button
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    INPUTS["left_click"] = False
                elif event.button == 3:
                    INPUTS["right_click"] = False
                elif event.button == 2:
                    INPUTS["scroll_down"] = False
                elif event.button == 4:
                    INPUTS["scroll_up"] = False

    def reset_input(self):
        for key in INPUTS:
            INPUTS[key] = False

    # Utils
    def render_font(
        self,
        text: str,
        color: tuple,
        pos: pygame.Vector2,
        font: pygame.font.Font,
        centerlized: bool = True,
    ):

        surf = font.render(str(text), False, color)
        rect = surf.get_rect(center=pos) if centerlized else surf.get_rect(topleft=pos)
        self.screen.blit(surf, rect)

    def custom_crosshair(self):
        pygame.mouse.set_visible(False)
        crosshari = pygame.transform.scale(
            pygame.image.load(
                "assets/Images/game_assets/Crosshair.png"
            ).convert_alpha(),
            (TILESIZE * SCALE, TILESIZE * SCALE),
        )
        crosshari.set_alpha(75)
        crosshair.set_pallet()
        crosshair_rect = crosshari.get_frect(center=pygame.mouse.get_pos())
        self.screen.blit(crosshari, crosshair_rect.center)

    def loop(self):
        while self.running:
            self.dt = self.clock.tick() / 1000
            self.user_input()
            self.screen.fill(COLORS["black"])

            self.states[-1].update(self.dt)
            self.states[-1].draw(self.screen)

            self.custom_crosshair()
            pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.loop()
