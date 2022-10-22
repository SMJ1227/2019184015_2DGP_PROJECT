from pico2d import *
import game_framework
import title_state
import play_state

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
    image.draw(play_state.TUK_GROUND_FULL_WIDTH // 2, play_state.TUK_GROUND_FULL_HEIGHT // 2)
    update_canvas()

def handle_events():
    events = get_events()
