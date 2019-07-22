# # コピペ
# # 本来は何のためのモジュール?
# from scipy.ndimage import distance_transform_cdt
 
# h, w = map(int, input().split())
# a = [list(input()) for _ in range(h)]
# n = [[1 if x == "." else 0 for x in row] for row in a]
 
# # cnt = distance_transform_cdt(n)
# cnt = distance_transform_cdt(n, metric='taxicab')
# print(cnt)
# print(cnt.max())

from collections import deque
 
ADS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
 
H, W = map(int, input().split(" "))
A = [list(input()) for _ in range(H)]

q = deque()
for y in range(H):
    for x in range(W):
        if A[y][x] == "#":
            q.append((x, y))

count = 0
while q:
    r = list(q)
    q = deque()
    for q_i in r:
        this_pos = this_x, this_y = q_i
        
        for ad_x, ad_y in ADS:
            pos = x, y = this_x+ad_x, this_y+ad_y
            if not ((0 <= x < W) and (0 <= y < H)):
                continue
            if A[y][x] == "#":
                continue
            A[y][x] = "#"
            q.append(pos)
    count += 1
    # print(A, count, q)

print(count-1)


# from collections import deque
 
# ADS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
 
# H, W = map(int, input().split(" "))
# A = [list(input()) for _ in range(H)]
 
# q = deque()
 
# for y in range(H):
#     for x in range(W):
#         if A[y][x] == "#":
#             q.append((x, y))
 
# count = 0
# while q: # 10**6
#     q.append((-1, -1))
#     while q:
#         this_pos = this_x, this_y = q.popleft()
#         if this_pos == (-1, -1):
#             break

#         for ad_x, ad_y in ADS:
#             x, y = this_x+ad_x, this_y+ad_y
#             if not ((0 <= x < W) and (0 <= y < H)):
#                 continue
#             if A[y][x] == "#":
#                 continue
#             A[y][x] = "#"
#             q.append((x, y))
#     count += 1
#     # print(A, q, count)
 
# print(count-1)