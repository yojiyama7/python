n = int(input())
a = tuple(map(int, input().split(" ")))

a_count = dict()
for a_i in a:
	if a_i not in a_count:
		a_count[a_i] = 0 
	a_count[a_i] += 1

sum_num = 0
for a_i in a_count:
	a_count_a_i = a_count[a_i]
	sum_num += a_count_a_i - a_i if a_i <= a_count_a_i else a_count_a_i
print(sum_num)