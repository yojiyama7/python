from itertools import chain
from collections import Counter

N, M = map(int, input().split(" "))
A = [list(map(int, input().split(" ")))[1:] for _ in range(N)]

print(sum(c==N for c in Counter(chain(*A)).values()))