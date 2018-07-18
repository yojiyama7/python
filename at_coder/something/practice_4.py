a, b, c, x = [int(input()) for i in range(4)]

can_count = 0

for i in range(a+1):
	coins_price_500 = i * 500
	for j in range(b+1):
		coins_price_100 = j * 100
		for k in range(c+1):
			coins_price_50 = k * 50
			if x == coins_price_500 + coins_price_100 + coins_price_50:
				can_count += 1

print(can_count)