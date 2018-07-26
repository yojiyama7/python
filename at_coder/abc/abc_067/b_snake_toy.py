n, k = map(int, input().split(" "))
l = map(int, input().split(" "))

print(sum(sorted(l, reverse=True)[:k]))