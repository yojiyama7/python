import pyxel
from pyxel_key import KEY_LIST, KEY_DICT

WINDOW_WIDTH, WINDOW_HEIGHT = 240, 145
WINDOW_TITLE                = "title"
# PYXEL_FILE_NAME             = "file_name.pyxel"
FPS                         = 60

class App:
    def __init__(self):
        self.mouse_visible = True
        self.active_key_list = []

        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, caption=WINDOW_TITLE, fps=FPS)
        # pyxel.load(PYXEL_FILE_NAME)

        pyxel.run(self.update, self.draw)

    def update(self):
        # if pyxel.btnp(pyxel.KEY_Q):
        #     pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.mouse_visible = not self.mouse_visible
        pyxel.mouse(self.mouse_visible)
        self.active_key_list = [key for key in KEY_LIST if pyxel.btn(key)]

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, "Hello, Pyxel!", pyxel.frame_count//(FPS//10) % 16)
        pyxel.text(10, 20, f"mouse_x, mouse_y: {pyxel.mouse_x}, {pyxel.mouse_y}", 7)
        pyxel.text(10, 30, f"active keys number: {len(self.active_key_list)}", 7)
        pyxel.text(10, 40, f"active keys(code): {', '.join(map(str, self.active_key_list))}", 7)
        pyxel.text(10, 50, f"active keys: {', '.join(f'{KEY_DICT[key]}' for key in self.active_key_list)}", 7)
        pyxel.text(10, 60, f"active keys(both): {', '.join(f'{KEY_DICT[key]}({key})' for key in self.active_key_list)}", 7)
        pyxel.text(10, 70, f"* Toggle mouse cursor by space key.", 7)
        pyxel.text(10, 80, f"mouse visible: {self.mouse_visible}", 7)

App()