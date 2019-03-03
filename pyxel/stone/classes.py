import pyxel
import numpy as np

# property
def two_vector_prop(name):
    def getter(self):
        return self.__dict__[name]

    def setter(self, pos):
        self.__dict__[name] = np.array(pos)

    return property(getter, setter)

def sub_prop(name):
    def getter(self):
        return self.__dict__[name]

    def setter(self, v):
        self.__dict__[name] = v

    return property(getter, setter)

# pyxel wraper
class Surface:
    def __init__(self):
        pass
    def draw(self):
        pass


class SurfaceImg:
    __pos   = two_vector_prop("pos")
    __pos_x = sub_prop("pos_x")
    __pos_y = sub_prop("pos_y")
    def __init__(self, img, pos, size, colkey=None):
        self.img = img
        self.pos = pos
        self.size = size
        self.colkey = colkey

    def draw(self, display_pos):
        pyxel.blt(*display_pos, self.img, *self.pos, *self.size, self.colkey)


class Part:
    __pos     = two_vector_prop("pos")
    __std_pos = two_vector_prop("std_pos")
    def __init__(self, surface, pos=(0, 0)):
        self.surface = surface
        self.pos = pos

        self.std_pos = (0, 0)

    def draw(self):
        self.surface.draw(self.std_pos + self.pos)


class Board:
    def __init__(self):
        pass
    def draw(self):
        pass


################################


"""
Pos
Pos.x       : x座標
Pos.y       : y座標
Pos.tuple   : (self.x, self.y)
Pos.np_array: np.array([self.x, self.y])
"""


# class TwoVector:
#     def __init__(self, values):
#         self.values = np.array(values[:2])
    
#     def __repr__(self):
#         return f"Twovector: {self.values}"
#     def __len__(self):
#         return len(self.values)
#     def __array__(self):
#         return self.values
#     def __array_ufunc__(ufunc, method, *inputs, **kwargs):
#         print(ufunc, method, inputs, kwargs)


# if __name__ == "__main__":
#     x = TwoVector([3, 5])
#     print(x)
#     print(np.array(x).shape)
