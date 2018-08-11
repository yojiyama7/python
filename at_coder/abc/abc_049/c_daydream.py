s = input()

while "" != s:
    result = False
    for word in ("dream", "dreamer", "erase", "eraser"):
        if s[-len(word):] == word:
            s = s[:-len(word)]
            result = True
            break
    if result == False:
        break
print("YES" if result else "NO")