from pico2d import *
import play_state
import game_world
from Monster import *

class Target:
    click = False

    def __init__(self):
        self.image = load_image('target.png')
        self.x, self.y = get_canvas_width() // 2, get_canvas_height() // 2
        self.click_start = 0
        self.time = time.time()

    def update(self):
        self.time = time.time()
        if server.bullet.bullets < 0:
            Target.click = False
            pass
        if self.time - self.click_start >= 0.1:
            Target.click = False

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, play_state.TUK_GROUND_FULL_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            self.click_start = time.time()
            Target.click = True

    def get_bb(self):
        if Target.click:
            return self.x-1, self.y-1, self.x+1, self.y+1
        else:
            return -500, -500, -500, -500

    def handle_collision(self, other, group):
        pass
