from itertools import permutations as perm

c = "abcd"

a = []
for i in range(1, len(c)+1):
    a += list(perm(c, i))

for b in sorted(a):
    print(" ".join(b))