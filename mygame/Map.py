from pico2d import *
import play_state
import random

class Map:
    image = random.randint(0, 2)

    def __init__(self):
        if Map.image == 1:
            self.image = load_image('TUK_GROUND.png')
        elif Map.image == 2:
            self.image = load_image('grass_map.png')

    def draw(self):
        self.image.draw(play_state.TUK_GROUND_FULL_WIDTH // 2, play_state.TUK_GROUND_FULL_HEIGHT // 2)
