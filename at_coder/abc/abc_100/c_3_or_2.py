def count_two(n):
	two = 0
	while n%2 == 0:
		n //= 2
		two += 1
	return two

n = int(input())
a = [int(m) for m in input().split(" ")]

print(sum([count_two(a_n) for a_n in a]))