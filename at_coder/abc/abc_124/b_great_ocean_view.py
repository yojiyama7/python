N = int(input())
H = list(map(int, input().split(" ")))

count = 0
g = 0
for h in H:
    # print(h, g)
    if h >= g:
        count += 1
        g = h

print(count)