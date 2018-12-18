DJ = zip(*[list(map(int, input().split(" "))) for _ in range(2)])

print(sum(map(max, DJ)))