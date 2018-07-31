n = int(input())

if 1 <= n <= 3:
    print((0, 0, 1)[n-1])
else:
    a, b, c = 0, 0, 1
    for i in range(4, n+1):
        a, b, c = b, c, (a+b+c)%10007
    print(c)
