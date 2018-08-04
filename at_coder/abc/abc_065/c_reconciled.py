import math

n, m = map(int, input().split(" "))

remain = abs(n-m)
if remain <= 1:
	print((math.factorial(n) * math.factorial(m) * (2 if remain==0 else 1)) % (10**9+7))
else:
	print(0)