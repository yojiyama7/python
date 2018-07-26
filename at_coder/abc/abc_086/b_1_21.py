import sys

a, b = input().split(" ")

link_ab = int(a+b)

for i in range(link_ab):
    if link_ab == i**2:
        print("Yes")
        sys.exit()
print("No")
