s = input()
t = input()

print("Yes" if t in [s[i:]+s[:i] for i in range(len(s))] else "No")