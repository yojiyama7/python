N = int(input())
A = list(map(int, input().split(" ")))

if sum(a < 0 for a in A) % 2 == 0:
    print(sum(map(abs, A)))
else:
    print(sum(map(abs, A)) - 2*min(map(abs, A)))