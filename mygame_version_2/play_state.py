import Map
from Bullet import *
from Target import *
from Boy import *
from Cactus import *
from Map import *

import random
import game_framework
import game_world
import pause_state
import level_state
import server
import json

game_level = None
open_sound = None

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

def enter():
    global open_sound
    open_sound = load_music('Open_sound.mp3')
    open_sound.set_volume(32)
    open_sound.play(1)

    server.world = Map()
    game_world.add_object(server.world, 0)

    server.boy = Boy()
    game_world.add_object(server.boy, 1)

    if game_level == 0:
        server.monsters = [Monster() for i in range(20)]
        game_world.add_objects(server.monsters, 1)
    elif game_level == 1:
        server.monsters = [Monster() for i in range(50)]
        game_world.add_objects(server.monsters, 1)
    elif game_level == 2:
        server.monsters = [Monster() for i in range(100)]
        game_world.add_objects(server.monsters, 1)

    server.target = Target()
    game_world.add_object(server.target, 2)

    server.bullet = Bullet()
    game_world.add_object(server.bullet, 2)

    if Map.image_number == 2:
        with open('cactus.json', 'r') as f:
            cactus_data_list = json.load(f)
            for data in cactus_data_list:
                cactus = Cactus(data['type'], data['number'], data['x'], data['y'])
                game_world.add_object(cactus, 1)
                game_world.add_collision_pairs(server.boy, cactus, 'character:cactus')
    else:
        pass

    game_world.add_collision_pairs(server.boy, server.monsters, 'character:monster')
    game_world.add_collision_pairs(server.target, server.monsters, 'target:monster')

def exit():
    global open_sound
    del open_sound
    game_world.clear()
    server.monsters = None

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            #print('COLLISON ', group)
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
