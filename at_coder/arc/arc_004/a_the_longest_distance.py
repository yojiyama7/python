N = int(input())
XY = [list(map(int, input().split(" "))) for _ in range(N)]

max_num = 0
for x1, y1 in XY:
    for x2, y2 in XY:
        max_num = max(max_num, (abs(x1-x2)**2 + abs(y1-y2)**2)**(1/2))

print(max_num)