D, G = map(int, input().split(" "))
P, C = zip(*[map(int, input().split(" ")) for _ in range(D)])

sum_points = [100*(i+1)*P[i] + C[i] for i in range(D)]
# -1 で アクセスする時のため
P = list(P) + [0]
C = list(C) + [0]

min_num = 10**9
for i in range(1<<D):
	first_zero = -1
	point = 0
	q_count = 0
	for j in range(D-1, -1, -1):
		if (i>>j)%2 == 1:
			point += sum_points[j]
			q_count += P[j]
		elif first_zero == -1:
			first_zero = j
	# print(f"a: {point}, {q_count}")
	for j in range(P[first_zero]):
		if point >= G:
			min_num = min(min_num, q_count)
			break
		point += 100*(first_zero+1)
		q_count += 1
	point += C[first_zero]
	# print(f"b: {point}, {q_count}")
	if point >= G:
		min_num = min(min_num, q_count)

print(min_num)