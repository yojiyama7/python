s = input()

for a, b in zip(s, s[::-1]):
    if a=="*" or b=="*" or a==b:
        continue
    print("NO")
    exit()
print("YES")