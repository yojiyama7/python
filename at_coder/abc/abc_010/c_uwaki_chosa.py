SX, SY, GX, GY, T, V = map(int, input().split(" "))
N = int(input())
XY = [list(map(int, input().split(" "))) for _ in range(N)]

for x, y in XY:
    d = ((x-SX)**2 + (y-SY)**2) ** (1/2)
    d += ((GX-x)**2 + (GY-y)**2) ** (1/2)
    if d <= V*T:
        print("YES")
        exit()
print("NO")