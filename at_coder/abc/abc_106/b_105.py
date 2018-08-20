from bisect import bisect_right

n = int(input())

print(bisect_right([105, 135, 165, 189, 195], n))

# from itertools import chain

# def divisor_gen(n):
#   for i in range(2, int(n**(1/2))+1):
#     if n % i == 0:
#       yield [i, int(n/i)]

# # n = int(input())

# print([i for i in range(1, 201) if len(list(chain(*divisor_gen(i))))==6 and i%2==1]  )