s = input()
t = int(input())

# わからん

x, y, unknown = 0, 0, 0
for s_i in s:
	if s_i == "L":
		x -= 1
	elif s_i == "R":
		x += 1
	elif s_i == "U":
		y += 1
	elif s_i == "D":
		y -= 1
	elif s_i == "?":
		unknown += 1
print(abs(x)+abs(y) + (unknown if t == 1 else -unknown))
