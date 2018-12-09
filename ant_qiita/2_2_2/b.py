n, m = map(int, input().split(" "))
ab = [list(map(int, input().split(" "))) for _ in range(m)]

ab.sort(key=lambda x: x[1])

count = 0
before = 0
for a_i, b_i in ab:
	if before > a_i:
		continue
	before = b_i
	count += 1

print(count)

################################

# n, m = map(int, input().split(" "))
# ab = [list(map(int, input().split(" "))) for _ in range(m)]

# # こうすると、ある範囲において、一番右(西)側に橋をかけることが一番要望を解決できる
# ab.sort(key=lambda x: x[1])

# count = 0
# x = 0
# for a_i, b_i in ab:
# 	if a_i <= x < b_i:
# 		continue
# 	x = b_i-1
# 	count += 1

# print(count)