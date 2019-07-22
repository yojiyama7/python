N = int(input())
A = [int(input()) for _ in range(N)]

b = sorted(A)
for a in A:
    if a == b[-1]:
        print(b[-2])
    else:
        print(b[-1])