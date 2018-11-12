n, m = map(int, input().split(" "))
ab = [list(map(int, input().split(" "))) for _ in range(m)]

d = dict(zip(range(1, n+1), [set() for _ in range(n)]))
for ab_i in ab:
	a_i, b_i = ab_i
	d[a_i].add(b_i)
	d[b_i].add(a_i)

for i in range(1, n+1):
	friends = d[i]
	friends_of_friends = set()
	for friend in friends:
		friends_of_friends |= d[friend]
	friends_of_friends -= friends | {i} 
	print(len(friends_of_friends))