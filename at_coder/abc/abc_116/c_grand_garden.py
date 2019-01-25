from itertools import groupby

N = int(input())
H = list(map(int, input().split(" ")))

l = H
count = 0
for i in range(max(H), 0, -1):
    count += sum(key for key, _ in groupby(l, key=lambda x: x==i))
    l = [l_i-1 if l_i == i else l_i for l_i in l]
    # print(l)

print(count)