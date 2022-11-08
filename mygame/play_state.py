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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(pause_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            bullet.reloading()
        elif event.type == SDL_MOUSEMOTION:
            target.mouse_x, target.mouse_y = event.x, TUK_GROUND_FULL_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            bullet.bullets -= 1
        else:
            character.handle_events(event)

TUK_GROUND_FULL_WIDTH = 1280
TUK_GROUND_FULL_HEIGHT = 1024

tuk_ground = None
character = None
monster = None
target = None
bullet = None

def enter():
    global tuk_ground, character, monster, target, bullet
    tuk_ground = Map()
    character = Boy()
    monster = Monster()
    target = Target()
    bullet = Bullet()

def exit():
    global tuk_ground, character, monster, target, bullet
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
