s = input()

s = s[0] + s

count = 0
for i in range(len(s)-1):
	if s[i] != s[i+1]:
		count += 1
print(count)