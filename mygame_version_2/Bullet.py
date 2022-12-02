from pico2d import *
import time

class Bullet:
    relaod = False

    def __init__(self):
        self.image = load_image('bullet.png')
        self.bullets = 6
        self.reload_start = time.time()
        self.time = time.time()

    def reloading(self):
        self.bullets = 6

    def update(self):
        if Bullet.relaod:
            self.time = time.time()
        if self.time - self.reload_start >= 2:
            self.reloading()
            self.reload_start = time.time()
            Bullet.relaod = False

    def draw(self):
        for i in range(self.bullets):
            self.image.draw(1200, 100 + (i * 30))

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            Bullet.relaod = True
            self.reload_start = time.time()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            self.bullets -= 1
