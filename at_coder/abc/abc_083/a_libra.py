a, b, c, d = [int(m) for m in input().split(" ")]

if a+b < c+d:
    print("Right")
elif a+b > c+d:
    print("Left")
else:
    print("Balanced")