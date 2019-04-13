# 数値演算はnumpyと同じ挙動
import numpy as np

# def sub_prop(name):
#     def getter(self):
#         return self.__dict__[name]
#     def setter(self, v):
#         self.__dict__[name] = v
#     return property(getter, setter)

# def to_no_two_vector(x):
#     if type(x) == Vector2:
#         return x._two_v
#     return x

class Vector2:
    def __init__(self, x, y):
        self._two_v = np.array([x, y])

    @property
    def x(self):
        return self._two_v[0]
    @x.setter
    def x(self, x):
        self._two_v[0] = x
    @property
    def y(self):
        return self._two_v[1]
    @y.setter
    def y(self, y):
        self._two_v[1] = y

    def __add__(self, other):
        return Vector2(*(self._two_v.__add__(other._two_v)))
    def __sub__(self, other):
        return Vector2(*(self._two_v.__sub__(other._two_v)))

    def __repr__(self):
        return f"Vector2: {self._two_v}"
    def __iter__(self):
        return self._two_v.__iter__()
    def __next__(self):
        return self._two_v.__next__()

if __name__ == "__main__":
    a, b = Vector2(10, 20), Vector2(30, 40)
    print(a, a.x, a.y)
    print(a + b)
    print(a - b)

    print(*a)
    
    for m in a:
        print(m)
    
    # print(a * b)
