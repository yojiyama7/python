n, s, t = map(int, input().split(" "))
w = int(input())
a = [int(input()) for i in range(n-1)]

weight = 0
best_count = 0
for a_i in [w] + a:
	weight += a_i
	if s <= weight <= t:
		best_count += 1
print(best_count)