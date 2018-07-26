n = int(input())
s = input()

max_same_count = 0
for i in range(1, n):
	same_count = len(set(s[:i]) & set(s[i:]))
	if max_same_count < same_count:
		max_same_count = same_count

print(max_same_count)