from itertools import chain
from collections import Counter

n, q = map(int, input().split(" "))
lr = [tuple(map(int, input().split(" "))) for _ in range(q)]

lr = [(lr_i[0]-1, lr_i[1]) for lr_i in lr]

points = [0] + sorted(chain(*lr)) + [n]
text = ""
stone = 0
for i in range(q*2+1):
    text += str(stone)*(points[i+1]-points[i])
    stone += 1
    stone %= 2
print(text)