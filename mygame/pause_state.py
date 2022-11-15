from pico2d import *
from Boy import *
import game_framework
import game_world
import title_state
import play_state

image = None
running = True

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

class Boy:
    def add_event(self, event):
        self.q.insert(0, event)

    def handle_events(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.q.insert(0, key_event)

    def __init__(self):
        self.q = []
        self.cur_state.enter(self, Boy.event)

    def update(self):
        self.cur_state.do(self)
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        pass

class IDLE:
    pass
class RUN:
    pass
class DRUN:
    pass
class TRUN:
    pass
class QRUN:
    pass

next_state = {
    IDLE : {RU: IDLE, LU: IDLE, UU: IDLE, DU: IDLE, RD: RUN, LD: RUN, UD: RUN, DD: RUN},
    RUN : {RU: IDLE, LU: IDLE, UU: IDLE, DU: IDLE, RD: DRUN, LD: DRUN, UD: DRUN, DD: DRUN},
    DRUN : {RU: RUN, LU: RUN, UU: RUN, DU: RUN, RD: TRUN, LD: TRUN, UD: TRUN, DD: TRUN},
    TRUN : {RU: DRUN, LU: DRUN, UU: DRUN, DU: DRUN, RD: QRUN, LD: QRUN, UD: QRUN, DD: QRUN},
    QRUN : {RU: TRUN, LU: TRUN, UU: TRUN, DU: TRUN, RD: IDLE, LD: IDLE, UD: IDLE, DD: IDLE}
}

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del image

def update():
    pass
    #play_state.update()

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(play_state.TUK_GROUND_FULL_WIDTH // 2, play_state.TUK_GROUND_FULL_HEIGHT // 2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_r:
                    game_framework.pop_state()
                case pico2d.SDLK_t:
                    game_framework.change_state(title_state)
                    game_world.clear()
                case pico2d.SDLK_q:
                    game_framework.quit()
