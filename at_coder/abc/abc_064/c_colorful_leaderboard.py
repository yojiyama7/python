n = int(input())
a = map(int, input().split(" "))

color_types = [False]*8
pro_count = 0
for a_i in a:
	if a_i < 3200:
		color_types[a_i//400] = 1
	else:
		pro_count += 1
print(max(1, sum(color_types)), sum(color_types)+pro_count)