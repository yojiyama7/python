from fractions import gcd

N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

m = A[0]
for a in A[1:]:
    m = gcd(a, m)

print("IM"*(K>max(A) or K%m != 0)+"POSSIBLE")