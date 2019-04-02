from itertools import accumulate

N, Q = map(int, input().split(" "))
S = input()
LR = [list(map(int, input().split(" "))) for _ in range(Q)]

p = (S[i:i+2]=="AC" for i in range(N))
p = [0] + list(accumulate(p))

# print(p)

for l, r in LR:
    l, r = l-1, r
    # print(S[l:r], l, r)
    print(p[r-1]-p[l])