n, m = map(int, input().split(" "))
ab = [list(map(int, input().split(" "))) for i in range(n)]
cd = [list(map(int, input().split(" "))) for i in range(m)]

for nx, ny in ab:
    distances = [abs(nx-mx)+abs(ny-my) for mx, my in cd]
    print(distances.index(min(distances))+1)