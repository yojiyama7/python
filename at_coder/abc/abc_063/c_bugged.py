n = int(input())
a = [int(input()) for _ in range(n)]

sum_a = sum(a)

if sum_a % 10 == 0:
	can_nums = list(filter(lambda x: x%10 != 0, set(a)))
	if len(can_nums) == 0:
		print(0)
	else:
		print(sum_a - min(can_nums))
else:
	print(sum_a)