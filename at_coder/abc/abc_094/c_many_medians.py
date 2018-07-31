n = int(input())
x = list(map(int, input().split(" ")))

x_sorted = sorted(x)
for x_i in x:
	print((x_sorted[n//2-1], x_sorted[n//2])[x_i < x_sorted[n//2]])