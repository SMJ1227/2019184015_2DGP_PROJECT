from pico2d import *
from BehaviorTree import BehaviorTree, Selector, Sequence, Leaf
from Character import *

import math
import random
import play_state
import game_framework
import game_world

class RandomLocation:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def update(self):
        pass

    def draw(self):
        pass

# monster Run Speed
PIXEL_PER_METER = (10.0 / 0.25)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# mopnster Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

Monster_type = ['monster.png', 'monster_horse.png']

class Monster:

    def __init__(self):
        self.monster_type_number = random.randint(0, 1)
        if self.monster_type_number == 0:
            self.image = load_image(Monster_type[self.monster_type_number])
        elif self.monster_type_number == 1:
            self.image = load_image(Monster_type[self.monster_type_number])

        self.x = random.randint(0, play_state.TUK_GROUND_FULL_WIDTH)
        self.y = random.randint(0, play_state.TUK_GROUND_FULL_HEIGHT)
        self.tx = random.randint(0, play_state.TUK_GROUND_FULL_WIDTH)
        self.ty = random.randint(0, play_state.TUK_GROUND_FULL_HEIGHT)
        self.random_location = RandomLocation(self.tx, self.ty)
        self.dir = random.random() * 2 * math.pi  # random moving direction
        self.speed = 0
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.frame = 0.0
        self.build_behavior_tree()

    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

    def calculate_squared_distance(self, a, b):
        return (a.x-b.x)**2 + (a.y-b.y)**2

    def move_to_boy(self):
        distance = self.calculate_squared_distance(self, play_state.character)

        if distance > (PIXEL_PER_METER * 100) ** 2:
            self.speed = 0
            return BehaviorTree.FAIL
        self.dir = math.atan2(play_state.character.y - self.y, play_state.character.x - self.x)
        if distance < (PIXEL_PER_METER * 0.5) ** 2:
            self.speed = 0
            return BehaviorTree.SUCCESS
        else:
            self.speed = RUN_SPEED_PPS
            return BehaviorTree.RUNNING

    def find_random_location(self):
        self.tx, self.ty = random.randint(50, 1230), random.randint(50, 974)
        self.random_location.x, self.random_location.y = self.tx, self.ty
        return BehaviorTree.SUCCESS

    def move_to(self, radius = 0.5):
        distance = (self.tx - self.x) ** 2 + (self.ty - self.y) ** 2
        self.dir = math.atan2(self.ty - self.y, self.tx - self.x)
        if distance < (PIXEL_PER_METER * radius) ** 2:
            self.speed = 0
            return BehaviorTree.SUCCESS
        else:
            self.speed = RUN_SPEED_PPS * 3
            return BehaviorTree.RUNNING

    def build_behavior_tree(self):
        move_to_boy_node = Leaf('Move to Boy', self.move_to_boy)
        find_random_location_node = Leaf('Find Random Location', self.find_random_location)
        move_to_node = Leaf('Move To', self.move_to)
        wander_sequence = Sequence('Wander', find_random_location_node, move_to_node)
        if self.monster_type_number == 0:
            self.bt = BehaviorTree(move_to_boy_node)
        elif self.monster_type_number == 1:
            self.bt = BehaviorTree(wander_sequence)

    def update(self):
        self.bt.run()
        self.calculate_current_position()

    def draw(self):
        if self.monster_type_number == 0:
            draw_rectangle(*self.get_bb())
            if math.cos(self.dir) < 0:
                self.image.composite_draw(0, 'h', self.x, self.y)
            else:
                self.image.draw(self.x, self.y)

        elif self.monster_type_number == 1:
            draw_rectangle(*self.get_bb())
            if math.cos(self.dir) < 0:
                self.image.clip_draw(int(self.frame) * 100, 100 * 0, 100, 100, self.x, self.y)
            else:
                self.image.clip_composite_draw(int(self.frame) * 100, 100 * 0, 100, 100, 0, 'h', self.x, self.y, 100, 100)

    def handle_event(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN:
            pass
            #for a, b, group in game_world.all_collision_pairs():
            #    if play_state.collide(a, b):
            #        game_world.remove_object(self)

    def get_bb(self):
        if self.monster_type_number == 0:
            return self.x-30, self.y-25, self.x+30, self.y+25
        elif self.monster_type_number == 1:
            return self.x - 40, self.y - 25, self.x + 40, self.y + 25

    def handle_collision(self, other, group):
        pass
        if group == 'target:monster':# and self.a:
            pass
            #game_world.remove_object(self)
        #    self.a = False
