n, t = map(int, input().split(" "))
u = tuple(map(int, input().split(" ")))

print(sum([min(t, u[i+1]-u[i]) for i in range(n-1)]) + t)
