import sys

n, y = [int(m) for m in input().split(" ")]

for i in range(n+1):
	bill_10000 = 10000 * i
	for j in range(n-i+1):
		bill_5000 = 5000 * j
		k = n-i-j
		bill_1000 = 1000 * k
		
		sum_price = bill_10000 + bill_5000 + bill_1000
		# print(sum_price)
		# print(i, j, k, sum((i, j, k)))
		if y == sum_price:
			print(i, j, k)
			sys.exit()

print(-1, -1, -1)