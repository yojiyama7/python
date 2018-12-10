# かっこ良き
# https://beta.atcoder.jp/contests/abc099/submissions/2655797

from bisect import bisect_right
import sys
from functools import lru_cache

sys.setrecursionlimit(10**8)

N = int(input())

# Nの範囲に伴う累乗の範囲
# 1: inf
# 6: 1-6
# 9: 1-5

l = [6**i for i in range(1, 6+1)] + [9**i for i in range(1, 5+1)]
l.sort()

# print(l)

@lru_cache(maxsize=None)
def dfs(n):
	r = bisect_right(l, n)
	if r <= 0:
		return n
	min_num = 10**9
	for i in range(r):
		min_num = min(min_num, dfs(n-l[i])+1)
	return min_num

print(dfs(N))