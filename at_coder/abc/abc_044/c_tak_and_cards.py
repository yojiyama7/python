# DPだよわからないよおおおお
from functools import lru_cache

N, A = map(int, input().split(" "))
X = list(map(int, input().split(" ")))

X = [x-A for x in X]

@lru_cache(maxsize=None)
def dfs(n)