def salary(n, d):
	if n in d:
		l = [salary(m, d) for m in d[n]]
		return min(l) + max(l) + 1
	else:
		return 1

n = int(input())
b = [int(input()) for _ in range(n-1)]

d = dict()
for i, b_i in enumerate(b):
	if b_i not in d:
		d[b_i] = []
	d[b_i].append(i+2)

print(salary(1, d))
