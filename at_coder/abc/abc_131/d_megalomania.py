N = int(input())
AB = [list(map(int, input().split(" "))) for _ in range(N)]

AB.sort(key=lambda x: x[1])
# print(AB)

time = 0
for a, b in AB:
    time += a
    # print(time, b, b<time)
    if b < time:
        print("No")
        exit()
print("Yes")