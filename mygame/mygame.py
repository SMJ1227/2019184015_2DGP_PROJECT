from pico2d import *
import logo_state
import title_state
import play_state
import game_framework
import map_state

hide_cursor()
pico2d.open_canvas(play_state.TUK_GROUND_FULL_WIDTH, play_state.TUK_GROUND_FULL_HEIGHT)
game_framework.run(play_state)
pico2d.clear_canvas()
