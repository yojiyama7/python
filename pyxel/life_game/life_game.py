import pyxel
from itertools import product
from random import randint

W, H = 100, 100

class App:
    def __init__(self):
        pyxel.init(240, 135, caption="life_game", fps=60)
        pyxel.mouse(True)

        self.x = 10
        self.y = 10
        self.game_map = [[randint(0, 1) for _ in range(W)] for _ in range(H)]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count % 4:
            return
        game_next = [[0 for _ in range(W)] for _ in range(H)]
        for ty, tx in product(range(H), range(W)):
            for dy, dx in product(range(-1, 2), range(-1, 2)):
                if dx == dy == 0:
                    continue
                x, y = tx+dx, ty+dy
                if not (0 <= x < W and 0 <= y < H):
                    continue
                game_next[ty][tx] += self.game_map[y][x]
        self.game_map = [[
            (self.game_map[y][x] and 2 <= game_next[y][x] <= 3) or 
            (not self.game_map[y][x] and game_next[y][x] == 3)
        for x in range(W)] for y in range(H)]

    def draw(self):
        pyxel.cls(0)
        
        for dy, dx in product(range(H), range(W)):
            x = self.x + dx
            y = self.y + dy
            if self.game_map[dy][dx]:
                pyxel.pset(x, y, 11)

if __name__ == "__main__":
    App()