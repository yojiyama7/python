n = int(input())
s = tuple(map(int, input().split(" ")))

count = 0
before = None
for s_i in s:
    if before == s_i:
        count += 1
        before = None
    else:
        before = s_i
print(count)
