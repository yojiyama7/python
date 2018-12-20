N, A, B = map(int, input().split(" "))
S = [int(input()) for _ in range(N)]

now_b = max(S) - min(S)
if now_b == B == 0:
    p = 1
if now_b == 0:
    print(-1)
    exit()
else:
    p = B / now_b

q = A-(sum(S)/N*p)

print(p, q)