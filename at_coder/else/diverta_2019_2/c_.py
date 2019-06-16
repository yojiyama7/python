# くそコードでも、通れば正義
N = int(input())
A = list(map(int, input().split(" ")))

A.sort()
if A[-1] < 0:
    s = A[-1]
    sa_list = []
    for a in A[:-1]:
        sa_list.append((s, a))
        s -= a
    print(s)
    for s, a in sa_list:
        print(s, a)
elif 0 <= A[0]:
    s = A[0]
    sa_list = []
    for a in A[1:-1]:
        sa_list.append((s, a))
        s -= a
    sa_list.append((A[-1], s))
    A[-1] -= s 
    print(A[-1])
    for s, a in sa_list:
        print(s, a)
else:
    s = A[-1]
    sa_list = []
    end = None
    for i, a in enumerate(A):
        if i == 0:
            continue
        if 0 <= a:
            end = i
            break
        sa_list.append((s, a))
        s -= a
    t = A[0]
    for a in A[end:-1]:
        sa_list.append((t, a))
        t -= a
    sa_list.append((s, t))
    s -= t
    print(s)
    for s, a in sa_list:
        print(s, a)