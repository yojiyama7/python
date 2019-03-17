N = int(input())
TXY = [list(map(int, input().split(" "))) for _ in range(N)]

for t, x, y in TXY:
    if x+y <= t and t%2 == (x+y)%2:
        continue
    print("No")
    exit()

print("Yes")