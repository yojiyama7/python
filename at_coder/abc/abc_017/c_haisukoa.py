from itertools import accumulate

N, M = map(int, input().split(" "))
LRS = [list(map(int, input().split(" "))) for _ in range(N)]

score_sum = 0
points = [0 for _ in range(M+1)]
for l, r, s in LRS:
    points[l-1] += s
    points[r] -= s
    score_sum += s

scores = list(accumulate(points))[:-1]
# print(scores)
print(score_sum-min(scores))