from functools import lru_cache
import sys

sys.setrecursionlimit(10**8)

N = int(input())
ABC = [list(map(int, input().split(" "))) for _ in range(N)]

l = [[None for _ in range(3)] for _ in range(N+10)]
# @lru_cache(maxsize=(N+10)*3)
def dp(i, use):
    if i == -1:
        return 0
    if l[i][use] != None:
        return l[i][use]
    max_num = 0
    for k in range(3):
        if k == use:
            continue
        max_num = max(max_num, dp(i-1, k)+ABC[i][use])
    l[i][use] = max_num 
    return max_num

print(max(dp(N-1, m) for m in range(3)))
