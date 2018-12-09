from collections import deque
from itertools import chain

ADS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

h, w = map(int, input().split(" "))
s = [list(input()) for _ in range(h)]

l = [[None for _ in range(w)] for _ in range(h)]
l[0][0] = 0

q = deque([(0, 0)])
while q:
	this_x, this_y = q.popleft()
	this_num = l[this_y][this_x]
	if (this_x, this_y) == (w-1, h-1):
		# [print(" ".join(str(l_j).rjust(2) if l_j != None else "  " for l_j in l_i)) for l_i in l]
		print(sum(s_i.count(".") for s_i in s) - l[h-1][w-1] - 1)
		exit()

	for ad_x, ad_y in ADS:
		x, y = this_x+ad_x, this_y+ad_y
		if not (0 <= x < w and 0 <= y < h):
			continue
		
		square = s[y][x]
		if square == "#":
			continue

		num = l[y][x]
		if num != None:
			continue
		l[y][x] = this_num + 1

		q.append((x, y))

print(-1)

################################

# from collections import deque
# from itertools import chain
# ads = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# h, w = map(int, input().split(" "))
# s = [list(input()) for _ in range(h)]

# def find_shortest(m):
# 	q = deque([(0, 0)])
# 	i = 0
# 	while q:
# 		for j in range(len(q)):
# 			this_x, this_y = q.popleft()
# 			# this_square = m[this_y][this_x]
# 			if (this_x, this_y) == (w-1, h-1):
# 				return i
# 			m[this_y][this_x] = i

# 			for ad_x, ad_y in ads:
# 				x, y = this_x+ad_x, this_y+ad_y
# 				if not (0 <= x < w and 0 <= y < h):
# 					continue
				
# 				square = m[y][x]
# 				if square == "#" or type(square) == int:
# 					continue

# 				q.append((x, y))
# 				m[y][x] = "#"
# 		i += 1
# 	return None


# white_num = "".join(chain(*s)).count(".")
# shortest_lenght = find_shortest(s)
# if shortest_lenght:
# 	print(white_num - 1 - shortest_lenght)
# else:
# 	print(-1)

# # しろます - 1 - 最短ルートの長さ