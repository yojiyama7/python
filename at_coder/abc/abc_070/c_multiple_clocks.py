def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd(a, b)

n = int(input())
t = [int(input()) for i in range(n)]

ans = t[0]
for t_i in t[1:]:
	ans = lcm(ans, t_i)

print(ans)