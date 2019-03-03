# やった！！！とけたぜええええ！！！！！

from collections import deque
from copy import deepcopy

ADS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

h, w, n = map(int, input().split(" "))
m = [list(input()) for _ in range(h)]
l = None

def find_shortest(pos, g_char):
	l = [[None for _ in range(w)] for _ in range(h)]
	l[pos[1]][pos[0]] = 0
	# print(pos, g_char)
	return bfs(l, pos, g_char)

def bfs(l, s_pos, g_char):
	q = deque([pos])
	while q:
		this_x, this_y = q.popleft()
		this_square = m[this_y][this_x]
		this_num = l[this_y][this_x]
		if this_square == g_char:
			# [print(l_i) for l_i in l]
			return (this_num, (this_x, this_y))
		
		for ad_x, ad_y in ADS:
			x, y = this_x+ad_x, this_y+ad_y
			if not (0 <= x < w and 0 <= y < h):
				continue
			
			square = m[y][x]
			if square == "X":
				continue
			
			num = l[y][x]
			if num != None:
				continue
			l[y][x] = this_num + 1
			q.append((x, y))
	
for y, line in enumerate(m):
	if "S" in line:
		pos = (line.index("S"), y)

sum_num = 0
for i in range(n):
	num, pos = find_shortest(pos, str(i+1))
	# print(i+1, num, pos)
	sum_num += num
print(sum_num)

################################

# # TLE わがんね

# import copy
# from collections import deque

# ads = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# h, w, n = map(int, input().split(" "))
# c = [list(input()) for _ in range(h)]

# def find_shortest(m, s_pos, g_char):
# 	# print(s_pos, g_char)
# 	q = deque([s_pos])
# 	i = 1
# 	while q:
# 		for j in range(len(q)):
# 			this_x, this_y = q.popleft()
# 			this_square = m[this_y][this_x]
# 			if this_square[0] == g_char:
# 				g_pos = (this_x, this_y)
# 				break

# 			for ad_x, ad_y in ads:
# 				x, y = this_x+ad_x, this_y+ad_y
# 				if not (0 <= x < w and 0 <= y < h):
# 					continue
				
# 				square = m[y][x]
# 				if square[1]:
# 					continue
# 				elif square[0] == "X":
# 					continue
# 				q.append((x, y))
# 				m[y][x][1] = i
# 		i += 1
# 		# [print(m_i) for m_i in m]
	
# 	return (m[g_pos[1]][g_pos[0]][1], g_pos)

# for y, line in enumerate(c):
# 	if "S" in line:
# 		x = line.index("S")
# 		s_pos = (x, y)
# 		c[y][x] = "0"
# c = [[[square, None] for square in c_i] for c_i in c]
# c[s_pos[1]][s_pos[0]][1] = 0
# # print(find_shortest(c, s_pos, "1"))

# sum_num = 0
# for i in range(n):
# 	# i -> i+1
# 	c2 = copy.deepcopy(c)
# 	length, g_pos = find_shortest(c2, s_pos, str(i+1))
# 	# print(i, length, g_pos)
# 	sum_num += length

# 	s_pos = g_pos

# print(sum_num)