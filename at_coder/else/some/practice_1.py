a, b = [int(n) for n in input().split(" ")]

if a % 2 == b % 2 == 1:
	print("Odd")
else:
	print("Even")