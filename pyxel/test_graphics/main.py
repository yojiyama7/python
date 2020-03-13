import pyxel

WINDOW_WIDTH, WINDOW_HEIGHT = 240, 145
WINDOW_TITLE                = "title"
PYXEL_RESOURCE_FILE         = "my_resource.pyxel"

class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, caption=WINDOW_TITLE)
        pyxel.load(PYXEL_RESOURCE_FILE)

        self.x = 0
        self.y = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            self.y += 1
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            self.x += 1

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8)
App()