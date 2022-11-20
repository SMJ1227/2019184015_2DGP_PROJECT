from pico2d import *
from Shot import *
import play_state
import game_world


class Target:
    def __init__(self):
        self.image = load_image('target.png')
        self.mouse_x = play_state.TUK_GROUND_FULL_WIDTH // 2
        self.mouse_y = play_state.TUK_GROUND_FULL_HEIGHT // 2

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.mouse_x, self.mouse_y)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.mouse_x, self.mouse_y = event.x, play_state.TUK_GROUND_FULL_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            shot = Shot(self.mouse_x, self.mouse_y)
            game_world.add_collision_pairs(shot, play_state.monsters, 'shot:monster')
            game_world.add_object(shot, 1)

    def get_bb(self):
        return self.mouse_x-1, self.mouse_y-1, self.mouse_x+1, self.mouse_y+1

    def handle_collision(self, other, group):
        pass
