# sort や max だと重くなる

n = int(input())
a = list(map(int, input().split(" ")))

a.sort()
maxs = []
for i in range(2):
	max_1 = a.pop()
	while True:
		max_2 = a.pop()
		if max_1 == max_2:
			maxs.append(max_1)	
			break
		max_1 = max_2
		if len(a) == 0:
			print(0)
			exit()
print(maxs[0]*maxs[1])