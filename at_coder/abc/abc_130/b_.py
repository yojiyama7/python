from itertools import accumulate
from bisect import bisect_right

N, X = map(int, input().split(" "))
L = list(map(int, input().split(" ")))

l = [0] + list(accumulate(L))
print(bisect_right(l, X))