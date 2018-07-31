abc = [int(input()) for i in range(3)]

for abc_i in abc:
    print(3-sorted(abc).index(abc_i))