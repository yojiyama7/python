def n_gram(s, n):
	nums = []
	for s_i in range(len(s)-n+1):
		nums.append(s[s_i:s_i+n])
	return nums

s = input()
k = int(input())

print(len(set(n_gram(s, k))))