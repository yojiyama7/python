from itertools import accumulate, groupby

N = int(input())
SE = [input().split("-") for _ in range(N)]

l = [0]*(24*12+1 +1)
for s, e in SE:
    sh, sm = int(s[:2]), int(s[2:])
    eh, em = int(e[:2]), int(e[2:])

    st = (sh*60+sm)//5
    et = -(-(eh*60+em)//5)

    l[st] += 1
    l[et] -= 1

p = list(accumulate(l))
q = []
for i in range(24*12+1):
    time_str = "{0:0>2}{1:0>2}".format(i//12, i%12*5)
    if (p[i-1] == 0 and p[i] != 0):
        q.append(time_str)
    if (p[i-1] != 0 and p[i] == 0):
        q.append(time_str)

for s, e in zip(q[::2], q[1::2]):
    print(s+"-"+e)
