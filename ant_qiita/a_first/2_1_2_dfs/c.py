n, m = map(int, input().split(" "))
uv = [list(map(int, input().split(" "))) for i in range(m)]

l = [None] + [set() for _ in range(n)]
for u_i, v_i in uv:
	l[u_i].add(v_i)
	l[v_i].add(u_i)

visited = [None] + [False for _ in range(n)]
def dfs(num, before=None):
	if visited[num]:
		return False
	visited[num] = True

	can_moves = l[num] - {before}
	if not can_moves:
		return True	
	
	flag = True
	for can_move in can_moves:
		if dfs(can_move, num):
			continue
		flag = False
	return flag

count = 0
while False in visited:
	# print(visited)
	count += dfs(visited.index(False))
print(count)

########################################

# n, m = map(int, input().split(" "))
# uv = [list(map(int, input().split(" "))) for _ in range(m)]

# l = [None] + [set() for _ in range(n)]
# for u_i, v_i in uv:
# 	l[u_i].add(v_i)
# 	l[v_i].add(u_i)
# visited = [None] + [False]*n

# def dfs(num, one_before=None, is_tree=True):
# 	visited[num] = True
# 	can_moves = l[num] - {one_before}
# 	for can_move in can_moves:
# 		if visited[can_move]:
# 			return False
# 		if dfs(can_move, num, is_tree) == False:
# 			return False
# 	return True

# count = 0
# while False in visited:
# 	count += dfs(visited.index(False))

# print(count)




