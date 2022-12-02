from pico2d import *
import logo_state
import title_state
import play_state
import game_framework
import map_state

pico2d.open_canvas(1280, 1024)
game_framework.run(logo_state)
pico2d.clear_canvas()
