n, m = map(int, input().split(" "))
ab = [list(map(int, input().split(" "))) for _ in range(m)]
 
s = [set() for _ in range(n)]
for ab_i in ab:
	a_i, b_i = map(lambda x: x-1, ab_i)
	s[a_i].add(b_i)
	s[b_i].add(a_i)
 
# print(s)
 
def dfs(num, visited=set()):
	visited = visited | {num}
	can_moves = s[num] - visited
	# print(num, can_moves, visited)
	if not can_moves:
		return (len(visited) == n)
	return sum(dfs(can_move, visited) for can_move in can_moves)
 
print(dfs(0))