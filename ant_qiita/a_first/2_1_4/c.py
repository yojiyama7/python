from itertools import permutations as p
from math import factorial as fact

n = int(input())
a, b = [tuple(map(int, input().split(" "))) for _ in range(2)]

count = 0
for a_i in p(a, n):
	for b_i in p(b, n):
		count += (sum(a_j > b_j for a_j, b_j in zip(a_i, b_i)) / n > 0.5)

print(count / fact(n)**2)

################################

# from itertools import permutations, product
# from math import factorial

# def int_or_float(n):
# 	return int(n) if n%1 == 0 else n

# n = int(input())
# a, b = [list(map(int, input().split(" "))) for _ in range(2)]

# # 読めねえよ
# print(int_or_float(sum(sum(a_i>b_i for a_i, b_i in zip(*x)) > n/2 for x in list(product(permutations(a, n), permutations(b, n)))) / factorial(n)**2))
