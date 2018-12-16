from itertools import accumulate
n = int(input())
ab = [tuple(map(int, input().split(" "))) for _ in range(n)]

l = [0]*1000002
for a_i, b_i in ab:
	l[a_i] += 1
	l[b_i+1] -= 1

print(max(accumulate(l)))