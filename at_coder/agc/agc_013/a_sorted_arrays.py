# 傾きの正負の変化を調べるのに、
# AとB(傾き)をかけてその符号を見るという方法があると気づいた
N = int(input())
A = list(map(int, input().split(" ")))

c = 1
e = 0
for i in range(N-1):
    d = A[i+1]-A[i]
    # print(d, e, e*d < 0)
    # 一方が負の数、もう一方が正の数なら
    if e*d < 0:
        c += 1
        e = 0
    elif d != 0: # この条件忘れていた
        e = d

print(c)

################################

# # TLE

# from itertools import groupby

# N = int(input())
# A = list(map(int, input().split(" ")))

# b = [A[i+1]-A[i] for i in range(N-1)]

# for i in range(b.count(0)):
#     b.remove(0)

# b = [0<b_i for b_i in b]

# b = [len(list(v)) for k, v in groupby(b)]

# # print(b)
# if len(b) <= 1:
#     print(1)
#     exit()

# c = 2
# can_remove = True
# for b_i in b[1:-1]:
#     if b_i == 1 and can_remove:
#         can_remove = False
#     else:
#         c += 1
#         can_remove = True

# print(c)