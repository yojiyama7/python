n = int(input())
xyh = [tuple(map(int, input().split(" "))) for _ in range(n)]

for cx in range(101):
	for cy in range(101):
		