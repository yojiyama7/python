n, k = map(int, input().split(" "))
ab = [tuple(map(int, input().split(" "))) for i in range(n)]

count = 0
for ab_num, ab_count in sorted(ab):
	count += ab_count
	if k <= count:
		print(ab_num)
		exit()