from itertools import product

n = int(input())

for pattern in product('abc', repeat=n):
	print("".join(pattern))