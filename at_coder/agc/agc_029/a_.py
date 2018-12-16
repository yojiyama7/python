S = input()

white = 0
count = 0
for i, s in enumerate(S):
    if s == "W":
        count += i-white
        white += 1

print(count)