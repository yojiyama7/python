from bisect import bisect_right

n = int(input())

print(bisect_right([105, 135, 165, 189, 195], n))

# from itertools import chain

# def divisor_gen(n):
# 	yield [1, n]
# 	for i in range(2, int(n**(1/2))+1):
# 		if n % i == 0:
# 			yield [i, n//i]
# print([i for i in range(1, 201) if len(list(chain(*divisor_gen(i))))==8 and i%2==1])

# def divisor(n):
# 	nums_list = []
# 	for i in range(1, int(n**(1/2))+1):
# 		if n % i == 0:
# 			nums_list.append([i, n//i])
# 	return list(chain(*nums_list))
# print([i for i in range(1, 201) if i%2==1 and len(divisor(i))==8])