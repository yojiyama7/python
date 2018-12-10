from itertools import accumulate

N = int(input())
A = list(map(int, input().split(" ")))

A = [0] + A + [0]
total_cost = sum(abs(A[i+1]-A[i]) for i in range(N+1))

one, two, three = [None] + A[:2]
for i in range(N):
	one, two, three = two, three, A[i+2]
	first, second = two-one, three-two
	cost_to_reduce = 0
	if (first < 0) != (second < 0):
		cost_to_reduce = min(abs(first), abs(second))*2
	print(total_cost - cost_to_reduce)
