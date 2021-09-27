
from typing_extensions import OrderedDict
import pyxel
from pyxel import *
from collections import OrderedDict as ODict

WHITE = 7
W, H = SIZE = (15*16, 15*9)
CAPTION = "Hello Pyxel"
FPS = 144

class Obj:
    def __init__(self, name, func, values, status=dict(), childs=[]):
        self.name = name
        self.func = func
        self.values = values
        self.status = status

    def draw(self):
        self.func(*self.values)
        for c in self.childs:
            c.draw()

objs_raw = [
    Obj("box", pyxel.rectb, [30, 10, W-15, H-5, WHITE], childs=[
        Obj("box-inner", pyxel.rectb[5, 5, 10, 10, WHITE]),    
    ]),
]

objs = OrderedDict([(obj.name, obj) for obj in objs_raw])

class App:
    def __init__(self):
        pyxel.init(W, H, caption=CAPTION, fps=FPS)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(KEY_Q):
            pyxel.quit()

    def draw_objs(self, objs):
        for obj in objs:
            obj.draw()

    def draw(self):
        pyxel.cls(0)
        self.draw_objs(objs):

App()