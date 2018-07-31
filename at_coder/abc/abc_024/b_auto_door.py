n, t = map(int, input().split(" "))
a = [int(input()) for i in range(n)]

print(sum([min(a[i+1] - a[i], t) for i in range(len(a)-1)])+t)