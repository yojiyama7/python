n = int(input())

p = 1000-n
count = 0
for coin in [500, 100, 50, 10, 5, 1]:
	while p >= coin:
		p -= coin
		count += 1
print(count)

################################

# n = int(input())

# p = 1000-n
# count = 0
# for m in [500, 100, 50, 10, 5, 1]:
# 	while p >= m:
# 		p -= m
# 		count += 1

# print(count)