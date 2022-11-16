from pico2d import *
import random
import play_state
import game_framework
import game_world

class Monster:
    image = None

    def __init__(self):
        if Monster.image == None:
            Monster.image = load_image('monster.png')
        self.monster_x = random.randint(0, play_state.TUK_GROUND_FULL_WIDTH)
        self.monster_y = random.randint(0, play_state.TUK_GROUND_FULL_HEIGHT)
        self.t = 0
        self.a = 0

    def update(self):
        self.monster_x = (1 - self.t) * self.monster_x + self.t * play_state.character.character_x
        self.monster_y = (1 - self.t) * self.monster_y + self.t * play_state.character.character_y
        self.t += 0.000001

    def draw(self):
        self.image.draw(self.monster_x, self.monster_y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.monster_x-30, self.monster_y-25, self.monster_x+30, self.monster_y+25

    def handle_event(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN:
            print(self.a)

    def handle_collision(self, other, group):
        if group == 'target:monster':
            game_world.remove_object(self)
