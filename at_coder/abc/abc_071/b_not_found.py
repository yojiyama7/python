import sys

s = input()

for c in [chr(i) for i in range(97, 97+26)]:
    if not c in s:
        print(c)
        sys.exit()
print("None")