import pygame
from pytmx.util_pygame import load_pygame
from scripts.Settings import *
from scripts.Camera import *
from scripts.Characters import *
from scripts.Objects import *


class State:
    def __init__(self, game):
        self.game = game

    def enter_state(self):
        if len(self.game.states) > 1:
            self.prev_state = self.game.states[-1]
        self.game.states.append(self)

    def exit_state(self):
        self.game.states.pop()

    def debugger(self, defbug_list):
        for index, name in enumerate(defbug_list):
            self.game.render_font(
                str(name), COLORS["white"], vec(10, 35 * index), self.game.font, False
            )

    def draw(self, screen):
        pass

    def update(self, dt):
        pass


class SplashScreen(State):
    def __init__(self, game):
        super().__init__(game)

    def draw(self, screen):
        screen.fill(COLORS["blue"])
        self.game.render_font(
            "Splash Screen: Press Space",
            COLORS["white"],
            pygame.Vector2(WIDTH / 2, HEIGHT / 2),
            self.game.font,
        )

    def update(self, dt):
        if INPUTS["space"] == True:
            Scene(self.game).enter_state()
            self.game.reset_input()


class Scene(State):
    def __init__(self, game):
        super().__init__(game)

        self.camera = Camera(self)
        self.update_sprites = pygame.sprite.Group()
        self.draw_sprites = pygame.sprite.Group()

        self.tmx_data = load_pygame("assets/Scenes/0/0.tmx")
        self.create_scene()

    def create_scene(self):
        layers = []

        for layer in self.tmx_data.layers:
            layers.append(layer.name)

        if "blocks" in layers:
            for x, y, surf in self.tmx_data.get_layer_by_name("blocks").tiles():
                Object([self.draw_sprites], (x * TILESIZE, y * TILESIZE), surf)

        if "entries" in layers:
            for obj in self.tmx_data.get_layer_by_name("entries"):
                if obj.name == "0":
                    self.player = Player(
                        self.game,
                        self,
                        [self.update_sprites, self.draw_sprites],
                        (obj.x, obj.y),
                        "player",
                    )

    def draw(self, screen):
        screen.fill(COLORS["red"])
        self.camera.draw(screen,[self.draw_sprites])

        self.draw_sprites.draw(screen)
        self.debugger([str(f"FPS: {self.game.clock.get_fps():.2f}")])

    def update(self, dt):
        self.update_sprites.update(dt)
        self.camera.update(dt,self.player)
