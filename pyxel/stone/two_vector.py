# HACK: np.ndarrayを使って代用している(要素の個数を意図して2つにしている)

# 数値演算はnumpyと同じ挙動
# import numpy as np


# class TwoVector(np.ndarray):
#     def __init__(self, x, y):
#         self.__two_v = np.array([x, y])
#     @property
#     def x(self):
#         return self.__two_v[0]
#     @x.setter
#     def x(self, x):
#         self.__two_v[0] = x
#     @property
#     def y(self):
#         return self.__two_v[y]
#     @x.setter
#     def x(self, y):
#         self.__two_v[0] = y

#     def __add__(self, other):
#         return TwoVector(*(self.__two_v + other.__two_v))

#     def __repr__(self):
#         return f"TwoVector: {self.__two_v}"


# if __name__ == "__main__":
#     a, b = TwoVector(10, 20), TwoVector(30, 40)
#     print(a, b)
#     print(a + b)