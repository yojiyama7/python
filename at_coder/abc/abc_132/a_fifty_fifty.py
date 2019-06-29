S = input()

d = dict()
for s in S:
    if s not in d:
        d[s] = 0
    d[s] += 1

print(["No", "Yes"][tuple(d.values()) == (2, 2)])