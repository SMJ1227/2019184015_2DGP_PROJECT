from pico2d import *
import time

class Bullet:
    def __init__(self):
        self.image = load_image('bullet.png')
        self.bullets = 6

    def reloading(self):
        self.bullets = 6

    def update(self):
        pass

    def draw(self):
        for i in range(self.bullets):
            self.image.draw(1200, 100 + (i * 30))

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            self.reloading()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            self.bullets -= 1
            if self.bullets == 0:
                self.reloading()
