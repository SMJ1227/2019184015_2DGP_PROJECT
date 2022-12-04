from pico2d import *
import random
import server

Map_type = ['grass_map.png', 'snow_map.png', 'dessert_map.png']

class Map:
    image_number = random.randint(0, 2)

    def __init__(self):
        self.image = load_image(Map_type[Map.image_number])
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        self.image.clip_draw_to_origin(
            self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0
        )

    def update(self):
        self.window_left = clamp(
            0, int(server.boy.x) - self.canvas_width // 2, self.w - self.canvas_width - 1)
        self.window_bottom = clamp(
            0, int(server.boy.y) - self.canvas_height // 2, self.h - self.canvas_height - 1)

    def handle_event(self, event):
        pass
