# DPはじめて解けた感(まあ1次元だけど)
import sys

sys.setrecursionlimit(10**8)

N = int(input())
A = list(map(int, input().split(" ")))

A = [A[0]] + A
memo = [None]*(N+1)
def dfs(n):
	if n <= 1:
		return 0
	if memo[n] == None:
		memo[n] = min(
			dfs(n-1) + abs(A[n]-A[n-1]),
			dfs(n-2) + abs(A[n]-A[n-2])
		)
	return memo[n]

print(dfs(N))	
# print(memo)