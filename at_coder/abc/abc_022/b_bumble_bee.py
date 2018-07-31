n = int(input())
a = [input() for i in range(n)]

count = 0
already_type = set()
for a_i in a:
    if a_i in already_type:
        count += 1
    else:
        already_type.add(a_i)
print(count)