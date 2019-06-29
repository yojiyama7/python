N = int(input())
D = list(map(int, input().split(" ")))

D.sort()
a, b = D[N//2-1], D[N//2]

print(b-a)