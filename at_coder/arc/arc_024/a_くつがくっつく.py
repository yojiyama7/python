from collections import Counter

N, M = map(int, input().split(" "))
L, R = [list(map(int, input().split(" "))) for _ in range(2)]

print(sum((Counter(L)&Counter(R)).values()))