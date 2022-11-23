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
        self.x = random.randint(0, play_state.TUK_GROUND_FULL_WIDTH)
        self.y = random.randint(0, play_state.TUK_GROUND_FULL_HEIGHT)
        self.t = 0
        self.a = None

    def update(self):
        self.x = (1 - self.t) * self.x + self.t * play_state.character.character_x
        self.y = (1 - self.t) * self.y + self.t * play_state.character.character_y
        self.t += 0.000001
        #y=(y2-y1)/(x2-x1)*(x-x1)+y1

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN:
            pass
            #for a, b, group in game_world.all_collision_pairs():
            #    if play_state.collide(a, b):
            #        game_world.remove_object(self)

    def get_bb(self):
        return self.x-30, self.y-25, self.x+30, self.y+25

    def handle_collision(self, other, group):
        pass
        if group == 'target:monster':# and self.a:
            game_world.remove_object(self)
        #    self.a = False
