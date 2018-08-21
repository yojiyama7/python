n = int(input())
a = list(map(int, input().split(" ")))

a = a + [-1]

m = 0
count = 0
for i in range(n):
    if a[i] < a[i+1]:
        m += 1
    elif m > 0:
        count += int((m+1)*(m/2))
        m = 0
count += n

print(count)