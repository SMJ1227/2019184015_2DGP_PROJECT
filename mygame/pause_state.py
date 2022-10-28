import pico2d
from pico2d import *
import game_framework
import title_state
import play_state

image = None
running = True

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del image

def update():
    pass
    #play_state.update()

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(play_state.TUK_GROUND_FULL_WIDTH // 2, play_state.TUK_GROUND_FULL_HEIGHT // 2)
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
                case pico2d.SDLK_t:
                    game_framework.change_state(title_state)
                case pico2d.SDLK_r:
                    play_state.exit()
                    game_framework.change_state(play_state)
                case pico2d.SDLK_q:
                    game_framework.quit()
                case pico2d.SDLK_d:
                    play_state.character.dirrl += 1
                case pico2d.SDLK_RIGHT:
                    play_state.character.dirrl += 1
                case pico2d.SDLK_a:
                    play_state.character.dirrl -= 1
                case pico2d.SDLK_LEFT:
                    play_state.character.dirrl -= 1
                case pico2d.SDLK_w:
                    play_state.character.dirud += 1
                case pico2d.SDLK_UP:
                    play_state.character.dirud += 1
                case pico2d.SDLK_s:
                    play_state.character.dirud -= 1
                case pico2d.SDLK_DOWN:
                    play_state.character.dirud -= 1

        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_d:
                    play_state.character.dirrl -= 1
                case pico2d.SDLK_RIGHT:
                    play_state.character.dirrl -= 1
                case pico2d.SDLK_a:
                    play_state.character.dirrl += 1
                case pico2d.SDLK_LEFT:
                    play_state.character.dirrl += 1
                case pico2d.SDLK_w:
                    play_state.character.dirud -= 1
                case pico2d.SDLK_UP:
                    play_state.character.dirud -= 1
                case pico2d.SDLK_s:
                    play_state.character.dirud += 1
                case pico2d.SDLK_DOWN:
                    play_state.character.dirud += 1

