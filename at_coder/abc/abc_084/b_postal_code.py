def all_num(text):
    for c in text:
        if not c in "1234567890":
            return False
    return True

a, b = [int(m) for m in input().split(" ")]
s = input()

print("Yes" if all([all_num(s[:a]), s[a] == "-", all_num(s[a+1:a+1+b])]) else "No")