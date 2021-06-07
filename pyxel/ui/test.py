import pyxel
import part
import random

# def rect_center(x, y, w, h, col):
#     pyxel.rect(x-w//2, y-h//2, w, h, col)

# def rectb_center(x, y, w, h, col):
#     pyxel.rectb(x-w//2, y-h//2, w, h, col)

class App:
    def __init__(self):
        pyxel.init(
            *(240, 135),
            caption="ui test",
            fps=60,
        )
        pyxel.mouse(True)

        # rect_1
        self.rect_1_col = 1
        # rect_2
        self.rect_2_is_draw = False
        self.rect_2_index = 0
        self.rect_2_x = 0
        self.rect_2_y = 0
        self.rect_2_w = 0
        self.rect_2_h = 0
        self.rect_2_col = 3

        pyxel.run(self.update, self.draw)
    
    def update(self):
        # rect_1
        x, y, w, h = pyxel.width//2, pyxel.height//2, 20, 10
        if x <= pyxel.mouse_x < x+w and y <= pyxel.mouse_y <= y+h:
            self.rect_1_is_hover = True
        else:
            self.rect_1_is_hover = False
        if self.rect_1_is_hover:
            self.rect_1_col = 5
        else:
            self.rect_1_col = 1
        # rect_2
        if self.rect_1_is_hover: 
            self.rect_2_is_draw = True
            if self.rect_2_index == 0:
                self.rect_2_x = pyxel.width//2
                self.rect_2_y = pyxel.height//2
                self.rect_2_w = 20
                self.rect_2_h = 10
            elif self.rect_2_index % 4 == 0 and self.rect_2_index // 4 >= 2:
                self.rect_2_x -= 1
                self.rect_2_y -= 1
                self.rect_2_w += 2
                self.rect_2_h += 2
            self.rect_2_index = (self.rect_2_index + 1) % 20
        else:
            self.rect_2_is_draw = False
            self.rect_2_index = 0

    def draw(self):
        pyxel.cls(7)

        # rect_1
        pyxel.rectb(pyxel.width//2, pyxel.height//2, 20, 10, self.rect_1_col)
        # rect_2
        if self.rect_2_is_draw:
            pyxel.rectb(self.rect_2_x, self.rect_2_y, self.rect_2_w, self.rect_2_h, self.rect_2_col)
if __name__ == "__main__":
    App()