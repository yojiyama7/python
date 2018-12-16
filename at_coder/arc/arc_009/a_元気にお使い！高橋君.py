N = int(input())
AB = [list(map(int, input().split(" "))) for _ in range(N)]

total = sum(n*v for n, v in AB)
print(int(total*1.05))