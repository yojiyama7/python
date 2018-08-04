n = int(input())
a = list(map(int, input().split(" ")))

a_list = [a_i-i for a_i in a for i in range(-1, 2)]

d = dict()
for a_i in a_list:
	if a_i not in d:
		d[a_i] = 0
	d[a_i] += 1

print(max(d.values()))