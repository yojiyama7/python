def S(n):
	return sum([int(m) for m in str(n)])

n = int(input())

print("Yes" if n%S(n) == 0 else "No")