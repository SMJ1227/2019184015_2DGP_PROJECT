from pico2d import *
from Map import *
import game_framework
import play_state
import title_state

image = None

def enter():
    global image
    image = load_image('map_state.png')

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
                    game_framework.change_state(title_state)
                case pico2d.SDLK_1:
                    Map.image_number = 0
                    game_framework.change_state(play_state)
                case pico2d.SDLK_2:
                    Map.image_number = 1
                    game_framework.change_state(play_state)
                case pico2d.SDLK_3:
                    Map.image_number = 2
                    game_framework.change_state(play_state)

def draw():
    clear_canvas()
    image.draw(play_state.TUK_GROUND_FULL_WIDTH // 2, play_state.TUK_GROUND_FULL_HEIGHT // 2)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
