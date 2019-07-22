N, A, B, C, D = map(int, input().split(" "))
S = input()

if C < D:
    if "##" in S[A:C] or "##" in S[B:D]:
        print("No")
    else:
        print("Yes")
else:
    if "##" in S[A:C] or "##" in S[B:D] or "..." not in S[B-2:D+1]:
        print("No")
    else:
        print("Yes")

# print('YNeos'['##'*('...'*(D<C)in S[B-2:D+1])in S[A:D]::2])