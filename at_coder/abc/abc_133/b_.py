N, D = map(int, input().split(" "))
X = [list(map(int, input().split(" "))) for _ in range(N)]

count = 0
for i in range(N):
    for j in range(i+1, N):
        m = sum((y-z)**2 for y, z in zip(X[i], X[j]))**(1/2)
        # print(i, j, m)
        if m % 1 == 0:
            count += 1

print(count)