h, w = map(int, input().split(" "))
c = [input() for i in range(h)]

print("\n".join(["{0}\n{0}".format(line) for line in c]))