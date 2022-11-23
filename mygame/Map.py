from pico2d import *
import play_state
import random

Map_type = ['grass_map.png', 'snow_map.png', 'dessert_map.png']

class Map:
    image_number = random.randint(0, 2)

    def __init__(self):
        self.image = load_image(Map_type[Map.image_number])
        # if Map.image == 0:
        #     self.image = load_image('grass_map.png')
        # elif Map.image == 1:
        #     self.image = load_image('snow_map.png')
        # elif Map.image == 2:
        #     self.image = load_image('dessert_map.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(640, 512)
