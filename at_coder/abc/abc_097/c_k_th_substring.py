def n_gram(s, n):
	return [s[i:i+n] for i in range(len(s)-n+1)]

s = input()
k = int(input())

subs = set()
for k_i in range(1, k+1):
	subs = subs | set(n_gram(s, k_i))
print(sorted(subs)[k-1])