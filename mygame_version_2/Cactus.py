from pico2d import *
import server

class Cactus:
    def __init__(self, type, number, x, y):
        self.type = type
        self.number = number
        self.x, self.y = x, y

    def draw(self):
        self.sx, self.sy = self.x - server.world.window_left, self.y - server.world.window_bottom
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        self.sx, self.sy = self.x - server.world.window_left, self.y - server.world.window_bottom
        if self.type == 'short':
            return self.sx-10, self.sy-25, self.sx+15, self.sy+35
        elif self.type == 'small':
            return self.sx-20, self.sy-20, self.sx+30, self.sy+25
        elif self.type == 'big':
            return self.sx-40, self.sy-35, self.sx+35, self.sy+45
        elif self.type == 'long':
            return self.sx-20, self.sy-30, self.sx+25, self.sy+35

    def handle_collision(self, other, group):
        pass
