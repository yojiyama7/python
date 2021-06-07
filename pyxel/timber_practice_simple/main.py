import pyxel as p
from collections import deque
import pickle
import os


class App:
    def __init__(self):
        p.init(240, 135, caption="Timber Practice", fps=60)
        p.load("assets/my_resource.pyxres")
        p.mouse(True)

        if os.path.isfile("tree_queue_pattern.pyc"):
            # print("yes")
            with open("tree_queue_pattern.pyc", "rb") as f:
                self.tree_queue_pattern = pickle.load(f)
        else:
            # self.tree_queue_pattern = [0, 1, 0, 2]
            self.tree_queue_pattern = [0, 1, 1, 0, 2, 2, 0, 1, 0, 2, 2, 0, 1, 1, 0, 2]
        self.start_game()
        self.is_setting = False
        self.tree_y_adjust = 0

        p.run(self.update, self.draw)

    def is_dead(self):
        return self.player_pos == self.tree_queue[-1]
    def gameover(self):
        self.is_gameover = True
    def check_and_solve_gameover(self):
        if self.is_dead():
            self.gameover()

    def start_game(self):
        self.player_pos = 1
        self.tree_index = 0
        self.tree_queue = deque()
        [self.append_tree_queue() for _ in range(7)]
        self.is_gameover = False

    def append_tree_queue(self):
        t = self.tree_queue_pattern[self.tree_index % len(self.tree_queue_pattern)]
        self.tree_queue.appendleft(t)
        self.tree_index += 1
        self.tree_y_adjust = 6
    def pop_and_push_tree_queue(self):
        self.tree_queue.pop()
        self.append_tree_queue()
    
    def move_player(self, player_pos):
        self.player_pos = player_pos
        self.check_and_solve_gameover()
        self.pop_and_push_tree_queue()
        self.check_and_solve_gameover()

    def is_in_rect(self, cxy, xy, wh):
        cx, cy = cxy
        x, y, w, h = *xy, *wh
        return (x <= cx < x+w and y <= cy < y+h)

    def update(self):
        self.tree_y_adjust = max(0, self.tree_y_adjust - 1)

        if self.is_setting:
            if p.btnp(p.MOUSE_LEFT_BUTTON):
                if self.is_in_rect((p.mouse_x, p.mouse_y), [4, 4], [9, 9]):
                    self.is_setting = False
                    with open("tree_queue_pattern.pyc", "wb") as f:
                        pickle.dump(self.tree_queue_pattern, f)
                    self.start_game()
                for i, t in enumerate(self.tree_queue_pattern):
                    if self.is_in_rect((p.mouse_x, p.mouse_y), [4, 20+10*i], [9, 9]):
                        self.tree_queue_pattern[i] = (self.tree_queue_pattern[i] + 1) % 3
                if self.is_in_rect((p.mouse_x, p.mouse_y), [4, 20+10*len(self.tree_queue_pattern)], [9, 9]):
                    self.tree_queue_pattern.append(0)
                if self.is_in_rect((p.mouse_x, p.mouse_y), [4, 20+10*(len(self.tree_queue_pattern)+1)], [9, 9]):
                    self.tree_queue_pattern.pop()
        else:
            if p.btnp(p.MOUSE_LEFT_BUTTON) and self.is_in_rect((p.mouse_x, p.mouse_y), [4, 4], [9, 9]):
                self.is_setting = True

        if self.is_gameover:
            if p.btnp(p.MOUSE_LEFT_BUTTON) and self.is_in_rect((p.mouse_x, p.mouse_y), (120-20, 67+24), (40, 16)) or p.btnp(p.KEY_SPACE):
                self.start_game()
        else:
            if any(p.btnp(k) for k in [p.KEY_A, p.KEY_LEFT, p.KEY_J]):
                self.move_player(1)
                # p.play(0, 0)
            elif any(p.btnp(k) for k in [p.KEY_D, p.KEY_RIGHT, p.KEY_L]):
                self.move_player(2)
                # p.play(1, 0)
            # if p.btnp(p.KEY_SPACE):
            #     self.start_game()
                

    def draw(self):
        p.cls(6)

        p.rectb(*[[120-20-15, 97], [120+20, 97]][self.player_pos-1], 15, 15, 7)

        for i, t in enumerate(self.tree_queue):
            y = -7+17*i - (self.tree_y_adjust*17)//6
            p.rect(*[120-15, y], *[30, 17], 4)
            # p.blt(*[120-15, y], 0, *[0, 0], *[30, 17])
            if t == 1:
                p.rectb(*[120-15-30, y+(17-5)//2], *[30, 5], 4)
            if t == 2:
                p.rectb(*[120+15, y+(17-5)//2], *[30, 5], 4)

        if self.is_setting:
            p.rect(*(0, 0), *(17, 135), 7)
            p.rectb(*[4, 4], *[9, 9], 13)
            p.text(*[7, 6], "X", 13)
            for i, t in enumerate(self.tree_queue_pattern):
                p.rectb(*[4, 20+10*i], *[9, 9], 13)
                p.text(*[7, 22+10*i], "NLR"[t], 0)
            p.rectb(*[4, 20+10*len(self.tree_queue_pattern)], *[9, 9], 13)
            p.text(*[7, 22+10*len(self.tree_queue_pattern)], "+", 0)
            p.rectb(*[4, 20+10*(len(self.tree_queue_pattern)+1)], *[9, 9], 13)
            p.text(*[7, 22+10*(len(self.tree_queue_pattern)+1)], "-", 0)
        else:
            p.rectb(*[4, 4], *[9, 9], 0)
            p.text(*[7, 6], "O", 0)

        if self.is_gameover:
            p.rect(*(120-30, 67-45), 60, 90, 7)
            p.rectb(*(120-30, 67-45), 60, 90, 13)
            p.text(*(120-18, 67-30), "GAME OVER", 0)
            p.rectb(*(120-20, 67+24), *(40, 16), 13)
            p.text(*(120-7, 67+30), "NEXT", 0)
        else:
            pass


if __name__ == "__main__":
    App()