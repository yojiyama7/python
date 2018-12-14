
################################
#-------------------------------
################################
# わからんのだよなぁ　どこ基準でなのか

# from collections import deque

# ADS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# H, W, T = map(int, input().split(" "))
# S = [list(input()) for _ in range(H)]

# for y, line in enumerate(S):
#     if "S" in line:
#         s_pos = s_x, s_y = (line.index("S"), y)
#     if "G" in line:
#         g_pos = g_x, g_y = (line.index("G"), y)

# costs = [[10**9 for _ in range(W)] for _ in range(H)]
# costs[s_y][s_x] = 0

# q = deque([s_pos])
# while q:
#     this_pos = this_x, this_y = q.popleft()
#     # if this_pos == g_pos:
#     #     break
#     this_num = costs[this_y][this_x]

#     for ad_x, ad_y in ADS:
#         pos = x, y = this_x+ad_x, this_y+ad_y
#         if not(0 <= x < W and 0 <= y < H):
#             continue

#         is_black = (S[y][x] == "#")
#         cost = this_num + (100 if is_black else 1)
#         if cost <= costs[y][x]:
#             costs[y][x] = cost
#             if is_black:
#                 q.append(pos)
#             else:
#                 q.appendleft(pos)

# g_cost = costs[g_y][g_x]
# white, black = g_cost%100, g_cost//100
# print(white, black)
# print((T-white)//black)