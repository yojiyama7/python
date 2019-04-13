N, M = map(int, input().split(" "))
AB = [list(map(int, input().split(" "))) for _ in range(N)]

AB.sort(key=lambda x: x[0])

sum_num = 0
for a, b in AB:
    c = min(b, M)
    sum_num += a*c
    # print(a*c, c, M)
    M -= c
    if M <= 0:
        break

print(sum_num)