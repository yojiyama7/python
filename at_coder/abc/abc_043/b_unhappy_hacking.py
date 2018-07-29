s = input()

text = ""
for s_i in s:
	if s_i == "B":
		text = text[:-1]
	else:
		text += s_i
print(text)