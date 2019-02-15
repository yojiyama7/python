# from bisect import bisect_left

# L, N = map(int, input().split(" "))
# X = [int(input()) for _ in range(N)]

# m = 0
# for i in range(N):
#     a = bisect_left(m, X)
#     b = (m-X[a-1], m-(L-X[a-1]))
#     c = X[a]-m
#     if b > c

################################

# Y = [x for x in X]

# sum_num1 = 0
# for i in range(N):
#     if i%2==0:
#         sum_num1 += X.pop(0)*2    
#     else:
#         sum_num1 += (L-X.pop())*2
#     print(sum_num1)

# # print(X, Y)

# sum_num2 = 0
# for i in range(N):
#     if i%2==0:
#         sum_num2 += (L-Y.pop())*2
#     else:
#         sum_num2 += Y.pop(0)*2 
#     print(sum_num2)

# # print(sum_num)