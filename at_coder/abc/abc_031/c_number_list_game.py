n = int(input())
a = tuple(map(int, input().split(" ")))

r = -10000000000000
for i in range(n):
    max_in_j = -10000000000000
    for j in range(n):
        min_ij, max_ij = min(i, j), max(i, j)
        if i != j: # 愚直な実装は読みやすい
            if max_in_j < sum(a[min_ij+1:max_ij+1:2]):
                max_in_j = sum(a[min_ij+1:max_ij+1:2])
                max_j = j
    min_ij, max_ij = min(i, max_j), max(i, max_j)
    if r < sum(a[min_ij:max_ij+1:2]):
        r = sum(a[min_ij:max_ij+1:2])

print(r)