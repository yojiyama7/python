N = int(input())

l = []
for i in range(1, 555555+1):
    if len(set(str(i))) == 1:
        l.append(i)

print(l[N-1])