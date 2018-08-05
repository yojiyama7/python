n = int(input())
s = [input() for _ in range(n)]

chars = set(s[0])
for s_i in s[1:]:
    chars &= set(s_i)

text = ""
for c in sorted(chars):
    text += c*min(s_i.count(c) for s_i in s)
print(text)
