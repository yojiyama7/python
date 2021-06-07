# TODO:
# 親子関係などのない他人であるオブジェクトであっても連絡の取れる要素取得方法
# Obj系統のクラスの抽象クラスの作成 ( 継承させる or プロパティにもたせ、メソッド等を__getattr__で使えるようにする又その部分の抽象化 )
    # 引数
        # xy
        # update_func(eventsとも関係)
        # (wh, col)
    # メソッド
        # update
        # draw
        # events(click, hoverなど),
# ある地点(オブジェクトや画面自体の右上、左下等)を基準とした相対座標

def _pass(*_):
    pass

import pyxel
import pyxel_framework
from pyxel_framework import *

from collections import deque
from random import randint

# HACK: このオブジェクトだけ特殊にほかのオブジェクトを取得している。
# 別の階層にいるそれぞれのオブジェクトが簡潔に連絡を取れたほうが良い。
class ObjRectNumList:
    def __init__(self, name, xy, wh, between, num_gen_func, update_func=_pass):
        self.name = name
        self.xy = xy
        # print(self.xy)
        self.wh = wh
        self.between = between
        self.num_gen_func = num_gen_func
        self.init_num_list()
        self.update_func = update_func

        self.is_update = True
        self.is_draw = True
        self.is_die = False
    
    def init_num_list(self):
        self.num_list = deque([1])
        for _ in range(6):
            self.append()
        self.update_rect_list()

    def update_rect_list(self):
        self.rect_list = [self.convert_num_to_rect(v, i) for i, v in enumerate(self.num_list)]

    def __setattr__(self, name, var):
        if name == "num_list":
            # self.num_list = var
            object.__setattr__(self, name, var)
            self.update_rect_list()
        else:
            object.__setattr__(self, name, var)

    def die(self):
        self.is_die = True

    def pop_and_append(self):
        print(len(self.num_list), self.num_list)
        self.pop()
        self.append()
        self.update_rect_list()

    def pop(self):
        self.num_list.pop()
        self.update_rect_list()
    
    def append(self):
        self.num_list.appendleft(self.num_gen_func(self))
        self.update_rect_list()

    def convert_num_to_rect(self, num, i):
        cols = [9, 13, 5]
        return Objs("", [
            ObjRect("", (self.xy[0], self.xy[1]+(self.between+self.wh[1])*i), self.wh, cols[num]),
            ObjRect("", (self.xy[0]+self.wh[0]*[-1, 0, 1][num], self.xy[1]+(self.between+self.wh[1])*i+self.wh[1]//2-2), (self.wh[0], 4), cols[num])
        ])

    def update(self):
        if not self.is_update:
            return
        for rect in self.rect_list:
            rect.update()
        self.update_func(self)
    
    def draw(self):
        if not self.is_draw:
            return
        for rect in self.rect_list:
            rect.draw()


class ObjPlayer:
    def __init__(self, name, xy, wh, col, update_func=_pass):
        self.name = name
        self.xy = xy
        self.wh = wh
        self.col = col
        self.update_rect()
        self.update_func = update_func
        self.pos_num = 0

        self.is_update = True
        self.is_draw = True
        self.num_queue = None
    
    def is_dead(self, num):
        return self.pos_num == num

    def left(self):
        self.pos_num = 0
        if self.is_dead(self.num_queue.num_list[-1]):
            self.num_queue.die()
        self.num_queue.pop_and_append()
        if self.is_dead(self.num_queue.num_list[-1]):
            self.num_queue.die()

    def right(self):
        self.pos_num = 2
        if self.is_dead(self.num_queue.num_list[-1]):
            self.num_queue.die()
        self.num_queue.pop_and_append()
        if self.is_dead(self.num_queue.num_list[-1]):
            self.num_queue.die()

    def update_rect(self):
        self.rect = ObjRect(self.name, self.xy, self.wh, self.col)
    
    def update(self):
        if not self.is_update:
            return
        self.update_func(self)
        if self.pos_num == 0:
            self.xy = (120-17-23, 92)
            self.update_rect()
        elif self.pos_num == 2:
            self.xy = (120+23, 92)
            self.update_rect()

    def draw(self):
        if not self.is_draw:
            return
        self.rect.draw()



class PyxelApp:
    def __init__(self):
        pyxel.init(240, 135, caption="Test", fps=60)
        pyxel.mouse(True)
        pyxel.load("assets/my_resource.pyxres")

        def set_text_mouse_pos(this):
            this.text = f"{pyxel.mouse_x}, {pyxel.mouse_y}"

        # self.var = Variables({
        #     "tree_queue": deque([0]*7),
        #     "player_pos_num": 0,
        # })

        self.obj = Objs("root", [
            Objs("home", [
                ObjBackGround("background_home", 6),
                ObjRect("ground", (0, 100), (pyxel.width, 35), 4),
                ObjRect("tree_1", (38, 30), (20, 80), 9),
                ObjRect("leef_1", (20, 6), (54, 50), 3),
                ObjRect("tree_2", (108, 40), (20, 80), 9),
                ObjRect("leef_2", (95, 20), (47, 53), 3),
                ObjRect("tree_3", (178, 34), (20, 80), 9),
                ObjRect("leef_3", (163, 17), (44, 63), 3),
                ObjRect("rect_1", (90, 90), (60, 18), 13,
                    update_func=(lambda this:
                        self.obj.select_child("playing") if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and this.is_hover(get_mouse_xy()) else None 
                    )
                ),
                ObjRectFrame("rect_frame_1", (90, 90), (60, 18), 7),
                ObjText("text_1", (110, 97), "START", 0),
                Objs("title", [
                    # ObjRect("rect_1", (92, 21), (56, 8), 7),
                    # ObjRect("rect_1", (92, 21), (56, 22), 7),
                    # ObjRect("rect_2", (78, 36), (59, 7), 7),
                    ObjImg("img_1", (80, 14), 0, (0, 0, 76, 16), 0),
                    ObjImg("img_2", (70, 27), 0, (0, 16, 101, 16), 0),
                ]),
            ]),
            Objs("playing", [
                ObjBackGround("background_playing", 0),
                # ObjRect("rect_1", (110, 97), (20, 97), 7),
                Objs("games", [
                    ObjPlayer("player1", (120-40, 92), (17, 17), 2,
                    update_func=lambda this: [
                        this.left() if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.KEY_LEFT) else None,
                        this.right() if pyxel.btnp(pyxel.KEY_D) or pyxel.btnp(pyxel.KEY_RIGHT) else None,
                    ]
                    ),
                    ObjRectNumList("rects_1", (104, -2), (32, 16), 0, lambda this: randint(0, 2) if this.num_list[0] == 1 else 1,
                        update_func=lambda this: [
                            [self.obj.playing.gameover.__setattr__(k, True) for k in ["is_update", "is_draw"]] if this.is_die else None,
                            this.__setattr__("is_die", False) if this.is_die else None,
                        ]
                    ),
                ]),
                ObjRect("rect_1", (120-60-10, 100), (10, 10), 9),
                ObjRect("rect_2", (120+60, 100), (10, 10), 5),
                Objs("gameover", [
                    ObjRect("rect_gameover", (120-40, 67-30), (80, 60), 7),
                    ObjRectFrame("rect_frame_gameover", (120-40, 67-30), (80, 60), 13),
                    ObjText("text_gameover", (120-17, 67-2), "GAME OVER", 0),
                    ObjRectFrame("rectframe_return", (120+28, 67+18), (10, 10), 13),
                    ObjImg("img_2", (120+28+1, 67+18+1), 0, (0, 32, 8, 8), 0,
                        update_func=lambda this: [self.obj.select_child("home"), [self.obj.playing.gameover.__setattr__(k, False) for k in ["is_update", "is_draw"]]] if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and this.is_hover(get_mouse_xy()) else None,
                    ),
                ], is_update=False, is_draw=False)
            ]),
            ObjText("text_1", (1, 1), "", 7,
                update_func=lambda this: this.__setattr__("text", f"{pyxel.mouse_x}, {pyxel.mouse_y}")
            ),
        ])
        # HACK
        self.obj.select_child("home")
        self.obj.playing.games.player1.num_queue = self.obj.playing.games.rects_1

        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.obj.update()

    def draw(self):
        self.obj.draw()
        # pyxel.text(1, 1, f"{pyxel.mouse_x}, {pyxel.mouse_y}", 7)


if __name__ == "__main__":
    PyxelApp()
