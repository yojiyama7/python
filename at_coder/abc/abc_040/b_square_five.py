n = int(input())

if n == 1:
	print(0)
	exit()

min_remain = 10**6
for n_i in range(1, n):
	remain = abs(n//n_i - n_i) + n%n_i
	if remain < min_remain:
		min_remain = remain
print(min_remain)