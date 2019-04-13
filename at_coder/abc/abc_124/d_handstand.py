from itertools import groupby

N, K = map(int, input().split(" "))
S = input()

# print([list(g) for k, g in groupby(S)])
l = [len(list(g)) for k, g in groupby(S)]

if S[0] == "0":
    l = [0] + l
if S[-1] == "0":
    l += [0]

# print(l)

w = K*2+1

m = sum(l[:w])
max_num = m
for i in range(len(l)-w):
    # print(w, i)
    m -= l[i]
    m += l[w+i]
    if i%2 == 1:
        # print(m)
        max_num = max(max_num, m)

print(max_num)
