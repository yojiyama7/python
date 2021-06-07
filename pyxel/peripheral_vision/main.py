import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(240, 135, caption="peripheral vision", fps=60)
        pyxel.mouse(True)

        self.scene = 0
        self.scene_init = False

        self.timer = -1

        self.rect_size = 19
        self.rect_between = 1

        self.block = []
        
        self.current_num = 1

        self.start_frame = -1
        self.end_frame = -1
        self.duration_frame = -1
    
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.scene == 0:
            if self.scene_init == False:
                self.timer = -1
                nums = list(range(1, 26))
                random.shuffle(nums)
                self.blocks = []
                size = (self.rect_size+self.rect_between)
                all_size = size*5-self.rect_between
                tx = (pyxel.width-all_size)//2
                ty = (pyxel.height-all_size)//2
                for i, num in enumerate(nums):
                    x, y = i%5, i//5
                    block = Block(tx+x*size, ty+y*size, self.rect_size, 13, 0, num)
                    self.blocks.append(block)
                self.current_num = 1
                self.start_frame = -1
                self.end_frame = -1
                self.duration_frame = -1
                self.scene_init = True
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.timer == -1:
                self.timer = 180
            if self.timer > 0:
                self.timer -= 1
            if self.timer == 0:
                self.start_frame = pyxel.frame_count
                self.scene = 1
        elif self.scene == 1:
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                for block in self.blocks:
                    if block.is_inside(pyxel.mouse_x, pyxel.mouse_y):
                        if block.num == self.current_num:
                            block.blink(5)
                            self.current_num += 1
                        else:
                            block.blink(8)
            if self.current_num >= 26:
                self.end_frame = pyxel.frame_count
                self.duration_frame = self.end_frame - self.start_frame
                self.scene = 2
            for block in self.blocks:
                block.update()
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.scene_init = False
                self.scene = 0
        elif self.scene == 2:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.scene_init = False
                self.scene = 0

            


    def draw(self):
        pyxel.cls(7)
        if self.scene == 0:
            if self.timer == -1:
                s = "CLICK TO START"
                tx = -(-(pyxel.width-len(s)*4-1)//2)
                ty = -(-(pyxel.height-5)//2)
                pyxel.text(tx, ty, s, 0)
            else:
                s = str(-(-self.timer//60))
                tx = -(-(pyxel.width-len(s)*4-1)//2)
                ty = -(-(pyxel.height-5)//2)
                pyxel.text(tx, ty, s, 0)
        elif self.scene == 1:
            for block in self.blocks:
                block.draw()
            pyxel.text(4, 4, str(round((pyxel.frame_count-self.start_frame)/60, 2)), 0)
        elif self.scene == 2:
            if self.duration_frame != -1:
                s = f"score: {str(round(self.duration_frame/60, 2))}"
                tx = -(-(pyxel.width-len(s)*4-1)//2)
                ty = -(-(pyxel.height-5)//2)
                pyxel.text(tx, ty, s, 0)
                s = "SPACE TO FINISH"
                tx = -(-(pyxel.width-len(s)*4-1)//2)
                ty = -(-(pyxel.height-5)//2)
                ty += 6
                pyxel.text(tx, ty, s, 0)
    # def blink_rect(self, index, col):
    #     size = (self.rect_size+self.rect_between)
    #     all_size = size*5-self.rect_between
    #     tx = (pyxel.width-all_size)//2
    #     ty = (pyxel.height-all_size)//2

    #     i, j = index%5, index//5
    #     x, y = tx+i*size, ty+j*size

    #     pyxel.rectb(x, y, self.rect_size, self.rect_size, col)

class Block:
    def __init__(self, x, y, size, rect_col, num_col, num):
        self.x = x
        self.y = y
        self.size = size
        self.rect_col = rect_col
        self.num = num
        self.num_col = num_col

        self.blink_frame = 0
        self.blink_col = 0
    
    def update(self):
        if self.blink_frame > 0:
            self.blink_frame -= 1

    def is_inside(self, x, y):
        return (self.x <= x < self.x+self.size and self.y <= y < self.y+self.size)

    def draw(self):
        col = self.blink_col if self.blink_frame > 0 else self.rect_col
        pyxel.rectb(self.x, self.y, self.size, self.size, col)
        s = str(self.num)
        dw = -(-(self.size-(len(s)*4-1))//2)
        dh = -(-(self.size-5)//2)
        pyxel.text(self.x+dw, self.y+dh, s, self.num_col)
    
    def blink(self, col):
        self.blink_col = col
        self.blink_frame = 20


App()