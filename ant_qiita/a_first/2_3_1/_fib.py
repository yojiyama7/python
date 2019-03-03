import sys
sys.setrecursionlimit(10**8)

n = int(input())

is_memo = [False]*(n+1)
memo = [None]*(n+1)
def fib(m):
	if m <= 1:
		return 1
	if is_memo[m]:
		return memo[m]

	result = memo[m] = fib(m-1) + fib(m-2)
	is_memo[m] = True
	return result

print(fib(n))

# ################################

# # 100で無理

# import sys
# sys.setrecursionlimit(10**8)

# n = int(input())

# def fib(m):
# 	if m <= 1:
# 		return 1
	
# 	return fib(m-1) + fib(m-2)

# print(fib(n))