# abc 045 c
from itertools import zip_longest

s = input()

sum_num = 0
for i in range(0, 2**(len(s)-1)):
	sings = bin(i)[2:].zfill(len(s)-1).replace("1", "+").replace("0", " ")
	formula = ("".join("".join(t) for t in zip_longest(s, sings, fillvalue=" "))).replace(" ", "")
	sum_num += eval(formula)

print(sum_num)