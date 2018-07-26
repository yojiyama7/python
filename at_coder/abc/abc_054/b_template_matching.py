n, m = map(int, input().split(" "))
a = [input() for i in range(n)]
b = [input() for i in range(m)]

for y in range(n-m+1):
    for x in range(n-m+1):
        if [line[x:x+m] for line in a[y:y+m]] == b:
            print("Yes")
            exit()
print("No")