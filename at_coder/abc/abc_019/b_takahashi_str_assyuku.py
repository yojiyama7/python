s = input()

text = ""
c = s[0]
count = 0
for s_i in s:
    if c != s_i:
        text += c + str(count)
        count = 0
        c = s_i
    count += 1
text += c + str(count)
print(text)