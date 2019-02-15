n, a, b = [int(n) for n in input().split(" ")]

some_sum = 0
for i in range(1, n+1):
	digit_sum = sum([int(m) for m in str(i)])
	if a <= digit_sum and digit_sum <= b:
		some_sum += i

print(some_sum)