from pico2d import *
import game_framework
import title_state

image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('tuk_credit.png')

def exit():
    global image
    del image
    pass

def update():
    global logo_time
    delay(0.01)
    logo_time += 0.01
    if logo_time >= 0.5:
        logo_time = 0
        game_framework.change_state(title_state)

def draw():
    clear_canvas()
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()

def handle_events():
    pass
