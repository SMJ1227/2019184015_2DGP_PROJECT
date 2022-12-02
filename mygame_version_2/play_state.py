from pico2d import *
from Map import *
from Monster import *
from Bullet import *
from Target import *
from boy import *

import game_framework
import game_world
import pause_state
import server

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(pause_state)
        else:
            server.target.handle_event(event)
            server.bullet.handle_event(event)
            server.boy.handle_events(event)

#TUK_GROUND_FULL_WIDTH = 1280
#TUK_GROUND_FULL_HEIGHT = 1024

def enter():
    server.world = Map()
    game_world.add_object(server.world, 0)

    server.boy = Boy()
    game_world.add_object(server.boy, 1)

    server.monsters = [Monster() for i in range(100)]
    game_world.add_objects(server.monsters, 1)

    server.target = Target()
    game_world.add_object(server.target, 2)

    server.bullet = Bullet()
    game_world.add_object(server.bullet, 2)

    game_world.add_collision_pairs(server.boy, server.monsters, 'character:monster')
    game_world.add_collision_pairs(server.target, server.monsters, 'target:monster')

def exit():
    #global world, character, target, bullet, monsters#, monster
    server.boy, server.monsters = None, None
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
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True

def pause():
    pass

def resume():
    pass
