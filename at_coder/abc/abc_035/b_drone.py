s = input()
t = int(input())

l, r, u, d, unknown = [s.count(c) for c in "LRUD?"]
distance = abs(r-l) + abs(u-d)
if t==1:
	print(distance + unknown)
else:
	print(max(distance - unknown, (distance - unknown)%2))