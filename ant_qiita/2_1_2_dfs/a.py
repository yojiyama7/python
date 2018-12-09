import sys

sys.setrecursionlimit(10**9)

h, w = map(int, input().split(" "))
c = [list(input()) for _ in range(h)]

ads = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for y, c_i in enumerate(c):
	if "s" in c_i:
		s_pos = (c_i.index("s"), y)
	# if "g" in c_i:
	# 	g_pos = (c_i.index("g"), y)
# l = [[None for _ in range(w)] for _ in range(h)]
# l[s_pos[1]][s_pos[0]] = 0
l = [[0 for _ in range(w)] for _ in range(h)]

def dfs(pos):
	this_x, this_y = pos
	this_square = c[this_y][this_x]
	this_num = l[this_y][this_x]
	if this_square == "g":
		return True

	c[this_y][this_x] = "#"
	# [print("".join(c_i)) for c_i in c]
	# print("---")
	for ad_x, ad_y in ads:
		x, y = this_x+ad_x, this_y+ad_y
		if not (0 <= x < w and 0 <= y < h):
			continue
		square = c[y][x]
		if square == "#":
			continue
		l[y][x] = this_num + 1
		if dfs((x, y)):
			return True
	
	return False

print("Yes" if dfs(s_pos) else "No")

################################

# import sys
 
# sys.setrecursionlimit(1000000000)
 
# h, w = map(int, input().split(" "))
# c = [list(input()) for _ in range(h)]
 
# ad_xs, ad_ys = [0, 0, -1, 1], [1, -1, 0, 0]
 
# def find_road(pos):
# 	this_x, this_y = pos
# 	c[this_y][this_x] = "#"
 
# 	for i in range(4):
# 		x, y = this_x+ad_xs[i], this_y+ad_ys[i]
# 		if not (0 <= x < w and 0 <= y < h):
# 			continue
# 		select = c[y][x]
# 		if select == "#":
# 			continue
# 		elif select == "g":
# 			return True
# 		elif select == ".":
# 			if find_road((x, y)):
# 				return True
# 	return False
 
# for y, line in enumerate(c):
# 	if "s" in line:
# 		x = line.index("s")
# 		start_pos = (x, y)
 
# print("Yes" if find_road(start_pos) else "No")