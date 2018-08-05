def count_big(s):
    count = 0
    for s_i in s:
        if s_i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            count += 1
    return count

s = input()
if s[0] == "A" and s[2:-1].count("C") == 1 and count_big(s) == 2:
    print("AC")
else:
    print("WA")