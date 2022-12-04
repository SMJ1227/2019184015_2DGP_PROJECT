from pico2d import *
from BehaviorTree import BehaviorTree, Selector, Sequence, Leaf
from boy import *

import math
import random
import game_framework
import game_world
import server
import clear_state

class RandomLocation:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def update(self):
        pass

    def draw(self):
        pass

# monster Run Speed
PIXEL_PER_METER = (10.0 / 0.25)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# mopnster Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

Monster_type = ['monster.png', 'monster_horse.png']

class Monster:
    remaining = 100

    def __init__(self):
        self.monster_type_number = random.randint(0, 1)
        if self.monster_type_number == 0:
            self.image = load_image(Monster_type[self.monster_type_number])
        elif self.monster_type_number == 1:
            self.image = load_image(Monster_type[self.monster_type_number])

        self.x = random.randint(100, server.world.w-100)
        self.y = random.randint(100, server.world.h-100)
        self.tx = random.randint(100, server.world.w-100)
        self.ty = random.randint(100, server.world.h-100)
        self.random_location = RandomLocation(self.tx, self.ty)
        self.dir = random.random() * 2 * math.pi  # random moving direction
        self.speed = 0
        self.frame = 0.0
        self.build_behavior_tree()
        self.font = load_font('ENCR10B.TTF', 16)

    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(100, self.x, server.world.w-100)
        self.y = clamp(100, self.y, server.world.h-100)

    def calculate_squared_distance(self, a, b):
        return (a.x-b.x)**2 + (a.y-b.y)**2

    def move_to_boy(self):
        distance = self.calculate_squared_distance(self, server.boy)

        if distance > (PIXEL_PER_METER * 100) ** 2:
            self.speed = 0
            return BehaviorTree.FAIL
        self.dir = math.atan2(server.boy.y - self.y, server.boy.x - self.x)
        if distance < (PIXEL_PER_METER * 0.5) ** 2:
            self.speed = 0
            return BehaviorTree.SUCCESS
        else:
            self.speed = RUN_SPEED_PPS
            return BehaviorTree.RUNNING

    def find_random_location(self):
        self.tx, self.ty = random.randint(100, server.world.w-100), random.randint(100, server.world.h-100)
        self.random_location.x, self.random_location.y = self.tx, self.ty
        return BehaviorTree.SUCCESS

    def move_to(self, radius = 0.5):
        distance = (self.tx - self.x) ** 2 + (self.ty - self.y) ** 2
        self.dir = math.atan2(self.ty - self.y, self.tx - self.x)
        if distance < (PIXEL_PER_METER * radius) ** 2:
            self.speed = 0
            return BehaviorTree.SUCCESS
        else:
            self.speed = RUN_SPEED_PPS * 2
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
        self.font.draw(595, 975, f'(Monsters: %d)' % (server.boy.remaining), (500, 0, 0))
        self.sx, self.sy = self.x - server.world.window_left, self.y - server.world.window_bottom
        if self.monster_type_number == 0:
            if math.cos(self.dir) < 0:
                self.image.composite_draw(0, 'h', self.sx, self.sy)
            else:
                self.image.draw(self.sx, self.sy)

        elif self.monster_type_number == 1:
            if math.cos(self.dir) < 0:
                self.image.clip_draw(int(self.frame) * 100, 100 * 0, 100, 100, self.sx, self.sy)
            else:
                self.image.clip_composite_draw(int(self.frame) * 100, 100 * 0, 100, 100, 0, 'h', self.sx, self.sy, 100, 100)

    def handle_event(self, event):
        pass

    def get_bb(self):
        self.sx, self.sy = self.x - server.world.window_left, self.y - server.world.window_bottom
        if self.monster_type_number == 0:
            return self.sx-30, self.sy-25, self.sx+30, self.sy+25
        elif self.monster_type_number == 1:
            return self.sx - 40, self.sy - 25, self.sx + 40, self.sy + 25

    def handle_collision(self, other, group):
        if group == 'character:monster' and Boy.hit:
            game_world.remove_object(self)
            server.boy.remaining -= 1
            if server.boy.remaining == 0:
                game_framework.push_state(clear_state)

        if group == 'target:monster':
            game_world.remove_object(self)
            server.boy.remaining -= 1
            if server.boy.remaining == 0:
                game_framework.push_state(clear_state)
