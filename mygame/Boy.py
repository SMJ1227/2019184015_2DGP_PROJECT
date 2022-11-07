from pico2d import *
import play_state

class Boy:
    def __init__(self):
        self.character_x = play_state.TUK_GROUND_FULL_WIDTH // 2
        self.character_y = play_state.TUK_GROUND_FULL_HEIGHT // 2
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
            if self.rl == 2:
                self.rl += 1
            if self.character_x >= 1280:
                self.character_x = 1280
            elif self.character_y >= 1024:
                self.character_y = 1024
            elif self.character_y <= 0:
                self.character_y = 0
        elif self.dirrl == -1:
            if self.rl == 3:
                self.rl -= 1
            if self.character_x <= 0:
                self.character_x = 0
            elif self.character_y >= 1024:
                self.character_y = 1024
            elif self.character_y <= 0:
                self.character_y = 0
        elif self.dirud == 1:
            if self.character_y >= 1024:
                self.character_y = 1024
        elif self.dirud == -1:
            if self.character_y <= 0:
                self.character_y = 0

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
