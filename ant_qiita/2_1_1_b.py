from itertools import zip_longest

abcd = input()

for i in range(0, 8):
	signs = bin(i)[2:].zfill(3).replace("1", "+").replace("0", "-")
	formula = "".join("".join(s) for s in zip_longest(abcd, signs, fillvalue=""))
	if eval(formula) == 7:
		print(formula+"=7")
		exit()
