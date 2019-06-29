N = int(input())
P = list(map(int, input().split(" ")))

a, b = P[:2]
count = 0
for c in P[2:]:
    if sorted([a, b, c])[1] == b:
        count += 1
    a, b = b, c

print(count)