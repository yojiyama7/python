N, C, K = map(int, input().split(" "))
T = [int(input()) for _ in range(N)]

T.sort(reverse=True)

count = 0
while T:
    limit = T[-1]+K
    count += 1
    for i in range(C):
        if T and T[-1] <= limit:
            T.pop()
        else:
            break

print(count)