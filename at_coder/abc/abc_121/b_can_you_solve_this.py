N, M, C = map(int, input().split(" "))
B = list(map(int, input().split(" ")))
A = [list(map(int, input().split(" "))) for _ in range(N)]

count = 0
for a in A:
    if sum(a_i*b_i for a_i, b_i in zip(a, B)) + C > 0:
        count += 1

print(count)

################################

# # kidai

# n, m, c = map(int, input().split())
# b_lis = list(map(int,input().split()))

# num = 0
# for i in range(n):
#     a_lis = list(map(int, input().split()))
#     to = 0
#     for s in range(m):
#         to += a_lis[s]*b_lis[s]
#     to += c
#     if to>0:
#         num += 1
# print(num)