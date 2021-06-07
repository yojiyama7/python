import pyxel

WINDOW_WIDTH, WINDOW_HEIGHT = 240, 145
WINDOW_TITLE                = "title"
PYXEL_FILE_NAME             = "my_resource.pyxres"

class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, caption=WINDOW_TITLE)
        pyxel.load(PYXEL_FILE_NAME)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

App()