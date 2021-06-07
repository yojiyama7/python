import pyxel


def _pass(*_):
    pass

def get_mouse_xy():
    return (pyxel.mouse_x, pyxel.mouse_y)

# class Value()


class Objs:
    def __init__(self, name, obj_list, is_update=True, is_draw=True):
        self.name = name
        self.obj_list = obj_list

        self.is_update = is_update
        self.is_draw = is_draw

    # HACK: 計算量がO(N)
    def __getattr__(self, name):
        for obj in self.obj_list:
            if obj.name == name:
                return obj
        raise ValueError(f"{self.name} don't have '{name}' propaty.")

    def select_child(self, name):
        for obj in self.obj_list:
            # print(obj.name, name, (obj.name == name))
            b = (obj.name == name)
            obj.is_update = b
            obj.is_draw = b
        # for obj in self.obj_list:
        #     print(obj.name, obj.is_update, obj.is_draw)
        

    def update(self):
        if not self.is_update:
            return
        for obj in self.obj_list:
            obj.update()

    def draw(self):
        if not self.is_draw:
            return
        for obj in self.obj_list:
            obj.draw()


class Variables:
    def __init__(self, var_dict):
        for k, v in var_dict.items():
            self.__setattr__(k, v)

    def update(self):
        pass

    def draw(self):
        pass


class ObjBackGround:
    def __init__(self, name, col, update_func=_pass):
        self.name = name
        self.col = col
        self.update_func = update_func

        self.is_update = True
        self.is_draw = True
    
    def update(self):
        if not self.is_update:
            return
        # print(f"update '{self.name}' background")
        self.update_func(self)

    def draw(self):
        if not self.is_draw:
            return
        pyxel.cls(self.col)


class ObjRect:
    def __init__(self, name, xy, wh, col, update_func=_pass):
        self.name = name
        self.xy = xy
        self.wh = wh
        self.col = col
        self.update_func = update_func

        self.is_update = True
        self.is_draw = True
    
    def is_hover(self, xy):
        return all(self.xy[i] <= xy[i] < self.xy[i]+self.wh[i] for i in range(2))

    def update(self):
        if not self.is_update:
            return
        self.update_func(self)

    def draw(self):
        if not self.is_draw:
            return
        pyxel.rect(*self.xy, *self.wh, self.col)


class ObjRectFrame:
    def __init__(self, name, xy, wh, col, update_func=_pass):
        self.name = name
        self.xy = xy
        self.wh = wh
        self.col = col
        self.update_func = update_func

        self.is_update = True
        self.is_draw = True
    
    def update(self):
        if not self.is_update:
            return
        self.update_func(self)

    def draw(self):
        if not self.is_draw:
            return
        pyxel.rectb(*self.xy, *self.wh, self.col)


class ObjImg:
    def __init__(self, name, xy, bank_num, uvwh, colkey=-1, update_func=_pass):
        self.name = name
        self.xy = xy
        self.bank_num = bank_num
        self.uvwh = uvwh
        self.colkey = colkey
        self.update_func = update_func

        self.is_update = True
        self.is_draw = True
    
    def is_hover(self, xy):
        return all(self.xy[i] <= xy[i] < self.xy[i]+self.uvwh[2+i] for i in range(2))

    def update(self):
        if not self.is_update:
            return
        self.update_func(self)

    def draw(self):
        if not self.is_draw:
            return
        pyxel.blt(*self.xy, self.bank_num, *self.uvwh, self.colkey)


class ObjText:
    def __init__(self, name, xy, text, col, update_func=_pass):
        self.name = name
        self.xy = xy
        self.text = text
        self.col = col
        self.update_func = update_func

        self.is_update = True
        self.is_draw = True
    
    def update(self):
        if not self.is_draw:
            return
        self.update_func(self)

    def draw(self):
        if not self.is_draw:
            return
        pyxel.text(*self.xy, self.text, self.col)