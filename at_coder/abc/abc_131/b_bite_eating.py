N, L = map(int, input().split(" "))

a = list(range(L, L+N))
a.sort(key=abs)

print(sum(a[1:]))