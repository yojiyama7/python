N = int(input())
XU = [input().split(" ") for _ in range(N)]

print(sum([float(x)*{"JPY": 1, "BTC": 380000}[u] for x, u in XU]))