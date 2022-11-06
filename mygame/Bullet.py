from pico2d import *

class Bullet:
    def __init__(self):
        self.image = load_image('bullet.png')
        self.bullets = 6

    def reloading(self):
        self.bullets = 6

    def draw(self):
        for i in range(self.bullets):
            self.image.draw(1200, 100 + (i * 30))