# 何言ってるかわからんのやけど
# 問題概要を理解できていない丸。
from math import pi

def volume_of_cone(r, h):
    # print(r*r*h)
    return r*r*pi*h / 3

l = [list(map(int, input().split(" "))) for _ in range(10)]

for l_i in l:
    print(volume_of_cone(*l_i[1:]))