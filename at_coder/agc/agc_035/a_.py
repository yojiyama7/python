N = int(input())
A = list(map(int, input().split(" ")))

m = A[0]
for i in range(1, N):
    m ^= A[i]

if m == 0:
    print("Yes")
else:
    print("No")