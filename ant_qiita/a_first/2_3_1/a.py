

################################

# 4. メモ化再帰4

################################

# # 3. メモ化再帰3
# N, W = map(int, input().split(" "))
# value, weight = zip(*(map(int, input().split(" ")) for _ in range(N)))

# memo = [[None for _ in range(W+1)] for _ in range(N)]
# # [i(zero-base) < n]個目、ここからの重量w以下
# def dfs(n, w):
# 	if n == N:
# 		return 0
# 	if memo[n][w] == None:
# 		if weight[n] <= w:
# 			memo[n][w] = max(dfs(n+1, w), dfs(n+1, w-weight[n])+value[n])
# 		else:
# 			memo[n][w] = dfs(n+1, w)
# 	return memo[n][w]

# print(dfs(0, W))

################################

# # 3. メモ化再帰2
# N, W = map(int, input().split(" "))
# value, weight = zip(*(map(int, input().split(" ")) for _ in range(N)))

# memo = [[None for _ in range(W+1)] for _ in range(N+1)]
# # [i(zero-base) > n]個目、ここまでの重量w
# def dfs(n, w):
# 	if n == N:
# 		return 0
# 	if memo[n][w] == None:
# 		if w+weight[n] <= W:
# 			memo[n][w] = max(dfs(n+1, w), dfs(n+1, w+weight[n])+value[n])
# 		else:
# 			memo[n][w] = dfs(n+1, w)
# 	return memo[n][w]

# print(dfs(0, 0))

################################

# 1. メモ化再帰1
# N, W = map(int, input().split(" "))
# value, weight = zip(*(map(int, input().split(" ")) for _ in range(N)))

# memo = [[None for _ in range(W+1)] for _ in range(N+1)]
# # [i(one-base) <= n]個目、ここからの重量w以下
# def dfs(n, w):
# 	if n == 0:
# 		return 0
# 	if memo[n][w] == None:
# 		if weight[n-1] <= w:
# 			memo[n][w] = max(dfs(n-1, w), dfs(n-1, w-weight[n-1])+value[n-1])
# 		else:
# 			memo[n][w] = dfs(n-1, w)
# 	return memo[n][w]

# print(dfs(N, W))

####################################

# n, w = map(int, input().split(" "))
# value, weight = zip(*(map(int, input().split(" ")) for _ in range(n)))

# memo = [[None for _ in range(w+1)] for _ in range(n+1)]

# def dfs(num, t):
# 	if num == 0:
# 		return 0
# 	if memo[num][t] == None:
# 		if weight[num-1] <= t:
# 			memo[num][t] = max(dfs(num-1, t-weight[num-1])+value[num-1], dfs(num-1, t))
# 		else:
# 			memo[num][t] = dfs(num-1, t)
# 	return memo[num][t]

# print(dfs(n, w))
# [print(memo_i) for memo_i in memo]

################################

# n, w = map(int, input().split(" "))
# value, weight = zip(*[list(map(int, input().split(" "))) for _ in range(n)])

# dp = [[0 for _ in range(w+1)] for _ in range(n+1)]

# for i in range(n):
# 	for j in range(1, w+1):
# 		if weight[i] <= j:
# 			dp[i+1][j] = max(dp[i][j-weight[i]]+value[i], dp[i][j])
# 		else:
# 			dp[i+1][j] = dp[i][j]

# # [print(dp_i) for dp_i in dp]
# print(dp[n][w])

################################
#---#---#---#---#---#---#---#---
################################

# # 多分解けてる atcoderじゃない
# # 解けてない

# from copy import deepcopy

# n, W = map(int, input().split(" "))
# value, weight = zip(*[list(map(int, input().split(" "))) for _ in range(n)])

# dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
# for w in range(n+1):
# 	dp[0][w] = 0

# for i in range(n):
# 	for j in range(W+1):
# 		if j >= weight[i]:
# 			dp[i+1][j] = max(dp[i][j-weight[i]]+value[i], dp[i][j])
# 		else:
# 			dp[i+1][j] = dp[i][j]

# print(dp[n][W])

