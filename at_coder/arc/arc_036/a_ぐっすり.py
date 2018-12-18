N, K = map(int, input().split(" "))
T = [int(input()) for _ in range(N)]

T += [0] # -1アクセス用

s = sum(T[:2])
for i in range(2, N):
    s += T[i]
    s -= T[i-3]
    if s < K:
        print(i+1)
        exit()
print(-1)
