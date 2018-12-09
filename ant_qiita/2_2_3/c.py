
################################
#---#---#---#---#---#---#---#---
################################

# from collections import Counter

# def fix(shape, chars):
# 	shape_c, chars_c = Counter(shape), chars
# 	only_shape, only_chars = shape_c - chars_c, chars_c - shape_c
# 	ans = ""
# 	for c in shape:
# 		if c not in only_shape:
# 			ans += c
# 			continue
# 		while True:
# 			chars_min = min(only_chars)
# 			if only_chars[chars_min] <= 0:
# 				del only_chars[chars_min]
# 				continue
# 			break
# 		ans += chars_min
# 		only_chars[chars_min] -= 1
# 	return ans

# # print(fix("coder", "deort"))

# n, k = map(int, input().split(" "))
# s = input()

# t = Counter(s)

# ans = ""
# for i in range(n):
# 	t_min = min(t)
# 	t[t_min] -= 1
# 	if t[t_min] <= 0:
# 		del t[t_min]
# 	diff = (s[i] != t_min) + (n - (i+1) - sum((Counter(s[i+1:]) & t).values()))
# 	if diff <= k:
# 		ans += t_min
# 		k -= diff
# 	else:
# 		t[t_min] += 1
# 		print(ans + fix(s[i:], t))
# 		exit()

# print("".join(sorted(s)))

################################

# sort_s = "".join(sorted(s))
# s_counter = Counter(s)
# sort_s_counter = Counter(sort_s)

# for i in range(n):
# 	s_counter[s[i]] -= 1
# 	sort_s_counter[sort_s[i]] -= 1
# 	change_count = (n-i-1) - sum((s_counter & sort_s_counter).values())
# 	print(k, change_count, s_counter & sort_s_counter, change_count)
# 	if change_count > k:
# 		print(sort_s[:i] + fix(s[i:], sort_s[i:]))
# 		exit()
# 	k -= change_count

# print(sort_s)


################################

# # もうだめだそういうことだ。

# n, k = map(int, input().split(" "))
# s = input()

# s = list(s)
# t = sorted(s)

# r = ""
# for i in range(n):
# 	smallest = t[0]
# 	s_ = s[:]
# 	s_.remove(smallest)
# 	t[1:]