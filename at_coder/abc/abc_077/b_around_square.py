n = int(input())

before_square = 1
max_square = 1
while before_square**2 <= n:
    max_square = before_square ** 2
    before_square += 1

print(max_square)