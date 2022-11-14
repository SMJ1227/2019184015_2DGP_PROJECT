from pico2d import *
import play_state

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

class IDLE:
    def enter(self, event):
        self.dirrl = 0
        self.dirud = 0

    def exit(self):
        pass

    def do(self):
        self.upframe = (self.upframe + 1) % 8

    def draw(self):
        self.image.clip_draw(self.upframe * 100, 100 * self.rl, 100, 100, self.character_x, self.character_y)

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
        self.upframe = (self.upframe + 1) % 8
        self.downframe = (self.downframe - 1) % 8
        self.character_x += self.dirrl * 1
        self.character_y += self.dirud * 1
        self.character_x = clamp(0, self.character_x, 1280)
        self.character_y = clamp(0, self.character_y, 1024)

    def draw(self):
        if self.dirrl == 0 and self.dirud == 0:
            self.image.clip_draw(self.upframe * 100, 100 * self.rl, 100, 100, self.character_x, self.character_y)
        if self.dirrl == 1:
            self.image.clip_draw(self.upframe * 100, 100 * 1, 100, 100, self.character_x, self.character_y)
        elif self.dirrl == -1:
            self.image.clip_draw(self.downframe * 100, 100 * 0, 100, 100, self.character_x, self.character_y)
        elif self.dirud == 1:
            self.image.clip_draw(self.upframe * 100, 100 * (self.rl-2), 100, 100, self.character_x, self.character_y)
        elif self.dirud == -1:
            self.image.clip_draw(self.downframe * 100, 100 * (self.rl-2), 100, 100, self.character_x, self.character_y)

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
        self.upframe = (self.upframe + 1) % 8
        self.downframe = (self.downframe - 1) % 8
        self.character_x += self.dirrl * 1
        self.character_y += self.dirud * 1
        self.character_x = clamp(0, self.character_x, 1280)
        self.character_y = clamp(0, self.character_y, 1024)

    def draw(self):
        if self.dirrl == 0 and self.dirud == 0:
            self.image.clip_draw(self.upframe * 100, 100 * self.rl, 100, 100, self.character_x, self.character_y)
        if self.dirrl == 1:
            self.image.clip_draw(self.upframe * 100, 100 * 1, 100, 100, self.character_x, self.character_y)
        elif self.dirrl == -1:
            self.image.clip_draw(self.downframe * 100, 100 * 0, 100, 100, self.character_x, self.character_y)
        elif self.dirud == 1:
            self.image.clip_draw(self.upframe * 100, 100 * (self.rl-2), 100, 100, self.character_x, self.character_y)
        elif self.dirud == -1:
            self.image.clip_draw(self.downframe * 100, 100 * (self.rl-2), 100, 100, self.character_x, self.character_y)

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
        self.upframe = (self.upframe + 1) % 8
        self.downframe = (self.downframe - 1) % 8
        self.character_x += self.dirrl * 1
        self.character_y += self.dirud * 1
        self.character_x = clamp(0, self.character_x, 1280)
        self.character_y = clamp(0, self.character_y, 1024)

    def draw(self):
        if self.dirrl == 0 and self.dirud == 0:
            self.image.clip_draw(self.upframe * 100, 100 * self.rl, 100, 100, self.character_x, self.character_y)
        if self.dirrl == 1:
            self.image.clip_draw(self.upframe * 100, 100 * 1, 100, 100, self.character_x, self.character_y)
        elif self.dirrl == -1:
            self.image.clip_draw(self.downframe * 100, 100 * 0, 100, 100, self.character_x, self.character_y)
        elif self.dirud == 1:
            self.image.clip_draw(self.upframe * 100, 100 * (self.rl-2), 100, 100, self.character_x, self.character_y)
        elif self.dirud == -1:
            self.image.clip_draw(self.downframe * 100, 100 * (self.rl-2), 100, 100, self.character_x, self.character_y)

class QRUN:
    def enter(self, event):
        self.dirrl = 0
        self.dirud = 0

    def exit(self):
        pass

    def do(self):
        self.upframe = (self.upframe + 1) % 8

    def draw(self):
        self.image.clip_draw(self.upframe * 100, 100 * self.rl, 100, 100, self.character_x, self.character_y)

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
        self.character_x = play_state.TUK_GROUND_FULL_WIDTH // 2
        self.character_y = play_state.TUK_GROUND_FULL_HEIGHT // 2
        self.upframe = 0
        self.downframe = 0
        self.dirrl = 0
        self.dirud = 0
        self. rl = 3
        self.image = load_image('animation_sheet.png')
        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
