import pyxel
import random
import numpy as np
from classes import *
from vector_two import Vector2 as V2

WINDOW_WIDTH, WINDOW_HEIGHT = 192, 108
WINDOW_TITLE                = "Stone"
PYXEL_FILE_NAME             = "stone.pyxel"
surfaces = {
    # "stone": SurfaceImg(0, (0, 0), (8, 8)),
    "stone_logo": SurfaceImg(0, V2(0, 32), V2(38, 10)),
}
parts = {
    "stone_logo" : Part(surfaces["stone_logo"]),
    "stone_logo2": Part(surfaces["stone_logo"]),
}
parts["stone_logo"].pos = V2(WINDOW_WIDTH - parts["stone_logo"].surface.size.x - 4, 4)

# for a in parts["stone_logo"].pos:
#     for b in parts["stone_logo"].pos:
#         print("a", a, b)


class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, caption=WINDOW_TITLE)
        pyxel.load(PYXEL_FILE_NAME)

        # # # #

        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # parts["stone_logo"].pos.y += 1

    def draw(self):
        pyxel.cls(0)
        # pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        # for x in range(0, 64, 8):
        #     for y in range(0, 64, 8):
        #         Surfaces["stone"].draw((x, y))
        # pyxel.blt(0, 0, 0, 0, 0, 8, 8)
        # pyxel.blt(0, 0, 0, 0, 0, 8, -8)
        for part in parts.values():
            part.draw()
        # pyxel.bltm(0, 0, 0, 0, 0, 10, 7)


App()