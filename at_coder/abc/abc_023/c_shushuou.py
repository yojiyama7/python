from collections import Counter

r, c, k = map(int, input().split(" "))
n = int(input())
rc = [tuple(map(int, input().split(" "))) for _ in range(n)]

lines = [0]*r
columns = [0]*c

for rc_i in rc:
	r_i, c_i = rc_i
	lines[r_i-1] += 1
	columns[c_i-1] += 1

lines_counter = Counter(lines)
columns_counter = Counter(columns)

sum_num = 0
for line_size, line_count in lines_counter.items():
	sum_num += columns_counter[k - line_size] * line_count

for rc_i in rc:
	r_i, c_i = rc_i
	square = lines[r_i-1] + columns[c_i-1]
	if k == square:
		sum_num -= 1
	elif k+1 == square:
		sum_num += 1

print(sum_num)