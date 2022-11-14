from pico2d import *
import play_state

class Target:
    def __init__(self):
        self.image = load_image('target.png')
        self.mouse_x = play_state.TUK_GROUND_FULL_WIDTH // 2
        self.mouse_y = play_state.TUK_GROUND_FULL_HEIGHT // 2

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.mouse_x, self.mouse_y)
