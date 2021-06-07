import pyxel

class Animation:
    pass

class Blink(Animation):
    def __init__(self, col, duration):
        self.col = col
        self.duration = duration

        self.col2 = None
        self.counter = 0

    def update(self, obj):
        if self.counter == 0:
            self.col2 = obj.col
            obj.col = self.col
        elif self.counter >= self.duration:
            obj.col = self.col2
            obj.animations.remove(self)
        self.counter += 1

class Rect:
    def __init__(self, xy, wh, col):
        self.x, self.y = xy
        self.w, self.h = wh
        self.col = col

        self.animations = []

    def add_animation(self, animation):
        self.animations.append(animation)
        
    def update(self):
        for animation in self.animations:
            animation.update(self)

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.col)

class App:
    def __init__(self):
        pyxel.init(240, 135, fps=60)
        pyxel.mouse(True)

        self.objs = [
            Rect((20, 20), (30, 30), 3)
        ]

        pyxel.run(self.update, self.draw)
    
    def update(self):
        for obj in self.objs:
            obj.update()
        
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.objs[0].add_animation(Blink(5, 60))

    def draw(self):
        pyxel.cls(0)

        for obj in self.objs:
            obj.draw()


if __name__ == "__main__":
    App()