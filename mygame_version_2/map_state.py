from pico2d import *
from Map import *
import game_framework
import title_state
import level_state

image = None
open_sound = None
def enter():
    global image, open_sound
    image = load_image('map_state.png')
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
                    game_framework.change_state(title_state)
                case pico2d.SDLK_1:
                    Map.image_number = 0
                    game_framework.change_state(level_state)
                case pico2d.SDLK_2:
                    Map.image_number = 1
                    game_framework.change_state(level_state)
                case pico2d.SDLK_3:
                    Map.image_number = 2
                    game_framework.change_state(level_state)

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
