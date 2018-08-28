from bisect import bisect_left, bisect_right

n, k = map(int, input().split(" "))
x = list(map(int, input().split(" ")))

zero_left = bisect_left(x, 0)
zero_right = bisect_right(x, 0)
m = x[:zero_left]
p = x[zero_right:]
zero_count = zero_right - zero_left
k -= zero_count
if k <= 0:
	print(0)
	exit()

y = m[-k:] + p[:k]
min_time = 1000000000000000000000000
for i in range(len(y)-k+1):
	l, r = y[i], y[i+k-1]
	time = r-l + min(abs(l), abs(r))
	if time < min_time:
		min_time = time

print(min_time)