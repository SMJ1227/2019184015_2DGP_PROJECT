from pico2d import *
import logo_state
import game_framework

pico2d.open_canvas(1280, 1024)
game_framework.run(logo_state)
pico2d.clear_canvas()
