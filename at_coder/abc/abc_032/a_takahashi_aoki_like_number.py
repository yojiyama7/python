a, b, n = [int(input()) for i in range(3)]

num = n
while True:
	if num % a == num % b == 0:
		break
	else:
		num += 1
print(num)