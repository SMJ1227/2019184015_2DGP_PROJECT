from pico2d import *
import play_state
import random

class Map:
    image = random.randint(0, 3)

    def __init__(self):
        if Map.image == 1:
            self.image = load_image('grass_map.png')
        elif Map.image == 2:
            self.image = load_image('snow_map.png')
        elif Map.image == 3:
            self.image = load_image('dessert_map.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(640, 512)
