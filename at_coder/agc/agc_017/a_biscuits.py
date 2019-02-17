from math import factorial

N, P = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

l = [0, 0]
for a in A:
    l[a%2] += 1

even = (2**l[0])*sum(factorial(l[1])//factorial(l[1]-i)//factorial(i) for i in range(0, l[1]+1, 2))
# print(even, 2**N)
if P:
    print(2**N-even)
else:
    print(even)