N = int(input())
A = list(map(int, input().split(" ")))

x = sum(A[::2])-sum(A[1::2])
l = [x]
for i in range(N-1):
    m = (A[i] - l[-1]//2) * 2
    l.append(m)

print(*l)