################################
#-------------------------------
################################

# N, X = map(int, input().split(" "))

# memo = [None]*(N+1)
# def dfs(l):
# 	if l == 0:
# 		return "P"
# 	if memo[l] == None:
# 		b = dfs(l-1)
# 		memo[l] = "B"+b+"P"+b+"B"
# 	return memo[l]

# print(dfs(N)[:X].count("P"))