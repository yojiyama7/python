S = input()

t = ""
for s in S:
    if s in "0123456789":
        t += s

print(t)