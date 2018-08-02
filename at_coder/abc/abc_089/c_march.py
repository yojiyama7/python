n = int(input())
s = [input() for i in range(n)]

t = [[s_i[0] for s_i in s].count(c) for c in "MARCH"]

sum_num = 0
for i in range(5):
	t_dummy_i = list(tuple(t))
	i_num = t_dummy_i.pop(i)
	for j in range(4):
		t_dummy_j = list(tuple(t_dummy_i))
		j_num = t_dummy_j.pop(j)
		for k in range(3):
			sum_num += i_num * j_num * t_dummy_j[k]

print(sum_num//6)