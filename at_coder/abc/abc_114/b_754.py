s = input()
print(min(map(lambda x: abs(753 - int(x)), (s[i:i+3] for i in range(len(s)-2)))))