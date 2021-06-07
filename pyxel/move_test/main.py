import pyxel

CONFIG_FPS = 60

PLAYER_WIDTH = 8
PLAYER_HEIGHT = 8
PLAYER_SPEED = 0.7

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = PLAYER_WIDTH
        self.h = PLAYER_HEIGHT

        self.is_alive = True
    
    def update(self):
        mx, my = 0, 0
        if pyxel.btn(pyxel.KEY_D):
            mx += PLAYER_SPEED
        if pyxel.btn(pyxel.KEY_A):
            mx -= PLAYER_SPEED
        if pyxel.btn(pyxel.KEY_W):
            my -= PLAYER_SPEED
        if pyxel.btn(pyxel.KEY_S):
            my += PLAYER_SPEED
        
        if abs(mx) and abs(my):
            mx, my = mx*0.7, my*0.7
        
        self.x += mx
        self.y += my

    def draw(self):
        x, y = round(self.x), round(self.y)
        pyxel.rectb(x, y, self.w, self.h, 7)


class App:
    def __init__(self):
        pyxel.init(240, 135, fps=CONFIG_FPS)
        pyxel.mouse(True)

        self.player = Player(10, 10)

        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.player.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(3, 3, f"{self.player.x}, {self.player.y}", 7)

        self.player.draw()

if __name__ == "__main__":
    App()