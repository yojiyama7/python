n, t = map(int, input().split(" "))
ct = [tuple(map(int, input().split(" "))) for _ in range(n)]

filtered = tuple(filter(lambda x: x[1] <= t, ct))
if len(filtered) != 0:
	print(min(map(lambda x: x[0], filtered)))
else:
	print("TLE")