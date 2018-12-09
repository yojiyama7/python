# なぜこれに？ ナップサックと違って1次元なのは？
# 個数の最小化
# dp[i] = min(dp[i], dp[i-coin]+1)

BIG_NUM = 10**9

n, m = map(int, input().split(" "))
c = list(map(int, input().split(" ")))

l = [BIG_NUM] * (n+1)
l[0] = 0

for c_i in c:
	for j in range(1, n+1):
		if j < c_i:
			continue
		l[j] = min(l[j-c_i]+1, l[j])

	# print(l)
print(l[n])

# n, m = map(int, input().split(" "))
# c = list(map(int, input().split(" ")))

# INF = 10**9

# c = [0] + c
# c.sort()

# l = dict(zip(c, [[0]+[INF for _ in range(n)] for _ in range(m+1)]))

# for i in range(m):
# 	for j in range(1, n+1):
# 		coin = c[i+1]
# 		# print(i, j, c[i+1])
# 		l[coin][j] = min(j//coin + l[c[i]][j%coin], l[c[i]][j])
# 		# print(c[i], j, l[i+1][j])

# [print(c_i, l[c_i]) for c_i in c]
# print(l[c[m]][n])

################################

# # DPわからん、、、

# n, m = map(int, input().split(" "))
# c = list(map(int, input().split(" ")))

