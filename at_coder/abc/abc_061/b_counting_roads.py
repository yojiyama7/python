import sys

n, m = map(int, input().split(" "))
ab = [[int(m) for m in input().split(" ")] for i in range(m)]

roads_count = [0 for i in range(n)]
for a_i, b_i in ab:
    if a_i != b_i:
        roads_count[a_i-1] += 1
        roads_count[b_i-1] += 1
[print(num) for num in roads_count]