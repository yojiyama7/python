from itertools import chain
from collections import Counter

AB = [list(map(int, input().split(" "))) for _ in range(3)]


print(["NO", "YES"][sum([m%2 for m in Counter(chain(*AB)).values()]) in [0, 2]])