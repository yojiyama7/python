n = int(input())
t = [int(input()) for _ in range(n)]

min_num = 10**4
for i in range(1<<n):
	ab = [[], []]
	for j in range(n):
		ab[(i>>j)%2].append(t[j])
	min_num = min(min_num, max(map(sum, ab)))	

print(min_num)

################################

# # bit全探索理解したい

# n = int(input())
# t = [int(input()) for _ in range(n)]

# min_num = 1000
# for i in range(1, 2**n):
# 	ab = [0, 0]
# 	for i, c in enumerate(bin(i)[2:].zfill(n)):
# 		ab[int(c)] += t[i]
# 	if max(ab) < min_num:
# 		min_num = max(ab)

# print(min_num)