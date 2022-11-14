from pico2d import *
from Map import *
from Monster import *
from Bullet import *
from Target import *
from Boy import *

import game_framework
import game_world
import pause_state

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(pause_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            bullet.reloading()
        elif event.type == SDL_MOUSEMOTION:
            target.mouse_x, target.mouse_y = event.x, TUK_GROUND_FULL_HEIGHT-1-event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            bullet.bullets -= 1
        else:
            character.handle_events(event)

TUK_GROUND_FULL_WIDTH = 1280
TUK_GROUND_FULL_HEIGHT = 1024

map = None
character = None
monsters = []
target = None
bullet = None

def enter():
    global map, character, monsters, target, bullet
    map = Map()
    game_world.add_object(map, 0)

    character = Boy()
    game_world.add_object(character, 1)

    monsters = Monster()#[Monster() for i in range(10)]
    game_world.add_object(monsters, 1)

    target = Target()
    game_world.add_object(target, 2)

    bullet = Bullet()
    game_world.add_object(bullet, 2)

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass
