from collections import deque

INF = 10**7
ADS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

h, w = map(int, input().split(" "))
c = [list(input()) for _ in range(h)]

for y, c_i in enumerate(c):
	if "s" in c_i:
		s_pos = (c_i.index("s"), y)
		break

l = [[INF for _ in range(w)] for _ in range(h)]
l[s_pos[1]][s_pos[0]] = 0

q = deque([s_pos])
while q:
	# print(l)
	this_x, this_y = q.popleft()
	this_square = c[this_y][this_x]
	this_num = l[this_y][this_x]
	if this_square == "g":
		break
	
	for ad_x, ad_y in ADS:
		x, y = this_x+ad_x, this_y+ad_y
		if not (0 <= x < w and 0 <= y < h):
			continue
		
		square = c[y][x]
		num = l[y][x]
		next_num = this_num+(square=="#")
		if num <= next_num:
			continue
		l[y][x] = next_num

		if square=="#":
			q.append((x, y))
		else:
			q.appendleft((x, y))

# [print(l_i) for l_i in l]
print("YES" if l[this_y][this_x] <= 2 else "NO")

################################

# h, w = map(int, input().split(" "))
# c = [list(input()) for _ in range(h)]

# # 0-1 bfs とは
# # 又 何故