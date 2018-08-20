import math

n = int(input())
t_a = [tuple(map(int, input().split(" "))) for _ in range(n)]

now_t, now_a = t_a[0]
for t_i, a_i in t_a[1:]:
    if now_t/now_a < t_i/a_i:
        now_a = math.ceil(now_a/a_i) * a_i
        now_t = now_a // a_i * t_i
    elif now_t/now_a > t_i/a_i:
        now_t = math.ceil(now_t/t_i) * t_i
        now_a = now_t // t_i * a_i

print(now_t + now_a)