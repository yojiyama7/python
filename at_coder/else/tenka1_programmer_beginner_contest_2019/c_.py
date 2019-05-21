from itertools import groupby, accumulate

N = int(input())
S = input()

l = [len(list(g)) for k, g in groupby(S)]
if S[0] == ".":
    l.pop(0)
if S[-1] == "#":
    l.pop()

if len(l) == 0:
    print(0)
    exit()

min_num = 10**18

black = [0] + list(accumulate(l[::2]))
white = [0] + list(accumulate(l[1::2]))

x = len(l)//2
for i in range(x+1):
    m = (black[i] - black[0]) + (white[x] - white[i])
    min_num = min(m, min_num)

print(min_num)
