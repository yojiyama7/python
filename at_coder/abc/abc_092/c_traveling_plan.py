n = int(input())
a = tuple(map(int, input().split(" ")))

for n_i in range(n):
	a_dummy = list(a)
	a_dummy.pop(n_i)