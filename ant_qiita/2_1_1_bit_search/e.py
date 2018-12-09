n, m = map(int, input().split(" "))
xy = [list(map(int, input().split(" "))) for _ in range(m)]

l = [[False for _ in range(n+1)] for _ in range(n+1)]
for x_i, y_i in xy:
	l[x_i][y_i] = l[y_i][x_i] = True

max_num = 0

for i in range(1<<n):
	count = 0
	flag = True
	
	for j in range(n):
		if (i>>j)%2 == 0:
			continue
		count += 1

		for k in range(n):
			if (i>>k)%2 == 0:
				continue
			if l[j+1][k+1] or j==k:
				continue

			flag = False
			break
			
	if flag:
		max_num = max(max_num, count)
			
print(max_num)

################################

# bit全探索完全に理解した()

# from itertools import groupby

# n, m = map(int, input().split(" "))
# xy = [list(map(int, input().split(" "))) for _ in range(m)]

# l = [[False]*n for _ in range(n)]
# for xy_i in xy:
# 	a, b = xy_i[0]-1, xy_i[1]-1
# 	l[a][b] = l[b][a] = True

# max_len = 0
# for i in range(1<<n):
# 	count = 0
# 	flag = True
# 	for a in range(n):
# 		if (i>>a)%2 == 0:
# 			continue
# 		count += 1
# 		for b in range(a+1, n):
# 			if (i>>b)%2 == 0:
# 				continue
# 			if l[a][b] == False:
# 				flag = False
# 	if flag:
# 		max_len = max(max_len, count)

# print(max_len)