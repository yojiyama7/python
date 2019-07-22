# 期待値は苦手な奴だなぁ

from math import factorial

N = int(input())
C = [int(input()) for _ in range(N)]

count = 0
for i in range(N):
    divisor = 0
    for j in range(N):
        if i == j:
            continue
        if C[i]%C[j]:
            continue
        divisor += 1
    count += (divisor//2+1)/(divisor+1)

print(count)