# これがヒントになるんだろうけど
# https://beta.atcoder.jp/contests/abc015/submissions/2740759

W = int(input())
N, K = map(int, input().split(" "))
width, value = zip(*(map(int, input().split(" ")) for _ in range(N)))



################################
#---#---#---#---#---#---#---#---
################################

# # TLE

# W = int(input())
# N, K = map(int, input().split(" "))
# weight, value = zip(*[list(map(int, input().split(" "))) for _ in range(N)])

# dp = [[[0 for _ in range(K+1)] for _ in range(W+1)] for _ in range(N+1)]

# for i in range(1, N+1):
#     for w in range(1, W+1):
#         for k in range(1, K+1):
#             if weight[i-1] <= w:
#                 dp[i][w][k] = max([
#                     dp[i-1][w-weight[i-1]][k-1] + value[i-1],
#                     dp[i-1][w][k]
#                 ])
#             else:
#                 dp[i][w][k] = dp[i-1][w][k]

# print(dp[N][W][K])
# # [print([print(dp_j) for dp_j in dp_i]) for dp_i in dp]

################################

# w = int(input())
# n, k = map(int, input().split(" "))
# width, value = zip(*(list(map(int, input().split(" "))) for _ in range(n)))

# memo = [[[0 for _ in range(k+1)] for _ in range(w+1)] for _ in range(n)]
# is_memo = [[[False for _ in range(k+1)] for _ in range(w+1)] for _ in range(n)]
# def dfs(now, used_w, used_count):
#     if used_count >= k:
#         return 
#     elif is_memo == False:
#         if used_w+width[now] <= w:
#             memo[now][used_w][used_count] = max()  

################################

# 部分的にWA 原因不明

# w = int(input())
# n, k = map(int, input().split(" "))
# width, value = zip(*(list(map(int, input().split(" "))) for _ in range(n)))

# width, value = [0]+list(width), [0]+list(value)

# memo = [[0 for _ in range(w+1)] for _ in range(n+1)]
# is_memo = [[False for _ in range(w+1)] for _ in range(n+1)]
# def dfs(num, width_limit, num_limit):
#     if 0 in [num, num_limit]:
#         return 0
#     if is_memo[num][width_limit] == False:
#         if width[num] <= width_limit:
#             memo[num][width_limit] = max([
#                 dfs(num-1, width_limit-width[num], num_limit-1)+value[num],
#                 dfs(num-1, width_limit, num_limit)
#             ])
#         else:
#             memo[num][width_limit] = dfs(num-1, width_limit, num_limit)
#     is_memo[num][width_limit] = True
#     return memo[num][width_limit]

# print(dfs(n, w, k))
# [print(memo_i) for memo_i in memo]