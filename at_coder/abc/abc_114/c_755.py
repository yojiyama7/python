from bisect import bisect_right
from itertools import product, chain

N = int(input())

# product("357", repeat=len(str(N)))
l = list(chain(*[[int("".join(m)) for m in product("357", repeat=i) if set(m) == {"3", "5", "7"}] for i in range(1, len(str(N))+1)]))
# print(l)
print(bisect_right(l, N))

################################

# # TLE
# count = 0
# for i in range(1, N+1):
# 	if set(str(i)) != {"3", "5", "7"}:
# 		continue
# 	count += 1
# print(count)