n, x = map(int, input().split(" "))
a = tuple(map(int, input().split(" ")))

a_in = [max(0, a[i] + a[i+1] - x) for i in range(n-1)]

count = 0
while set(a_in) != {0}:
    i = max(range(0, n-2), key=lambda x: a_in[x]+a_in[x+1])
    a_in[i]   = max(0, a_in[i] - 1)
    a_in[i+1] = max(0, a_in[i+1] - 1)
    count += 1
    print(a_in)

print(count)