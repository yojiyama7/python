from copy import deepcopy

ads = [(0, 1), (1, 0), (0, -1), (-1, 0)]

a = [list(input()) for _ in range(10)]
w, h = 10, 10

def is_connect(m, pos):
	m = deepcopy(m)
	dfs(m, pos)
	# print(m)
	for line in m:
		if "o" in line:
			return False
	return True

def dfs(m, pos):
	this_x, this_y = pos
	this_square = m[this_y][this_x]

	m[this_y][this_x] = "x"
	for ad_x, ad_y in ads:
		x, y = this_x+ad_x, this_y+ad_y
		if not (0 <= x < w and 0 <= y < h):
			continue
		square = m[y][x]
		if not (square == "o"):
			continue
		dfs(m, (x, y))

for y in range(h):
	for x in range(w):
		if a[y][x] == "o":
			continue
		if is_connect(a, (x, y)):
			print("YES")
			exit()
print("NO")

################################

# from itertools import chain
# import sys
# import copy

# ads = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# a = [list(input()) for _ in range(10)]

# def is_one_island(m, pos):
# 	def cant_move_map(pos):
# 		this_x, this_y = pos
# 		m[this_y][this_x] = "x"
# 		for i in range(4):
# 			ad_x, ad_y = ads[i]
# 			x, y = this_x+ad_x, this_y+ad_y
# 			if not (0 <= x < 10 and 0 <= y < 10):
# 				continue
# 			square = m[y][x]
# 			if square == "x":
# 				continue
# 			cant_move_map((x, y))
# 	cant_move_map(pos)
# 	return len(set(chain(*m))) == 1
		


# for y, a_i in enumerate(a):
# 	if "o" in a_i:
# 		x = a_i.index("o")
# 		start_pos = (x, y)

# for y in range(10):
# 	for x in range(10):
# 		if a[y][x] == "o":
# 			continue
# 		a_ = copy.deepcopy(a)
# 		a_[y][x] = "o"

# 		if is_one_island(a_, start_pos):
# 			print("YES")
# 			exit()

# print("NO")

################################
#---#---#---#---#---#---#---#---
################################

# def cant_move_map(m, pos):
# 	this_x, this_y = pos
# 	m[this_y][this_x] = "x"

# 	for i in range(4):
# 		ad_x, ad_y = ads[i]
# 		x, y = this_x+ad_x, this_y+ad_y
# 		if not (0 <= x < 10 and 0 <= y < 10):
# 			continue
		
# 		square = m[y][x]
# 		if square == "x":
# 			continue
# 		m = cant_move_map(m, (x, y))
# 	return m

# for y, a_i in enumerate(a):
# 	if "o" in a_i:
# 		x = a_i.index("o")
# 		start_pos = (x, y)

# for y in range(10):
# 	for x in range(10):
# 		if a[y][x] == "o":
# 			continue

# 		a[y][x] = "o"
# 		if len(set(chain(*cant_move_map(a, start_pos)))) == 1:
# 			print("YES")
# 			exit()
# 		a[y][x] = "x"

# print("NO")

################################

# for y, a_i in enumerate(a):
# 	if "o" in a_i:
# 		x = a_i.index("o")
# 		start_pos = (x, y)

# find_road(a, pos)	
