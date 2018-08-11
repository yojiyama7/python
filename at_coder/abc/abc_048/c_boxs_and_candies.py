n, x = map(int, input().split(" "))
a = tuple(map(int, input().split(" ")))

[min(0, x - a[i+1]+a[i]) for i in range(n-1)]