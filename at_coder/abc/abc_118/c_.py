from fractions import gcd

N = int(input())
A = list(map(int, input().split(" ")))

b = A[0]
for a in A[1:]:
    b = gcd(a, b)

print(b)