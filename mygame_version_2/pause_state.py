from pico2d import *
from Boy import *
import game_framework
import game_world
import title_state
import play_state

image = None
running = True
open_sound = None

def enter():
    global image, open_sound
    image = load_image('pause_state_fixing.png')
    open_sound = load_music('Open_sound.mp3')
    open_sound.set_volume(32)
    open_sound.play(1)

def exit():
    global image, open_sound
    del image, open_sound

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
                    game_framework.pop_state()
                case pico2d.SDLK_r:
                    game_framework.pop_state()
                case pico2d.SDLK_t:
                    #game_world.clear()
                    #game_framework.change_state(title_state)
                    pass
                case pico2d.SDLK_q:
                    game_framework.quit()
