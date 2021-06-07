import pyxel as pxl

WIDTH   = 240
HEIGHT  = 135
FPS     = 144

# class Obj:
#     def __init__(self): pass
#     def draw(self): pass

# class DataRect:
#     def __init__(self, w, h, col):
#         self.w      = w
#         self.h      = h
#         self.col    = col

# class ObjRect:
#     def __init__(self, data):
#         self.data = data
#     def draw(self):
#         data = self.data
#         pyxel.rect(
#             data.x, data.y,
#             data.w, data.h, 
#             data.col
#         )

class App:
    def __init__(self):
        pxl.init(WIDTH, HEIGHT, fps=FPS)
        pxl.mouse(True)

        self.x, self.y = 1, 1

        pxl.run(self.update, self.draw)
    
    def update(self):
        if pxl.btn(pxl.KEY_A):
            self.x -= 1
        if pxl.btn(pxl.KEY_D):
            self.x += 1
        if pxl.btn(pxl.KEY_W):
            self.y -= 1
        if pxl.btn(pxl.KEY_S):
            self.y += 1

    def draw(self):
        pxl.cls(0)
        x, y = self.x, self.y
        w, h = [31]*2
        col = 7
        bw_w, bw_h = [11]*2
        for i in range(100):
            for j in range(100):
                a, b = x+(w+bw_w)*i, y+(h+bw_h)*j
                pxl.rectb(a, b, w, h, col)


if __name__ == "__main__":
    App()