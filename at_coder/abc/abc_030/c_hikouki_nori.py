import bisect

n, m = map(int, input().split(" "))
x, y = map(int, input().split(" "))
a, b = [tuple(map(int, input().split(" "))) for _ in range(2)]

now_time = 0
count = 0
while True:
	next_flight_index = bisect.bisect_left([a, b][count%2], now_time)
	if next_flight_index < [n, m][count%2]:
		now_time = [a, b][count%2][next_flight_index]
	else:
		break
	now_time += [x, y][count%2]
	count += 1

print(count//2)