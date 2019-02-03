# 完全に答え見た
# accumulateは部分列の総和の時に使いやすそう
from itertools import accumulate, groupby

N = int(input())
A = list(map(int, input().split(" ")))

f = lambda x: x*(x-1)
print(sum(f(len(list(g))) for _, g in groupby(sorted(accumulate([0]+A))))//2)
