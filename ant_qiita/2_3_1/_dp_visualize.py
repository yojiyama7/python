# 動きを可視化したい。

class ColorValue:
	def __init__(num, color="BLACK"):



def visualize(n, w, dp, square_size=3):
	print(" "*(square_size+1) + " ".join(map(lambda x: str(x).rjust(square_size), range(w+1))))

n, w = map(int, input().split(" "))
value, weight = zip(*[list(map(int, input().split(" "))) for _ in range(n)])

dp = [[0 for _ in range(w+1)] for _ in range(n+1)]

for i in range(n):
	for j in range(1, w+1):
		if weight[i] <= j:
			dp[i+1][j] = max(dp[i][j-weight[i]]+value[i], dp[i][j])
		else:
			dp[i+1][j] = dp[i][j]

visualize(n, w, dp, square_size=2)

# print(" "*3+"".join(map(lambda x: str(x).rjust(3), range(w+1))))
# [print(dp_i) for dp_i in dp]
# print(dp[n][w])