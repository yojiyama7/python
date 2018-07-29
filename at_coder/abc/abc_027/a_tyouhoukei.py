l = tuple(map(int, input().split(" ")))

print([l_i for l_i in set(l) if l.count(l_i) != 2][0])