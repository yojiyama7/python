def get_adjacent(lists, pos, hw):
	h, w = hw
	x, y = pos
	adjacents = []
	for adjust_y, adjust_x in ((0, 1), (1, 0), (0, -1), (-1, 0)):
		if 0 <= y+adjust_y < h and 0 <= x+adjust_x < w:
			adjacents.append(lists[y+adjust_y][x+adjust_x])
	return adjacents

h, w = map(int, input().split(" "))
s = [input() for i in range(h)]

for y in range(h):
	for x in range(w):
		if s[y][x] == "#":
			if "#" not in get_adjacent(s, (x, y), (h, w)):
				print("No")
				exit()
print("Yes")
