from pico2d import *
import random
import game_framework
import play_state
import map_state
import level_state

image = None

def enter():
    global image
    image = load_image('title_state.png')

def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_SPACE:
                    play_state.game_level = random.randint(0, 2)
                    game_framework.change_state(play_state)
                case pico2d.SDLK_m:
                    game_framework.change_state(map_state)

def draw():
    clear_canvas()
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
