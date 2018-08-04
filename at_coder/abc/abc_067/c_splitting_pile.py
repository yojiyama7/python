n = int(input())
a = tuple(map(int, input().split(" ")))

x, y = 0, sum(a)
min_num = 10000000000000
for a_i in a[:-1]:
	x += a_i
	y -= a_i
	tmp = abs(x-y)
	if tmp < min_num:
		min_num = tmp
print(min_num)

