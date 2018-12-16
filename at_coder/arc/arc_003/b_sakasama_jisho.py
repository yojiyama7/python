N = int(input())
S = [input() for _ in range(N)]

[print(s) for s in sorted(S, key=lambda x: x[::-1])]