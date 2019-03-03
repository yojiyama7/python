# はぁ わからん。
# きた、わかった
from fractions import gcd
# pythonバージョン違い
# from math import gcd
from functools import lru_cache

N, D = map(int, input().split(" "))

@lru_cache(maxsize=None)
def dfs(n, d):
	# print(n, d)
	if d == 1:
		return 1
	elif n == 0:
		return 0
	s = sum(dfs(n-1, d//gcd(d, i)) for i in range(1, 7))
	# print(s)
	return s / 6

print(dfs(N, D))