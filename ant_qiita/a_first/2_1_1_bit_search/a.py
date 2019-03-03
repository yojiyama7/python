s = input()

s_len = len(s)

sum_num = 0
for i in range(1<<(s_len-1), 1<<s_len):
	n, a = 0, 0
	for j in range(s_len):
		if (i>>j)%2 == 0:
			continue
		n += int(s[a:j+1])
		a = j+1
	sum_num += n

print(sum_num)

################################

# from itertools import zip_longest

# s = input()

# sum_num = 0
# for i in range(0, 2**(len(s)-1)):
# 	sings = bin(i)[2:].zfill(len(s)-1).replace("1", "+").replace("0", " ")
# 	formula = ("".join("".join(t) for t in zip_longest(s, sings, fillvalue=" "))).replace(" ", "")
# 	sum_num += eval(formula)

# print(sum_num)