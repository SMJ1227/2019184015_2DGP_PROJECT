from pico2d import *
from Map import *
from Monster import *
from Bullet import *
from Target import *
from Boy import *
import game_framework
import pause_state

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_d or event.key == SDLK_RIGHT:
                character.dirrl += 1
            elif event.key == SDLK_a or event.key == SDLK_LEFT:
                character.dirrl -= 1
            elif event.key == SDLK_w or event.key == SDLK_UP:
                character.dirud += 1
            elif event.key == SDLK_s or event.key == SDLK_DOWN:
                character.dirud -= 1
            elif event.key == SDLK_ESCAPE:
                game_framework.push_state(pause_state)
            elif event.key == SDLK_r:
                bullet.reloading()

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d or event.key == SDLK_RIGHT:
                character.dirrl -= 1
            elif event.key == SDLK_a or event.key == SDLK_LEFT:
                character.dirrl += 1
            elif event.key == SDLK_w or event.key == SDLK_UP:
                character.dirud -= 1
            elif event.key == SDLK_s or event.key == SDLK_DOWN:
                character.dirud += 1
        elif event.type == SDL_MOUSEMOTION:
            target.mouse_x, target.mouse_y = event.x, TUK_GROUND_FULL_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            bullet.bullets -= 1

    delay(0.01)


TUK_GROUND_FULL_WIDTH = 1280
TUK_GROUND_FULL_HEIGHT = 1024

running = True
tuk_ground = None
character = None
monster = None
target = None
bullet = None

def enter():
    global running
    global tuk_ground, character, monster, target, bullet
    running = True
    tuk_ground = Map()
    character = Boy()
    monster = Monster()
    target = Target()
    bullet = Bullet()

def exit():
    global running
    global tuk_ground, character, monster, target, bullet
    del running
    del tuk_ground
    del character
    del monster
    del target
    del bullet

def update():
    character.update()
    monster.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    tuk_ground.draw()
    bullet.draw()
    character.draw()
    monster.draw()
    target.draw()

def pause():
    pass

def resume():
    pass
