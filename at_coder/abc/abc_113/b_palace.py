n = int(input())
t, a = map(int, input().split(" "))
h = list(map(int, input().split(" ")))

b = [abs((t - 0.006*h_i) - a) for h_i in h]
print(b.index(min(b))+1)

