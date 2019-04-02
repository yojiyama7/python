from collections import Counter

N = int(input())
S = input()

r = 1
for m in Counter(S).values():
    r = r * (m+1) % (10**9+7)

print(r-1)