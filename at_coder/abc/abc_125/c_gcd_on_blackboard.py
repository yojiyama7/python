def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split(" ")))

A.sort()

l = [0]
m = A[0]
for i in range(1, N):
    tmp = gcd(m, A[i])
    if tmp < m:
        l.append(i)
    m = tmp
    # print(m)

max_num = m
for l_i in l:
    b = A.copy()
    b.pop(l_i)
    x = b[0]
    for i in range(1, N-1):
        # print("a:", i)
        x = gcd(x, b[i])
    # print(x)
    max_num = max(max_num, x)

print(max_num)