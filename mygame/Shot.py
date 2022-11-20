from pico2d import *
import game_world

class Shot:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def update(self):
        pass

    def draw(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        if group == 'shot:monster':
            game_world.remove_object(self)
        else:
            game_world.remove_object(self)
