from pico2d import *
from Boy import *
import game_framework
import game_world
import play_state
import title_state
import map_state

image = None

def enter():
    global image
    image = load_image('clear_state_fixing.png')

def exit():
    global image
    del image

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_q:
                    game_framework.quit()
                case pico2d.SDLK_m:
                    pass
                    #game_world.clear()
                    #game_framework.change_state(map_state)
