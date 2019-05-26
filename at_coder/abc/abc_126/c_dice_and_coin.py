from math import log

N, K = map(int, input().split(" "))

sum_num = 0
for i in range(1, N+1):
    count = 0
    while i < K:
        i *= 2
        count += 1
    sum_num += 1 / 2**count
    # print(count, sum_num)

print(sum_num / N)