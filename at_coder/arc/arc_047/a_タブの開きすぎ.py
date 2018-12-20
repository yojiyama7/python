N, L = map(int, input().split(" "))
S = input()

tab = 1
count = 0
for s in S:
    if s == "+":
        tab += 1
    else:
        tab -= 1
    if tab > L:
        count += 1
        tab = 1

print(count)