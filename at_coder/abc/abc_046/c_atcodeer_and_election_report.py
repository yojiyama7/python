import math

n = int(input())
t_a = [tuple(map(int, input().split(" "))) for _ in range(n)]

now_t, now_a = t_a[0]
for t_i, a_i in t_a[1:]:
	if now_t/now_a < t_i/a_i:
		one = math.ceil(now_a/a_i)
	else:
		one = math.ceil(now_t/t_i)
	now_a = one * a_i
	now_t = one * t_i

print(now_t + now_a)