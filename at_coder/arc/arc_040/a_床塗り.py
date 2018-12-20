N = int(input())
S = [input() for _ in range(N)]

red, blue = 0, 0
for s in "".join(S):
    if s == "R":
        red += 1
    elif s == "B":
        blue += 1

if red > blue:
    print("TAKAHASHI")
elif red < blue:
    print("AOKI")
else:
    print("DRAW")