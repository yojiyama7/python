A, B = AB = list(map(int, input().split(" ")))

if A == B:
    print(A+B)
else:
    print(max(AB)*2-1)