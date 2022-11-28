from pico2d import *
from Map import *
from Monster import *
from Bullet import *
from Target import *
from Character import *

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
            monster.handle_event(event)
            target.handle_event(event)
            bullet.handle_event(event)
            character.handle_events(event)

TUK_GROUND_FULL_WIDTH = 1280
TUK_GROUND_FULL_HEIGHT = 1024

world = None
character = None
monster = None
#monsters = []
target = None
bullet = None

def enter():
    global world, character, target, bullet, monsters, monster
    world = Map()
    game_world.add_object(world, 0)

    character = Boy()
    game_world.add_object(character, 1)

    monster = Monster()
    #monsters = [Monster()]
    monsters = [Monster() for i in range(10)]
    game_world.add_objects(monsters, 1)

    target = Target()
    game_world.add_object(target, 2)

    bullet = Bullet()
    game_world.add_object(bullet, 2)

    game_world.add_collision_pairs(character, monsters, 'character:monster')
    game_world.add_collision_pairs(target, monsters, 'target:monster')

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
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def pause():
    pass

def resume():
    pass
