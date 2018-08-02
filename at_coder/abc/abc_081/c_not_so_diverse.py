n, k = map(int, input().split(" "))

a = tuple(map(int, input().split(" ")))

a_count = dict()
for a_i in a:
	if a_i not in a_count:
		a_count[a_i] = 0
	a_count[a_i] += 1

print(sum(sorted(a_count.values())[:len(a_count)-k]))