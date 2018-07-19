a, b = [int(m) for m in input().split(" ")]

height_sub = b - a
print(int((height_sub + 1)*height_sub/2 - b))