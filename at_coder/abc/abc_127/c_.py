from itertools import accumulate

N, M = map(int, input().split(" "))
LR = [list(map(int, input().split(" "))) for _ in range(M)]

q = [0] * (N+1)
for l, r in LR:
    # print(l, r)
    q[l-1] += 1
    q[r] -= 1

# print(q, list(accumulate(q)))

print(sum(M == m for m in list(accumulate(q))[:-1]))