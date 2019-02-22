# # not submit

# from itertools import chain, zip_longest

# L, N = map(int, input().split(" "))
# X = [int(input()) for _ in range(N)]

# zip_chain = lambda a, b: list(chain(*zip_longest(a, b)))
# def remove_all(a, x):
#     while x in a:
#         a.remove(x)
#     return a
# # print(X[::2], X[1::2])

# l1 = zip_chain((L-x for x in X[::2]), X[1::2])
# l2 = zip_chain(X[::-2], (L-x for x in X[-1::-2]))

# l1, l2 = [remove_all(l_i, None) for l_i in [l1, l2]]

# print(l1, l2)

# a1 = l1[0] + 2*sum(l1[1:-1]) + l1[-1]
# a2 = l2[0] + 2*sum(l2[1:-1]) + l1[-1]

# print(max(a1, a2))

################################

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