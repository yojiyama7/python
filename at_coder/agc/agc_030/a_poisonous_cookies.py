A, B, C = map(int, input().split(" "))

if A+B < C:
    # print("a")
    print(A+B+1+B)
else:
    # print("b")
    print(B+C)