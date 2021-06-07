import pyxel
from dot_dict import DotDict as dd
from wrapped_value import WrappedValue as wv

CONFIG = dd({
    "width": 256,
    "height": 135,
    "fps": 144,
})

class Surface:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def update(self):
        pass

    def draw(self):
        pass
    

class SurfaceRect(Surface):
    def __init__(self)

class App:
    def __init__(self):
        pyxel.init(CONFIG.width, CONFIG.height, fps=CONFIG.fps)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

App()