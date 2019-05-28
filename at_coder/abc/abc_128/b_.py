N = int(input())
SP = [input().split(" ") for _ in range(N)]

l = sorted([(i+1, s, int(p)) for i, (s, p) in enumerate(SP)], key=lambda x: (x[1], -x[2]))

for l_i in l:
    print(l_i[0])