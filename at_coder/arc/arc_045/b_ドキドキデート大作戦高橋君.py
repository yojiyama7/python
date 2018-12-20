# accumulateなのはわかるんだがなぁ、、、
# 0, 1 を累積和して、取得の値が幅と同じだけあれば、全てが一と判定できる、、、。
from itertools import accumulate

N, M = map(int, input().split(" "))
ST = [list(map(int, input().split(" "))) for _ in range(M)]

u = [set() for _ in range(M)]
l = [0]*(M+1)
for i, (s, t) in enumerate(ST):
    l[s-1] += 1
    l[t] -= 1
    u[].add()

for i, m in enumerate(list(accumulate(l))[:-1]):
    if i <= 1:
        continue
    
    
    # count = 0
    # for j in len(bin(i)):
    #     if (i<j)%2 == 0:
    #         continue
    #     count += 1
    # if count <= 1:
    #     continue
    # for j in len(bin(i)):
    #     if (i<j)%2 == 0:
    #         continue
    #     print(j)