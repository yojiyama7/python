import pyxel
from fractions import Fraction

def draw_line_with_fraction(x0, y0, x1, y1, col):
    # 2点のどちらが始点か[点1, (点2)]
    # x, y のどちらを基準軸にするか[x, y]
    ### for 文を回す時の方向
    ### w > h の時 x
    ### w = h の時 どっちでも
    ### w < h の時 y
    
    # 基準軸の方向
    # サブ軸の方向

    w = x1 - x0
    h = y1 - y0
    is_steep = h > w

    error = Fraction(0)
    gradient = abs(Fraction(h) / Fraction(w)) 
    y = y0
    for x in range(x0, x1+1):
        if is_steep:
            pyxel.pset(y, x, col)
        else:
            pyxel.pset(x, y, col)
        error += gradient
        if error >= 0.5:
            y += 1
            error -= Fraction(1)
def draw_line_with_magnification_2w(x0, y0, x1, y1, col):
    w = x1 - x0
    h = y1 - y0

    error = 0
    gradient = 2*h
    y = y0
    for x in range(x0, x1+1):
        pyxel.pset(x, y, col)
        error += gradient
        if error >= w:
            y += 1
            error -= 2*w
def draw_line(x0, y0, x1, y1, col):
    draw_line_with_fraction(x0, y0, x1, y1, col)
    # draw_line_with_magnification_2w(x0, y0, x1, y1, col)

class App:
    def __init__(self):
        pyxel.init(240, 135, fps=144)
        pyxel.mouse(True)

        self.pos_list = [
            (0, 0),
            (97, 23),
        ]
        self.col = 0
        self._pos_turn = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.pos_list[self._pos_turn] = (pyxel.mouse_x, pyxel.mouse_y)
            self._pos_turn = (self._pos_turn + 1) % len(self.pos_list)

    def draw(self):
        pyxel.cls(7)
        draw_line(*self.pos_list[0], *self.pos_list[1], self.col)
        pyxel.pset(*self.pos_list[0], 3)
        pyxel.pset(*self.pos_list[1], 8)

if __name__ == "__main__":
    App()