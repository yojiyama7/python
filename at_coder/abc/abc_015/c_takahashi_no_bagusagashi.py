from itertools import product

n, k = map(int, input().split(" "))
t = [tuple(map(int, input().split(" "))) for _ in range(n)]

for t_i in product(*t):
	xor_result = 0
	for t_j in t_i:
		xor_result ^= t_j
	if xor_result == 0:
		print("Found")
		exit()

print("Nothing")