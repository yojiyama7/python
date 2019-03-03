s, t = [input() for _ in range(2)]

n, m = map(len, [s, t])
for i in range(n-m, -1, -1):
	if not all(s_j in ["?", t_j] for s_j, t_j in zip(s[i:i+m], t)):
		continue
	print((s[:i] + t + s[i+m:]).replace("?", "a"))
	exit()
print("UNRESTORABLE")

################################

# s, t = [input() for _ in range(2)]
# t_len = len(t)

# def is_fit(a, b):
# 	for i in range(t_len):
# 		if a[i] not in [b[i], "?"]:
# 			return False
# 	return True

# for i in range(len(s)-t_len, -1, -1):
# 	if not is_fit(s[i:i+t_len], t):
# 		continue
# 	s = list(s)
# 	s[i:i+t_len] = list(t)
# 	s = "".join(s).replace("?", "a")
# 	print(s)
# 	exit()
# print("UNRESTORABLE")

		