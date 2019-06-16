N = int(input())
XY = [list(map(int, input().split(" "))) for _ in range(N)]

d = {(-1, -1): 0}
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        x1, y1 = XY[i]
        x2, y2 = XY[j]
        x3, y3 = x2-x1, y2-y1
        # 条件付けミス(or以降)
        if x3 < 0 or (x3 == 0 and y3 < 0):
            x3, y3 = -1*x3, -1*y3
        pos = (x3, y3)
        if pos not in d:
            d[pos] = 0
        d[pos] += 1

# print(d.values(), d, max(d.values()))
print(N - max(d.values())//2)