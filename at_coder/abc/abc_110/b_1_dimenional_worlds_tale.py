n, m, x, y = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

print("No War" if max([x]+a) < min([y]+b) else "War")