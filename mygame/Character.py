from pico2d import *
import play_state
import game_framework
import game_world

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
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class IDLE:
    def enter(self, event):
        self.dirrl = 0
        self.dirud = 0

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 100 * self.rl, 100, 100, self.x, self.y)

class RUN:
    def enter(self, event):
        if event == RD:
            self.dirrl += 1
            if self.rl == 2:
                self.rl += 1
        elif event == LD:
            self.dirrl -= 1
            if self.rl == 3:
                self.rl -= 1
        elif event == UD:
            self.dirud += 1
        elif event == DD:
            self.dirud -= 1
        elif event == RU:
            self.dirrl -= 1
        elif event == LU:
            self.dirrl += 1
        elif event == UU:
            self.dirud -= 1
        elif event == DU:
            self.dirud += 1

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.dirrl * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dirud * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1280)
        self.y = clamp(0, self.y, 1024)

    def draw(self):
        if self.dirrl == 0 and self.dirud == 0:
            self.image.clip_draw(int(self.frame) * 100, 100 * self.rl, 100, 100, self.x, self.y)
        if self.dirrl == 1:
            self.image.clip_draw(int(self.frame) * 100, 100 * 1, 100, 100, self.x, self.y)
        elif self.dirrl == -1:
            self.image.clip_draw(int(self.frame) * 100, 100 * 0, 100, 100, self.x, self.y)
        elif self.dirud == 1:
            self.image.clip_draw(int(self.frame) * 100, 100 * (self.rl-2), 100, 100, self.x, self.y)
        elif self.dirud == -1:
            self.image.clip_draw(int(self.frame) * 100, 100 * (self.rl-2), 100, 100, self.x, self.y)

class DRUN:
    def enter(self, event):
        if event == RD:
            self.dirrl += 1
            if self.rl == 2:
                self.rl += 1
        elif event == LD:
            self.dirrl -= 1
            if self.rl == 3:
                self.rl -= 1
        elif event == UD:
            self.dirud += 1
        elif event == DD:
            self.dirud -= 1
        elif event == RU:
            self.dirrl -= 1
        elif event == LU:
            self.dirrl += 1
        elif event == UU:
            self.dirud -= 1
        elif event == DU:
            self.dirud += 1

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.dirrl * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dirud * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1280)
        self.y = clamp(0, self.y, 1024)

    def draw(self):
        if self.dirrl == 0 and self.dirud == 0:
            self.image.clip_draw(int(self.frame) * 100, 100 * self.rl, 100, 100, self.x, self.y)
        if self.dirrl == 1:
            self.image.clip_draw(int(self.frame) * 100, 100 * 1, 100, 100, self.x, self.y)
        elif self.dirrl == -1:
            self.image.clip_draw(int(self.frame) * 100, 100 * 0, 100, 100, self.x, self.y)
        elif self.dirud == 1:
            self.image.clip_draw(int(self.frame) * 100, 100 * (self.rl-2), 100, 100, self.x, self.y)
        elif self.dirud == -1:
            self.image.clip_draw(int(self.frame) * 100, 100 * (self.rl-2), 100, 100, self.x, self.y)

class TRUN:
    def enter(self, event):
        if event == RD:
            self.dirrl += 1
            if self.rl == 2:
                self.rl += 1
        elif event == LD:
            self.dirrl -= 1
            if self.rl == 3:
                self.rl -= 1
        elif event == UD:
            self.dirud += 1
        elif event == DD:
            self.dirud -= 1
        elif event == RU:
            self.dirrl -= 1
        elif event == LU:
            self.dirrl += 1
        elif event == UU:
            self.dirud -= 1
        elif event == DU:
            self.dirud += 1

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.dirrl * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dirud * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1280)
        self.y = clamp(0, self.y, 1024)

    def draw(self):
        if self.dirrl == 0 and self.dirud == 0:
            self.image.clip_draw(int(self.frame) * 100, 100 * self.rl, 100, 100, self.x, self.y)
        if self.dirrl == 1:
            self.image.clip_draw(int(self.frame) * 100, 100 * 1, 100, 100, self.x, self.y)
        elif self.dirrl == -1:
            self.image.clip_draw(int(self.frame) * 100, 100 * 0, 100, 100, self.x, self.y)
        elif self.dirud == 1:
            self.image.clip_draw(int(self.frame) * 100, 100 * (self.rl-2), 100, 100, self.x, self.y)
        elif self.dirud == -1:
            self.image.clip_draw(int(self.frame) * 100, 100 * (self.rl-2), 100, 100, self.x, self.y)

class QRUN:
    def enter(self, event):
        self.dirrl = 0
        self.dirud = 0

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 100 * self.rl, 100, 100, self.x, self.y)

next_state = {
    IDLE : {RU: IDLE, LU: IDLE, UU: IDLE, DU: IDLE, RD: RUN, LD: RUN, UD: RUN, DD: RUN},
    RUN : {RU: IDLE, LU: IDLE, UU: IDLE, DU: IDLE, RD: DRUN, LD: DRUN, UD: DRUN, DD: DRUN},
    DRUN : {RU: RUN, LU: RUN, UU: RUN, DU: RUN, RD: TRUN, LD: TRUN, UD: TRUN, DD: TRUN},
    TRUN : {RU: DRUN, LU: DRUN, UU: DRUN, DU: DRUN, RD: QRUN, LD: QRUN, UD: QRUN, DD: QRUN},
    QRUN : {RU: TRUN, LU: TRUN, UU: TRUN, DU: TRUN, RD: IDLE, LD: IDLE, UD: IDLE, DD: IDLE}
}

class Boy:
    def add_event(self, event):
        self.q.insert(0, event)

    def handle_events(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.q.insert(0, key_event)

    def __init__(self):
        self.x = play_state.TUK_GROUND_FULL_WIDTH // 2
        self.y = play_state.TUK_GROUND_FULL_HEIGHT // 2
        self.frame = 0
        self.dirrl = 0
        self.dirud = 0
        self. rl = 3
        self.image = load_image('animation_sheet.png')
        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        self.cur_state.do(self)
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(600, 1000, f'(Time: {get_time():.2f})', (0, 0, 0))
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-10, self.y-35, self.x+15, self.y+40

    def handle_collision(self, other, group):
        if group == 'character:monster':
            pass#game_framework.quit()
        #     game_world.remove_object(self)
