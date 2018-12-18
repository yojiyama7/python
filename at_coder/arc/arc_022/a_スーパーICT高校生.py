S = input()

m = 0
for s in S.lower():
    if s == "ict"[m]:
        m += 1
        if m >= 3:
            print("YES")
            exit()
print("NO")