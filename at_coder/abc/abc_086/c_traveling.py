n = int(input())
txy = [tuple(map(int, input().split(" "))) for i in range(n)]

# 間に合うかどうかの計算はどこ？
for txy_i in txy:
	t, x, y = txy_i
	remain = t - x - y
	if not (0 <= remain and remain % 2 == 0):
		print("No")
		exit()
print("Yes")