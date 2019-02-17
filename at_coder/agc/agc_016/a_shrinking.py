S = input()

t = [set(s) for s in S]

for i in range(len(S)):
    print(t)
    u = [t[j]|t[j+1] for j in range(len(t)-1)]
    a = u[0]
    for u_i in u[1:]:
        a = a&u_i
    print(u, a)
    if len(a):
        print(i)
        exit()
    t = u

