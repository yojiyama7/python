from bisect import bisect_left
# 最初最後両方left 

N, Q = map(int, input().split(" "))
STX = [list(map(int, input().split(" "))) for _ in range(N)]
D = [int(input()) for _ in range(Q)]

q = [-1]*Q
for s, t, x in STX[::-1]:
    l = bisect_left(D, max(0, s-x))
    r = bisect_left(D, max(0, t-x))
    # print(s, t, x, l, r)
    count = r-l
    for i in range(count):
        if 0 <= q[l+i] < x:
            continue
        q[l+i] = x
    

# print(q)

for q_i in q:
    print(q_i)