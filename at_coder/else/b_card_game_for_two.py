# n = 10
# a = [4, 5, 7, 2, 7, 4, 8, 3, 9, 3]

n = int(input())
a = [int(i) for i in input().split(" ")]

a.sort()
m = n % 2

alice = 0
bob = 0

while n > 0:
    if n % 2 == m:
        alice += a[-1]
    else:
        bob += a[-1]
    a.pop()
    n -= 1

print(alice - bob)