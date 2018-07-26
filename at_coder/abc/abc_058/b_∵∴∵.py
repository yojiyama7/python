from itertools import zip_longest, chain

o = input()
e = input()

print("".join(chain(*zip_longest(o, e, fillvalue=""))))