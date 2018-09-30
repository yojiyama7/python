def gcd(a, b):
	if a > b:
		a, b = b, a
	while a:
		a, b = b%a, a
	return b

n, x = map(int, input().split(" "))
y = list(map(int, input().split(" ")))

y = [abs(y_i-x) for y_i in y]
m = y[0]
for y_i in y[1:]:
	m = gcd(m, y_i)
print(m)