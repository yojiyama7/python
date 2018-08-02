x, y = map(int, input().split(" "))

n = x
count = 0
while n <= y:
	n *= 2
	count += 1
print(count)