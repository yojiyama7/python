abc = [int(m) for m in input().split(" ")]

for abc_i in set(abc):
    if abc.count(abc_i) == 1:
        print(abc_i)
        break