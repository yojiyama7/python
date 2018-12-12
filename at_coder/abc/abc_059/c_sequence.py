N = int(input())
A = tuple(map(int, input().split(" ")))

m = 0
c = 0
for i in range(N):
	m += A[i]
	# print(m)
	if i%2 == 0:
		if m <= 0:
			c += abs(m)+1
			m += abs(m)+1
	else:
		if m >= 0:
			c += m+1
			m -= m+1
	# print(m, c)
# print(c)

m = 0
d = 0
for i in range(N):
	m += A[i]
	# print(m)
	if i%2 == 1:
		if m <= 0:
			d += abs(m)+1
			m += abs(m)+1
	else:
		if m >= 0:
			d += m+1
			m -= m+1
	# print(m, d)

print(min(c, d))