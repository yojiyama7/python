# https://beta.atcoder.jp/contests/abc032/submissions/3181449

################################
#-------------------------------
################################

# # WA TLE

# # from itertools import accumulate
# # from operator import mul

# N, K = map(int, input().split(" "))
# S = [int(input()) for _ in range(N)]

# if 0 in S:
#     print(N)
#     exit()

# max_num = 0
# m = 1
# j = 0
# for i in range(N):
#     # print(i, j, m, "a")
#     while (i > j) or (m <= K and j < N):
#         m *= S[j]
#         j += 1
#     max_num = max(max_num, j-i-2+1)
#     # print(m)
#     m //= S[i]
#     # print(i, j, m)

# print(max_num)

################################

# # わからん TLE

# n, k = map(int, input().split(" "))
# s = [int(input()) for _ in range(n)]

# if 0 in s:
#     print(n)
#     exit()

# products = [1]
# for s_i in s:
#     products.append(products[-1]*s_i)

# a, b, max_len = 0, 0, 0
# while b <= n:
#     if products[b] // products[a] <= k:
#         if b-a > max_len:
#             max_len = b-a
#         b += 1
#     else:
#         a += 1
#     b = a if b < a else b

# print(max_len)
