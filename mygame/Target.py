from pico2d import *
import play_state
import game_world


class Target:
    def __init__(self):
        self.image = load_image('target.png')
        self.x = play_state.TUK_GROUND_FULL_WIDTH // 2
        self.y = play_state.TUK_GROUND_FULL_HEIGHT // 2

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, play_state.TUK_GROUND_FULL_HEIGHT - 1 - event.y

    def get_bb(self):
        return self.x-1, self.y-1, self.x+1, self.y+1

    def handle_collision(self, other, group):
        pass
