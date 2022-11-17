from pico2d import *
from Map import *
from Monster import *
from Bullet import *
from Target import *
from Boy import *
from Shot import *

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

        else:
            #monster.handle_event(event)
            target.handle_event(event)
            bullet.handle_event(event)
            character.handle_events(event)

TUK_GROUND_FULL_WIDTH = 1280
TUK_GROUND_FULL_HEIGHT = 1024

monster = None
world = None
character = None
monsters = []
target = None
bullet = None
shot = None

def enter():
    global world, monster, monsters, character, target, bullet, shot
    world = Map()
    game_world.add_object(world, 0)
    character = Boy()
    game_world.add_object(character, 1)
    monster = Monster()
    monsters = [Monster() for i in range(10)]
    game_world.add_objects(monsters, 1)
    target = Target()
    game_world.add_object(target, 2)
    bullet = Bullet()
    game_world.add_object(bullet, 2)

    shot = Shot(0, 0)
    game_world.add_collision_pairs(character, monsters, 'character:monster')
    game_world.add_collision_pairs(shot, monsters, 'shot:monster')

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISON ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb : return False
    if ra < lb : return False
    if ta < bb : return False
    if ba > tb : return False

    return True

def pause():
    pass

def resume():
    pass
