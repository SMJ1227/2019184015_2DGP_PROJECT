from pico2d import *
import random

class Map:
    def __init__(self):
        self.image = load_image('TUK_GROUND.png')

    def draw(self):
        self.image.draw(TUK_GROUND_FULL_WIDTH // 2, TUK_GROUND_FULL_HEIGHT // 2)

class Monster:
    def __init__(self):
        global character_x
        global character_y
        self.image = load_image('monster.png')
        self.monster_x = random.randint(0, TUK_GROUND_FULL_WIDTH)
        self.monster_y = random.randint(0, TUK_GROUND_FULL_HEIGHT)
        self.t = 0

    def update(self):
        self.monster_x = (1 - self.t) * self.monster_x + self.t * character_x #monster_x = (1 - t) * monster_x + t * character_x
        self.monster_y = (1 - self.t) * self.monster_y + self.t * character_y #monster_y = (1 - t) * monster_y + t * character_y
        self.t += 0.0000005
        # if self.t >= 1:
        #     self.t -= 1

    def draw(self):
        self.image.draw(self.monster_x, self.monster_y)

class Boy:
    def __init__(self):
        self.character_x = TUK_GROUND_FULL_WIDTH // 2
        self.character_y = TUK_GROUND_FULL_HEIGHT // 2
        self.upframe = 0
        self.downframe = 0
        self.dirrl = 0
        self.dirud = 0
        self. rl = 3
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.upframe = (self.upframe + 1) % 8
        self.downframe = (self.downframe - 1) % 8
        self.character_x += self.dirrl * 5
        self.character_y += self.dirud * 5
        if self.dirrl == 1:
            if self.character_x >= 1280:
                self.character_x = 1280
                if self.rl == 2:
                    self.rl += 1
        elif self.dirrl == -1:
            if self.character_x <= 0:
                self.character_x = 0
                if self.rl == 3:
                    self.rl -= 1
        elif self.dirud == 1:
            if self.character_y >= 1024:
                self.character_y == 1024
        elif self.dirud == -1:
            if self.character_y <= 0:
                self.character_y == 0

    def draw(self):
        if self.dirrl == 0 and self.dirud == 0:
            self.image.clip_draw(self.upframe * 100, 100 * self.rl, 100, 100, self.character_x, self.character_y)
        elif self.dirrl == 1:
            self.image.clip_draw(self.upframe * 100, 100 * 1, 100, 100, self.character_x, self.character_y)
        elif self.dirrl == -1:
            self.image.clip_draw(self.downframe * 100, 100 * 0, 100, 100, self.character_x, self.character_y)
        elif self.dirud == 1:
            self.image.clip_draw(self.upframe * 100, 100 * (self.rl-2), 100, 100, self.character_x, self.character_y)
        elif self.dirud == -1:
            self.image.clip_draw(self.downframe * 100, 100 * (self.rl-2), 100, 100, self.character_x, self.character_y)


def handle_events():
    global running
    global dirrl, dirud
    global mouse_x, mouse_y
    global bullets
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_d or event.key == SDLK_RIGHT:
                dirrl += 1
            elif event.key == SDLK_a or event.key == SDLK_LEFT:
                dirrl -= 1
            elif event.key == SDLK_w or event.key == SDLK_UP:
                dirud += 1
            elif event.key == SDLK_s or event.key == SDLK_DOWN:
                dirud -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_r:
                bullet_reloading()

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d or event.key == SDLK_RIGHT:
                dirrl -= 1
            elif event.key == SDLK_a or event.key == SDLK_LEFT:
                dirrl += 1
            elif event.key == SDLK_w or event.key == SDLK_UP:
                dirud -= 1
            elif event.key == SDLK_s or event.key == SDLK_DOWN:
                dirud += 1
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, TUK_GROUND_FULL_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            bullets -= 1
    pass


TUK_GROUND_FULL_WIDTH = 1280
TUK_GROUND_FULL_HEIGHT = 1024
open_canvas(1280, 1024)
target = load_image('target.png')
bullet = load_image('bullet.png')
hide_cursor()

running = True
mouse_x = TUK_GROUND_FULL_WIDTH // 2
mouse_y = TUK_GROUND_FULL_HEIGHT // 2
bullets = 6

tuk_ground = Map()
monster = Monster()
character = Boy()


def target_moving():
    global mouse_x, mouse_y
    target.draw(mouse_x, mouse_y)

def bullet_printing():
    global bullets
    for i in range(bullets):
        bullet.draw(1200, 100 + (i*30))

def bullet_reloading():
    global bullets
    bullets = 6

while running:
    handle_events()
    clear_canvas()

    tuk_ground.draw()
    character.draw()
    monster.draw()

    target_moving()
    bullet_printing()
    update_canvas()
    delay(0.01)

close_canvas()
