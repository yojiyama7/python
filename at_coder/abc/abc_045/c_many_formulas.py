# 文字列操作が無駄に多いので、二進数の1の位置で分割するようにしたほうがいい

from itertools import zip_longest, chain

s = input()

sign_amount = len(s)-1
table = str.maketrans("01", " +")

sum_num = 0
for i in range(2 ** sign_amount):
	bin_str = bin(i)[2:].zfill(sign_amount)
	signs = bin_str.translate(table)
	formula = "".join(chain(*zip_longest(s, signs, fillvalue=" "))).replace(" ", "")
	sum_num += eval(formula)

print(sum_num)