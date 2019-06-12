N, M = map(int, input().split(" "))
A = [int(input()) for _ in range(M)]

l = [0]*(N+10)
l[0] = 1
for a in A:
    l[a] = -1

for i in range(N):
    if l[i] == -1:
        continue
    if l[i+1] != -1:
        l[i+1] = (l[i+1]+l[i])%(10**9+7)
    if l[i+2] != -1:
        l[i+2] = (l[i+2]+l[i])%(10**9+7)

print(l[N])