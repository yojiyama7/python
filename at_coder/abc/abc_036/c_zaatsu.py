n = int(input())
a = [int(input()) for _ in range(n)]

d = dict(zip(sorted(set(a)), range(len(set(a)))))
for a_i in a:
    print(d[a_i])