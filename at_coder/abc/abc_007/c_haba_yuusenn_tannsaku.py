from collections import deque
 
INF = 10**5
ADS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
 
h, w = map(int, input().split(" "))
s_pos, g_pos = [tuple(map(lambda x: int(x)-1, input().split(" ")))[::-1] for _ in range(2)]
c = [list(input()) for _ in range(h)]
 
l = [[INF for _ in range(w)] for _ in range(h)]
l[s_pos[1]][s_pos[0]] = 0
q = deque([s_pos])
while q:
	this_x, this_y = q.popleft()
	if (this_x, this_y) == g_pos:
		break
	this_num = l[this_y][this_x]
	
	for ad_x, ad_y in ADS:
		x, y = this_x+ad_x, this_y+ad_y
		if not (0 <= x < w and 0 <= y < h):
			continue
		
		square = c[y][x]
		if not (square == "."):
			continue
		
		l[y][x] = this_num + 1
		q.append((x, y))
		c[y][x] = "#"
		
# [print(l_i) for l_i in l]
print(l[this_y][this_x])