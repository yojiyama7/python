n = int(input())
xy = [tuple(map(int, input().split(" "))) for _ in range(n)]

max_num = 0
for x_i, y_i in xy:
    for x_j, y_j in xy:
        max_num = max(max_num, (abs(x_i-x_j)**2 + abs(y_i-y_j)**2) ** (1/2))

print(max_num)

################################

# n = int(input())
# xy = [tuple(map(int, input().split(" "))) for _ in range(n)]

# max_line = 0
# for x_i, y_i in xy:
#     for x_j, y_j in xy:
#         length = (abs(y_i-y_j)**2 + abs(x_i-x_j)**2) ** (1/2) 
#         if length > max_line:
#             max_line = length

# print(max_line)