from pico2d import *
import random
import play_state

class Monster:
    def __init__(self):
        self.image = load_image('monster.png')
        self.monster_x = random.randint(0, play_state.TUK_GROUND_FULL_WIDTH)
        self.monster_y = random.randint(0, play_state.TUK_GROUND_FULL_HEIGHT)
        self.t = 0

    def update(self):
        self.monster_x = (1 - self.t) * self.monster_x + self.t * play_state.character.character_x
        self.monster_y = (1 - self.t) * self.monster_y + self.t * play_state.character.character_y
        self.t += 0.00001

    def draw(self):
        self.image.draw(self.monster_x, self.monster_y)