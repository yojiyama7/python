N = int(input())
X, Y, H = zip(*[tuple(map(int, input().split(" "))) for _ in range(N)])

for i in range(N):
	if H[i] <= 0:
		continue
	std = i
	break
# print(X[std], Y[std])
for cy in range(101):
	for cx in range(101):
		ch = H[std] + abs(cx-X[std]) + abs(cy-Y[std])
		flag = True
		for i in range(N):
			if max(0, ch - abs(cx-X[i]) - abs(cy-Y[i])) != H[i]:
				flag = False
				# break
			# print(ch, cx, cy, X[i], Y[i], ch - abs(cx-X[i]) - abs(cy-Y[i]), H[i])
		if flag:
			print(cx, cy, ch)
			exit()

			