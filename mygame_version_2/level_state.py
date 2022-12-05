from pico2d import *
from Map import *
import game_framework
import play_state
import map_state

image = None
open_sound = None

def enter():
    global image, open_sound
    image = load_image('level_state.png')
    open_sound = load_music('Open_sound.mp3')
    open_sound.set_volume(32)
    open_sound.play(1)

def exit():
    global image, open_sound
    del image, open_sound

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.change_state(map_state)
                case pico2d.SDLK_1:
                    play_state.game_level = 0
                    game_framework.change_state(play_state)
                case pico2d.SDLK_2:
                    play_state.game_level = 1
                    game_framework.change_state(play_state)
                case pico2d.SDLK_3:
                    play_state.game_level = 2
                    game_framework.change_state(play_state)

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
