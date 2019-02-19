# これはdp慣れしてますわぁ、、(答え写した)
# ただdpの時も場合によってはCounter使えるという知見を得た
from collections import Counter

N, A = map(int, input().split(" "))
X = list(map(int, input().split(" ")))

X = [x-A for x in X]

c = Counter([0])
for x in X:
    d = Counter()
    for k, v in c.items():
        d[k+x] += v
    c += d

print(c[0]-1)

################################

# N, A = map(int, input().split(" "))
# X = list(map(int, input().split(" ")))

# dp = [[[0 for _ in range(N+1)] for _ in range(N*A+1)] for i in range(N+1)]
# dp[0][0][0] = 1

# for i in range(N):

################################

# # DPだよわからないよおおおお
# from functools import lru_cache

# N, A = map(int, input().split(" "))
# X = list(map(int, input().split(" ")))

# X = [x-A for x in X]

# @lru_cache(maxsize=None)
# def dfs(n)