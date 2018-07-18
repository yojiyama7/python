def count_two(n):
	two_count = 0
	while n != 0 and n % 2 == 0:
		two_count += 1
		n //= 2
	return two_count

n = int(input())
a = map(int, input().split())
a_two_count_sum = sum([count_two(ai) for ai in a])
print(a_two_count_sum)