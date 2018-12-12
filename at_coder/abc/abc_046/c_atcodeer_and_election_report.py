N = int(input())
TA = [list(map(int, input().split(" "))) for _ in range(N)]

n_t, n_a = 1, 1
for t, a in TA:
    # print(n_t/t, n_a/a)
    v = max(-(-n_t//t), -(-n_a//a))
    n_t, n_a = t*v, a*v

print(n_t+n_a)

################################
#-------------------------------
################################

# あってるはずなんだよなぁ math.ceilがわるいっぽい？
# import math

# N = int(input())
# TA = [list(map(int, input().split(" "))) for _ in range(N)]

# n_t, n_a = 1, 1
# for t, a in TA:
#     # print(n_t/t, n_a/a)
#     v = max(math.ceil(n_t/t), math.ceil(n_a/a))
#     n_t, n_a = t*v, a*v

# print(n_t+n_a)

################################

# N = int(input())
# TA = [list(map(int, input().split(" "))) for _ in range(N)]

# print("-")

# s_t, s_a = 1, 1 
# for t, a in TA:
#     v_t, v_a = 0, 0
#     while v_t < s_t or v_a < s_a:
#         v_t += t
#         v_a += a
#     s_t, s_a = v_t, v_a
#     # print(s_t, s_a)

# print(s_t+s_a)

################################

# import math

# n = int(input())
# t_a = [tuple(map(int, input().split(" "))) for _ in range(n)]

# now_t, now_a = t_a[0]
# for t_i, a_i in t_a[1:]:
#     if now_t/now_a < t_i/a_i:
#         now_a = math.ceil(now_a/a_i) * a_i
#         now_t = now_a // a_i * t_i
#     elif now_t/now_a > t_i/a_i:
#         now_t = math.ceil(now_t/t_i) * t_i
#         now_a = now_t // t_i * a_i

# print(now_t + now_a)