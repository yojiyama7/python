N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

l, r = 0, 0
sum_num = A[0]
point = 0
while r < N:
    # print(l, r, sum_num, point)
    if sum_num >= K:
        point += N-r
        sum_num -= A[l]
        l += 1
    else:
        r += 1
        if r < N:
            sum_num += A[r]

print(point)

################################

# l, r = 0, 0
# sum_num = 0
# point = 0
# while r < N:
#     if sum_num < K:
#         sum_num += A[r]
#         r += 1
#     else:
#         point += N-r+1
#         print(point, N, r)
#         sum_num -= A[l]
#         l += 1

# print(point)    

################################

# A += [0]

# r = -1
# sum_num = 0
# point = 0
# for l in range(N):
#     sum_num -= A[l-1]
#     if r < l and l != 0:
#         r = l
#     while sum_num < K:
#         r += 1
#         if r == N:
#             print(point)
#             exit()
#         sum_num += A[r]
#     point += N-r

