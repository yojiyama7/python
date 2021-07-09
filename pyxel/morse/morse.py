import pyxel

INF = 10**18

W, H = 240, 145
TITLE = "title"

FPS = 60
NONE_FRAME = (0, 0)
DOT_FRAME = (1, 6)
BAR_FRAME = (7, 15)
BETWEEN_FRAME = (15, INF)

def is_inrange(x, lr):
    l, r = lr
    return l <= x <= r

class App:
    def __init__(self):
        pyxel.init(W, H, fps=FPS, caption=TITLE)

        self.sign = ""
        self.sound = [[0, 0]]
        self.text = ""   

        self.st = False

        pyxel.sound(0).set(
            "a2",
            "p",
            "6",
            "n",
            120,
        )
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):
            pyxel.play(0, 0)
            _, br = self.sound[-1]
            l = pyxel.frame_count
            w = l-br
            if is_inrange(w, BETWEEN_FRAME):
                self.sign += ' '
            self.sound.append([l, -1])
        if pyxel.btnr(pyxel.KEY_SPACE):
            pyxel.stop(0)
            self.sound[-1][1] = pyxel.frame_count
            l, r = self.sound[-1]
            w = r-l
            if is_inrange(w, NONE_FRAME):
                pass
            elif is_inrange(w, DOT_FRAME):
                self.sign += '.'
            elif is_inrange(w, BAR_FRAME):
                self.sign += '-'
            else:
                self.sign += '?'
        print(self.sign[-16:], end='\r', flush=True)
    def draw(self):
        pyxel.cls(0)
        if pyxel.btn(pyxel.KEY_SPACE):
            pyxel.rect(10, 10, 10, 10, 3)

App()