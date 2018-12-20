# ここまで至れなかったぜ、、、 is_printedを覚えた(学んだ)。
N, M = map(int, input().split(" "))
A = [int(input()) for _ in range(M)]

A_is_printed = [False]*(N+1)
for a in A[::-1]:
    if A_is_printed[a] == False:
        print(a)
        A_is_printed[a] = True
for i in range(1, N+1):
    if A_is_printed[i] == False:
        print(i)

################################
#-------------------------------
################################

# N, M = map(int, input().split(" "))
# A = [int(input()) for _ in range(M)]

# s = list(range(1, N+1))
# b = []
# for a in A[::-1]:
#     if a in s:
#         s.remove(a)
#         b.append(a)

# for b_i in b+s:
#     print(b_i)