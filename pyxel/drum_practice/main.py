import pyxel
import random

WINDOW_WIDTH, WINDOW_HEIGHT = 240, 145
WINDOW_TITLE                = "title"
# PYXEL_FILE_NAME             = "file_name.pyxel"

class Rect:
    def __init__(self, x, y, w, h, col):
        self.x, self.y, self.w, self.h, self.col = x, y, w, h, col
        self.is_clicked = False
    
    def update(self):
        self.is_clicked = False
        if self.is_hover() and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.is_clicked = True

    def draw(self):
        pyxel.rectb(self.x, self.y, self.w, self.h, self.col)

    def is_hover(self):
        return all([
            self.x <= pyxel.mouse_x < self.x+self.w,
            self.y <= pyxel.mouse_y < self.y+self.h
        ])

class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, caption=WINDOW_TITLE, fps=60)
        pyxel.mouse(True)
        # pyxel.load(PYXEL_FILE_NAME)

        self.bass_notes = [random.randint(0, 1) for _ in range(8)]
        self.obj_bass_notes = []
        pw, ph = 8, 8
        pb = 12
        cw = (pw+pb)*8-pb
        cx = (pyxel.width-cw)//2
        for i in range(8):
            x = cx + (pw+pb)*i
            y = 30
            self.obj_bass_notes.append(Rect(x, y, pw, ph, 0))
            if i%4 == 2:
                y = 50
                self.obj_bass_notes.append(Rect(x, y, pw, ph, 0))
            if self.bass_notes[i]:
                y = 70
                self.obj_bass_notes.append(Rect(x, y, pw, ph, 0))
        self.obj_play_button = []
        pw, ph = 16, 16
        pb = 0
        cw = (pw+pb)-pb
        cx = (pyxel.width-cw)//2
        x = cx
        y = 100
        self.obj_play_button.append(Rect(x, y, pw, ph, 1))
        self.obj_play_button.append(Rect(x+2, y+2, pw-4, ph-4, 1))

        pyxel.sound(0).set(
            "e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr",
            "p",
            "6",
            "vffn fnff vffs vfnn",
            25,
        )

        pyxel.run(self.update, self.draw)

    def update(self):
        for obj in self.obj_bass_notes:
            obj.update()
        for obj in self.obj_play_button:
            obj.update()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):
            pyxel.play(0, [0, 1], loop=True)
        if self.obj_play_button[0].is_clicked:
            self.play_sound()
        

    def draw(self):
        pyxel.cls(7)
        for obj in self.obj_bass_notes:
            obj.draw()
        for obj in self.obj_play_button:
            obj.draw()

    def play_sound(self):
        print("ssssound")

App()