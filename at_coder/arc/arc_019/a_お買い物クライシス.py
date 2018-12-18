S = input()

s = S
for b, a in ["O0", "D0", "I1", "Z2", "S5", "B8"]:
    s = s.replace(b, a)
print(s)