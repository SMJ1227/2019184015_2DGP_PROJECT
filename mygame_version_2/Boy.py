from pico2d import *
import time
import game_framework
import server
import gameover_state
from Map import *

class Shield:
    shield_sound = None

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        self.image = load_image('shield.png')
        if Shield.shield_sound is None:
            Shield.shield_sound = load_wav('Shield_sound.wav')
            Shield.shield_sound.set_volume(20)

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, 100, 100)

class Hp:
    def __init__(self):
        self.image = load_image('heart.png')

    def update(self):
        pass

    def draw(self):
        for i in range(server.boy.heart):
            self.image.draw(50 + (i * 30), 950)

RD, LD, UD, DD, RU, LU, UU, DU = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RD,
    (SDL_KEYDOWN, SDLK_a): LD,
    (SDL_KEYDOWN, SDLK_w): UD,
    (SDL_KEYDOWN, SDLK_s): DD,
    (SDL_KEYUP, SDLK_d): RU,
    (SDL_KEYUP, SDLK_a): LU,
    (SDL_KEYUP, SDLK_w): UU,
    (SDL_KEYUP, SDLK_s): DU,
}

# 이속
PIXEL_PER_METER = (10.0 / 0.25) # 10pixel 25cm / 키185cm
RUN_SPEED_KMPH = 30.0 # Km/Hour
if Map.image_number == 0:
    pass
elif Map.image_number == 1 or 2:
    RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class IDLE:
    def enter(boy, event):
        boy.dirrl = 0
        boy.dirud = 0

    def exit(boy):
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(boy):
        sx, sy = boy.x - server.world.window_left, boy.y - server.world.window_bottom
        boy.image.clip_draw(int(boy.frame) * 100, 100 * boy.rl, 100, 100, sx, sy)

class RUN:
    def enter(boy, event):
        if event == RD:
            boy.dirrl += 1
            if boy.rl == 2:
                boy.rl += 1
        elif event == LD:
            boy.dirrl -= 1
            if boy.rl == 3:
                boy.rl -= 1
        elif event == UD:
            boy.dirud += 1
        elif event == DD:
            boy.dirud -= 1
        elif event == RU:
            boy.dirrl -= 1
        elif event == LU:
            boy.dirrl += 1
        elif event == UU:
            boy.dirud -= 1
        elif event == DU:
            boy.dirud += 1

    def exit(boy):
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        boy.x += boy.dirrl * RUN_SPEED_PPS * game_framework.frame_time
        boy.y += boy.dirud * RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(100, boy.x, server.world.w - 100)
        boy.y = clamp(100, boy.y, server.world.h - 100)

    def draw(boy):
        sx, sy = boy.x - server.world.window_left, boy.y - server.world.window_bottom

        if boy.dirrl == 0 and boy.dirud == 0:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * boy.rl, 100, 100, sx, sy)
        if boy.dirrl == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * 1, 100, 100, sx, sy)
        elif boy.dirrl == -1:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * 0, 100, 100, sx, sy)
        elif boy.dirud == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * (boy.rl-2), 100, 100, sx, sy)
        elif boy.dirud == -1:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * (boy.rl-2), 100, 100, sx, sy)

class DRUN:
    def enter(boy, event):
        if event == RD:
            boy.dirrl += 1
            if boy.rl == 2:
                boy.rl += 1
        elif event == LD:
            boy.dirrl -= 1
            if boy.rl == 3:
                boy.rl -= 1
        elif event == UD:
            boy.dirud += 1
        elif event == DD:
            boy.dirud -= 1
        elif event == RU:
            boy.dirrl -= 1
        elif event == LU:
            boy.dirrl += 1
        elif event == UU:
            boy.dirud -= 1
        elif event == DU:
            boy.dirud += 1

    def exit(boy):
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        boy.x += boy.dirrl * RUN_SPEED_PPS * game_framework.frame_time
        boy.y += boy.dirud * RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(100, boy.x, server.world.w - 100)
        boy.y = clamp(100, boy.y, server.world.h - 100)

    def draw(boy):
        sx, sy = boy.x - server.world.window_left, boy.y - server.world.window_bottom

        if boy.dirrl == 0 and boy.dirud == 0:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * boy.rl, 100, 100, sx, sy)
        if boy.dirrl == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * 1, 100, 100, sx, sy)
        elif boy.dirrl == -1:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * 0, 100, 100, sx, sy)
        elif boy.dirud == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * (boy.rl-2), 100, 100, sx, sy)
        elif boy.dirud == -1:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * (boy.rl-2), 100, 100, sx, sy)

class TRUN:
    def enter(boy, event):
        if event == RD:
            boy.dirrl += 1
            if boy.rl == 2:
                boy.rl += 1
        elif event == LD:
            boy.dirrl -= 1
            if boy.rl == 3:
                boy.rl -= 1
        elif event == UD:
            boy.dirud += 1
        elif event == DD:
            boy.dirud -= 1
        elif event == RU:
            boy.dirrl -= 1
        elif event == LU:
            boy.dirrl += 1
        elif event == UU:
            boy.dirud -= 1
        elif event == DU:
            boy.dirud += 1

    def exit(boy):
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        boy.x += boy.dirrl * RUN_SPEED_PPS * game_framework.frame_time
        boy.y += boy.dirud * RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(100, boy.x, server.world.w - 100)
        boy.y = clamp(100, boy.y, server.world.h - 100)

    def draw(boy):
        sx, sy = boy.x - server.world.window_left, boy.y - server.world.window_bottom

        if boy.dirrl == 0 and boy.dirud == 0:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * boy.rl, 100, 100, sx, sy)
        if boy.dirrl == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * 1, 100, 100, sx, sy)
        elif boy.dirrl == -1:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * 0, 100, 100, sx, sy)
        elif boy.dirud == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * (boy.rl - 2), 100, 100, sx, sy)
        elif boy.dirud == -1:
            boy.image.clip_draw(int(boy.frame) * 100, 100 * (boy.rl - 2), 100, 100, sx, sy)

class QRUN:
    def enter(boy, event):
        boy.dirrl = 0
        boy.dirud = 0

    def exit(boy):
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(boy):
        sx, sy = boy.x - server.world.window_left, boy.y - server.world.window_bottom

        boy.image.clip_draw(int(boy.frame) * 100, 100 * boy.rl, 100, 100, sx, sy)

next_state = {
    IDLE : {RU: IDLE, LU: IDLE, UU: IDLE, DU: IDLE, RD: RUN, LD: RUN, UD: RUN, DD: RUN},
    RUN : {RU: IDLE, LU: IDLE, UU: IDLE, DU: IDLE, RD: DRUN, LD: DRUN, UD: DRUN, DD: DRUN},
    DRUN : {RU: RUN, LU: RUN, UU: RUN, DU: RUN, RD: TRUN, LD: TRUN, UD: TRUN, DD: TRUN},
    TRUN : {RU: DRUN, LU: DRUN, UU: DRUN, DU: DRUN, RD: QRUN, LD: QRUN, UD: QRUN, DD: QRUN},
    QRUN : {RU: TRUN, LU: TRUN, UU: TRUN, DU: TRUN, RD: IDLE, LD: IDLE, UD: IDLE, DD: IDLE}
}

class Boy:
    hit = False
    close_sound = None

    def __init__(self):
        self.image = load_image('animation_sheet.png')
        self.x, self.y = server.world.w // 2, server.world.h // 2
        #self.x, self.y = get_canvas_width() // 2, get_canvas_height() // 2
        self.frame = 0
        self.dirrl = 0
        self.dirud = 0
        self. rl = 3
        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        self.font = load_font('ENCR10B.TTF', 16)
        self.hit_start = 0
        self.time = time.time()
        self.time_long = time.time()
        self.shield = Shield(self.x, self.y)
        self.hp = Hp()
        self.heart = 5
        self.remaining = 100
        if Boy.close_sound is None:
            Boy.close_sound = load_wav('close_sound.wav')
            Boy.close_sound.set_volume(20)

    def update(self):
        self.sx, self.sy = self.x - server.world.window_left, self.y - server.world.window_bottom
        self.shield = Shield(self.sx, self.sy)
        self.time = time.time()
        if self.time - self.hit_start >= 1:
            Boy.hit = False
        self.cur_state.do(self)
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        if Boy.hit:
            self.shield.draw()
        self.font.draw(600, 1000, f'(Time: {self.time - self.time_long:.2f})', (0, 0, 0))
        self.hp.draw()

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_events(self, event):
        global RUN_SPEED_KMPH
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.q.insert(0, key_event)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if Map.image_number == 0:
                RUN_SPEED_KMPH = 40.0
            elif Map.image_number == 1 or 2:
                RUN_SPEED_KMPH = 30.0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
            if Map.image_number == 0:
                RUN_SPEED_KMPH = 30.0
            elif Map.image_number == 1 or 2:
                RUN_SPEED_KMPH = 20.0

    def get_bb(self):
        return self.sx-10, self.sy-35,  self.sx+15, self.sy+40

    def handle_collision(self, other, group):
        if group == 'character:monster':
            if self.heart == 1 and Boy.hit is not True:
                self.heart -= 1
                self.hp.draw()
                Boy.close_sound.play()
                game_framework.push_state(gameover_state)
            else:
                if Boy.hit is not True:
                    self.hit_start = time.time()
                    Boy.hit = True
                    Shield.shield_sound.play()
                    self.heart -= 1
                elif Boy.hit:
                    pass
        elif group == 'character:cactus':
            if self.heart == 1 and Boy.hit is not True:
                self.heart -= 1
                self.hp.draw()
                Boy.close_sound.play()
                game_framework.push_state(gameover_state)
            else:
                if Boy.hit is not True:
                    self.hit_start = time.time()
                    Boy.hit = True
                    Shield.shield_sound.play()
                elif Boy.hit:
                    pass

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2
