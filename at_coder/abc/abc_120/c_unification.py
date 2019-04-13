S = input()

n = len(S)

red, blue = 0, 0
for s in S:
    if s == "0":
        if blue > 0:
            blue -= 1
        else:
            red += 1
    else:
        if red > 0:
            red -= 1
        else:
            blue += 1

print(n-red-blue)
