# イマイチ理解できてない希ガス？
A, B, C, D, E, F = map(int, input().split(" "))

# 900
water = set()
for a in range(F//(100*A)+1):
	for b in range(F//(100*B)+1):
		w = A*a + B*b
		if w > F//100:
			break
		water.add(w)
water.remove(0)

suger = set()
for c in range(F//C+1):
	for d in range(F//D+1):
		s = C*c + D*d
		if s > F:
			break
		suger.add(s)

# print(water, suger)

max_num = 0
max_w, max_s = A, 0
for w in water:
	for s in suger:
		if 100*w+s > F or s > E*w:
			continue
		# print(w*100, s)
		if max_num < s/w:
			max_num = s/w
			max_w, max_s = w, s

print(100*max_w+max_s, max_s)
		
