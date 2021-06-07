import pyxel

class Part:
    def check_is_click(self):
        return self.check_is_hover() and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)
    
    def update(self):
        if check_is_click():
            self.func_click()


class Rect:
    def __init__(self, x, y, w, h, col):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col

    def update(self):
        pass

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.col)