n, m = map(int, input().split(" "))
ab = [tuple(map(int, input().split(" "))) for i in range(m)]

from_one, to_n = set(), set()
for ab_i in ab:
	if ab_i[0] == 1:
		from_one.add(ab_i[1])
	elif ab_i[1] == n:
		to_n.add(ab_i[0])
	
print("POSSIBLE" if from_one & to_n else "IMPOSSIBLE")