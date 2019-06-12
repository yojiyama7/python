# 配列はnumpyを使おう

# # TLE
# H, W = map(int, input().split(" "))
# S = [input() for _ in range(H)]

# l, r, d, u = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(4)]

# for y in range(H):
#     for x in range(W):
#         if S[y][x] == "#":
#             l[y][x] = -1
#         elif x == 0:
#             l[y][x] = 0
#         else:
#             l[y][x] = l[y][x-1] + 1
# for y in range(H):
#     for x in range(W-1, -1, -1):
#         if S[y][x] == "#":
#             r[y][x] = -1
#         elif x == W-1:
#             r[y][x] = 0
#         else:
#             r[y][x] = r[y][x+1] + 1
# for x in range(W):
#     for y in range(H):
#         if S[y][x] == "#":
#             u[y][x] = -1
#         elif y == 0:
#             u[y][x] = 0
#         else:
#             u[y][x] = u[y-1][x] + 1
# for x in range(W):
#     for y in range(H-1, -1, -1):
#         if S[y][x] == "#":
#             d[y][x] = -1
#         elif y == H-1:
#             d[y][x] = 0
#         else:
#             d[y][x] = d[y+1][x] + 1

# max_num = 0
# for y in range(H):
#     for x in range(W):
#         m = l[y][x] + r[y][x] + u[y][x] + d[y][x] + 1
#         # if m > max_num:
#         #     print(x, y, l[y][x], r[y][x], u[y][x], d[y][x], m)
#         max_num = max(max_num, m)

# print(max_num)