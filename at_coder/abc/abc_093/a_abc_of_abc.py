s = input()

print("Yes" if all([c in s for c in "abc"]) else "No")