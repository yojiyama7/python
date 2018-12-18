# え一人しかいないんだが？？？
# https://atcoder.jp/contests/arc025/submissions/1780175
# 累積和からのCounterで value[C]2
# 考えはあってるのか、、、

################################
#-------------------------------
################################

from itertools import accumulate
H, W = map(int, input().split(" "))
C = [list(map(int, input().split(" "))) for _ in range(H)]

for y in range(H):
    C[y][(y+1)%2::2] = [-m for m in C[y][(y+1)%2::2]]
C = [accumulate([0]+c) for c in [[0]*W]+C]
C = [accumulate(c) for c in zip(*C)]
C = [list(c) for c in zip(*C)]

# [print(c) for c in C]

max_num = 0
for y1 in range(H):
    for x1 in range(W):
        for y2 in range(y1+1, H+1):
            for x2 in range(x1+1, W+1):
                # print(C[y1][x1]-C[y2][x2])
                if C[y2][x2] - C[y2][x1] - C[y1][x2] + C[y1][x1] == 0:
                    max_num = max(max_num, (x1-x2)*(y1-y2))

print(max_num)