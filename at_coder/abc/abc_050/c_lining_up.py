# 条件のために 1のカウント or 0のカウント を 2 にしているので最適解はありそう

from collections import Counter

n = int(input())
a = tuple(map(int, input().split(" ")))
# n = 10000
# a = tuple(sum([[i, i] for i in range(1, n+1, 2)], [])[:n])

a_counter = Counter(a)
a_counter[int(n%2==0)] = 2

if set(a_counter.values()) == {2}:
    print((2 ** (n//2)) % (10**9+7))
else:
    print(0)