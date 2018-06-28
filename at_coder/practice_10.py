# sys.stdin 標準入力全行

# Relative rela
# import sys

# n = int(sys.stdin.readline())
# txy_list = [[int(n) for n in sys.stdin.readline().split()] for i in range(n)]
# times_list = [txy_list[0][0]] + [txy_list[i+1][0] - txy_list[i][0] for i in range(n-1)]

# before_x, before_y = 0, 0
# for i, txy in enumerate(txy_list):
# 	t, x, y = txy
# 	rela_x, rela_y = x - before_x, y - before_y
# 	remaining = times_list[i] - (abs(rela_x) + abs(rela_y))
# 	if 0 <= remaining and remaining % 2 == 0:
# 		before_x, before_y = x, y
# 	else:
# 		print("No")
# 		sys.exit()
# print("Yes")

import sys

n = int(sys.stdin.readline())
before_t, before_x, before_y = 0, 0, 0
for i in range(n):
	txy_strs = sys.stdin.readline().split()
	t, x, y = tuple(map(int, txy_strs))

	movable = t - before_t
	min_move = abs(x - before_x) + abs(y - before_y)

	remaining = movable - min_move
	if 0 <= remaining and remaining % 2 == 0:
		before_t, before_x, before_y = t, x, y
	else:
		print("No")
		sys.exit()
print("Yes")
