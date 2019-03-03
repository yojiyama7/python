# AC

D, G = map(int, input().split(" "))
PC = [list(map(int, input().split(" "))) for _ in range(D)]

min_count = 10**18
for i in range(1<<D):
    # print(bin(i)[2:])
    count = 0
    point = 0
    top_zero = None
    for j, (p, c) in enumerate(PC):
        if (i>>j)%2:
            count += p
            point += 100*(j+1)*p + c
        else:
            top_zero = j
    if top_zero != None:
        for j in range(PC[top_zero][0]-1):
            # print(j, top_zero, point)
            if point >= G:
                break
            point += 100*(top_zero+1)
            count += 1
    # print("count:", count)
    if point >= G:
        min_count = min(min_count, count)

print(min_count)

################################

# # RE

# D, G = map(int, input().split(" "))
# P, C = zip(*[list(map(int, input().split(" "))) for _ in range(D)])

# def dfs(i, point, last_unsolve=-1):
#     if i == D:
#         return 0
#     l = [
#         dfs(i+1, point + 100*(i+1)*p+c) + p,
#         dfs(i+1, point, last_unsolve=i)
#     ]
